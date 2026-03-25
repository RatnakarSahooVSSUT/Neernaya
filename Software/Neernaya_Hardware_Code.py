import time
import board
import busio
import statistics
import requests
import RPi.GPIO as GPIO
from statistics import mean
from w1thermsensor import W1ThermSensor
from RPLCD.i2c import CharLCD
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- LED ----------------

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.HIGH)

# ---------------- LCD ----------------

lcd = CharLCD('PCF8574', 0x27, cols=20, rows=4)

time.sleep(1)
lcd.clear()

lcd.cursor_pos = (0, 0)
lcd.write_string("NEERNAYA")

lcd.cursor_pos = (1, 0)
lcd.write_string("Aquaculture Monitor")

lcd.cursor_pos = (2, 0)
lcd.write_string("Preparing Readings")

print("System Started")
print("---------------------------")

start_time = time.time()

# ----------- 60 SECOND COUNTDOWN -----------

for remaining in range(60, 0, -1):
    lcd.cursor_pos = (3, 0)
    lcd.write_string("Reading in {:2d}s   ".format(remaining))
    time.sleep(1)

lcd.clear()

# ---------------- I2C + ADC ----------------

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)
ads.gain = 1

turbidity_channel = AnalogIn(ads, 0)
tds_channel = AnalogIn(ads, 1)
do_channel = AnalogIn(ads, 2)
ph_channel = AnalogIn(ads, 3)

# ---------------- TEMPERATURE ----------------

temp_sensor = W1ThermSensor()

# ---------------- TURBIDITY CONFIG ----------------

CLEAR_WATER_VOLTAGE = 3.06
NTU_PER_VOLT = 70
MAX_NTU = 300

# ---------------- DO CALIBRATION ----------------

V_SAT = 2.60

# ---------------- pH CONFIG ----------------

PH_MID_VOLTAGE = 2.5
PH_SLOPE = 0.133

# ---------------- BACKEND CONFIG ----------------

API_URL = "https://neernaya-backend.vercel.app/telemetry/push"
DEVICE_ID = 1

# ---------------- GENERAL SETTINGS ----------------

WINDOW_DURATION = 60
READ_INTERVAL = 2

# ---------------- FILTER FUNCTION ----------------

def filtered_voltage(channel, samples=20, trim=2):
    readings = []

    for _ in range(samples):
        v = channel.voltage

        if v is not None and 0 <= v <= 5:
            readings.append(v)

        time.sleep(0.02)

    if len(readings) == 0:
        return 0

    median = statistics.median(readings)
    filtered = [x for x in readings if abs(x - median) < 0.3]

    if len(filtered) == 0:
        return median

    filtered.sort()

    if len(filtered) > (2 * trim):
        trimmed = filtered[trim:len(filtered) - trim]
    else:
        trimmed = filtered

    return statistics.mean(trimmed)

# ---------------- SAFE VALUE WITH ROUNDING ----------------

def safe_value(val, default=0, digits=2):
    try:
        if val is None:
            return default
        if isinstance(val, float) and (val != val):  # NaN
            return default
        return round(float(val), digits)
    except:
        return default

# ---------------- SEND TO BACKEND ----------------

def send_to_backend(temp, do, turb, tds, ec, salinity, hardness, ph):
    payload = {
        "device_id": DEVICE_ID,
        "temp": safe_value(temp, digits=2),
        "do": safe_value(do, digits=2),
        "turb": safe_value(turb, digits=2),
        "tds": safe_value(tds, digits=2),
        "ec": safe_value(ec, digits=2),
        "salinity": safe_value(salinity, digits=3),
        "hardness": safe_value(hardness, digits=2),
        "ph": safe_value(ph, digits=2)
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        print("?? Sent:", payload)

        if response.status_code in [200, 201]:
            print("? Data sent successfully")
        else:
            print("?? Failed:", response.status_code)
            print("Response:", response.text)

    except Exception as e:
        print("? Error:", e)

# ---------------- TURBIDITY ----------------

def voltage_to_ntu(voltage):
    if voltage > CLEAR_WATER_VOLTAGE:
        voltage = CLEAR_WATER_VOLTAGE
    ntu = (CLEAR_WATER_VOLTAGE - voltage) * NTU_PER_VOLT
    return max(0, min(MAX_NTU, ntu))

def classify_turbidity(ntu):
    if ntu <= 5:
        return "Too Clear"
    elif ntu <= 25:
        return "Good Pond"
    elif ntu <= 50:
        return "Ideal Pond"
    elif ntu <= 100:
        return "Muddy"
    else:
        return "Dangerous"

# ---------------- TDS ----------------

def calculate_tds(voltage, temperature):
    compensation = 1 + 0.02 * (temperature - 25)
    compensated_voltage = voltage / compensation
    tds = (
        133.42 * (compensated_voltage ** 3)
        - 255.86 * (compensated_voltage ** 2)
        + 857.39 * compensated_voltage
    ) * 0.5
    return max(0, tds)

def calculate_ec(tds):
    return tds * 2

def calculate_salinity(ec):
    return (ec / 1000) * 0.55

def calculate_hardness(tds):
    return tds * 0.5

def classify_tds(tds):
    if tds <= 150:
        return "Very Soft"
    elif tds <= 400:
        return "Ideal"
    elif tds <= 800:
        return "Acceptable"
    elif tds <= 1200:
        return "High"
    else:
        return "Dangerous"

# ---------------- DO ----------------

def oxygen_saturation(temp):
    table = {
        0: 14.6, 5: 12.8, 10: 11.3, 15: 10.1,
        20: 9.1, 25: 8.26, 30: 7.56, 35: 6.95
    }
    nearest = min(table.keys(), key=lambda x: abs(x - temp))
    return table[nearest]

def calculate_do(voltage, temp):
    do_sat = oxygen_saturation(temp)
    return max(0, (voltage / V_SAT) * do_sat)

def classify_do(do):
    if do >= 8:
        return "Excellent"
    elif do >= 6:
        return "Good"
    elif do >= 4:
        return "Acceptable"
    elif do >= 2:
        return "Low Oxygen"
    else:
        return "Dangerous"

# ---------------- pH ----------------

def calculate_ph(voltage):
    return 7 + ((PH_MID_VOLTAGE - voltage) / PH_SLOPE)

def classify_ph(ph):
    if ph < 6.5:
        return "Acidic ??"
    elif ph <= 8.5:
        return "Safe ?"
    else:
        return "Basic ??"

# ---------------- BUFFERS ----------------

temp_buffer = []
ntu_buffer = []
tds_buffer = []
do_buffer = []
ph_buffer = []

# ---------------- MAIN LOOP ----------------

while True:
    temperature = temp_sensor.get_temperature()

    ntu = voltage_to_ntu(filtered_voltage(turbidity_channel))
    tds = calculate_tds(filtered_voltage(tds_channel), temperature)
    do = calculate_do(filtered_voltage(do_channel), temperature)
    ph = calculate_ph(filtered_voltage(ph_channel))

    temp_buffer.append(temperature)
    ntu_buffer.append(ntu)
    tds_buffer.append(tds)
    do_buffer.append(do)
    ph_buffer.append(ph)

    time.sleep(READ_INTERVAL)

    if time.time() - start_time >= WINDOW_DURATION:
        avg_temp = round(mean(temp_buffer), 2)
        avg_ntu = round(mean(ntu_buffer), 2)
        avg_tds = round(mean(tds_buffer), 2)
        avg_do = round(mean(do_buffer), 2)
        avg_ph = round(mean(ph_buffer), 2)

        ec = round(calculate_ec(avg_tds), 2)
        sal = round(calculate_salinity(ec), 3)
        hard = round(calculate_hardness(avg_tds), 2)

        print("Temperature:", avg_temp, "oC")
        print("DO:", avg_do, "mg/L ?", classify_do(avg_do))
        print("Turbidity:", avg_ntu, "NTU ?", classify_turbidity(avg_ntu))
        print("TDS:", avg_tds, "ppm ?", classify_tds(avg_tds))
        print("pH:", avg_ph, "?", classify_ph(avg_ph))
        print("EC:", ec, "uS/cm")
        print("Salinity:", sal, "ppt")
        print("Hardness:", hard, "mg/L")
        print("---------------------------")

        # SEND DATA
        send_to_backend(avg_temp, avg_do, avg_ntu, avg_tds, ec, sal, hard, avg_ph)

        lcd.clear()

        lcd.cursor_pos = (0, 0)
        lcd.write_string("T:{:2.0f}oC   DO:{:1.0f}mg/L".format(avg_temp, avg_do))

        lcd.cursor_pos = (1, 0)
        lcd.write_string("Tb:{:1.0f}NTU  pH:{:.1f}".format(avg_ntu, avg_ph))

        lcd.cursor_pos = (2, 0)
        lcd.write_string("TDS:{:3.0f}ppm EC:{:3.0f}uS".format(avg_tds, ec))

        lcd.cursor_pos = (3, 0)
        lcd.write_string("Sa:{:.1f}ppt H:{:2.0f}mg/L".format(sal, hard))

        temp_buffer.clear()
        ntu_buffer.clear()
        tds_buffer.clear()
        do_buffer.clear()
        ph_buffer.clear()

        start_time = time.time()