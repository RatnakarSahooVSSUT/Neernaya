# 🧩 Components List – Neernaya (Raspberry Pi 5)

![Hardware](https://img.shields.io/badge/Category-Hardware-orange?style=for-the-badge)
![Raspberry Pi](https://img.shields.io/badge/Controller-Raspberry%20Pi%205-red?style=for-the-badge&logo=raspberrypi)
![Sensors](https://img.shields.io/badge/Sensors-pH%20%7C%20TDS%20%7C%20DO%20%7C%20Turbidity-blue?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interfaces-I2C%20%7C%20GPIO-green?style=for-the-badge)

📍 *Project: Neernaya – Smart Water Quality Monitoring System*

---

## 🧠 Core Controller

| Component | Description |
|----------|------------|
| 🍓 Raspberry Pi 5 | Main processing unit for data acquisition, processing, and IoT communication |

---

## 📊 Sensors Used

| Sensor | Type | Purpose |
|-------|------|--------|
| 🌡️ DS18B20 Temperature Sensor | Digital | Measures water temperature |
| ⚗️ pH Sensor Module | Analog | Determines acidity/basicity of water |
| 💧 Turbidity Sensor | Analog | Measures water clarity (NTU) |
| 🫧 Dissolved Oxygen (DO) Sensor | Analog | Measures oxygen level in water |
| 🧂 TDS Sensor | Analog | Measures total dissolved solids |

---

## 🔌 Data Acquisition

| Component | Description |
|----------|------------|
| 📟 ADS1115 (16-bit ADC) | Converts analog sensor signals to digital (I2C interface) |

---

## 📺 Display & Output

| Component | Description |
|----------|------------|
| 🖥️ 20x4 I2C LCD (PCF8574) | Displays real-time sensor readings |
| 💡 LED Indicator | Status indication (system active/alerts) |
| 🔔 Buzzer (Optional) | Audio alert for critical conditions |

---

## 🔗 Supporting Components

| Component | Purpose |
|----------|--------|
| 🔌 Breadboard | Prototyping and circuit connections |
| 🔗 Jumper Wires | Electrical connections |
| 🔋 Power Supply (5V) | Powers Raspberry Pi and sensors |
| ⚡ Resistors (220Ω, 4.7kΩ) | LED protection & pull-up resistor for DS18B20 |

---

## 🌐 Communication & Interface

| Module | Role |
|-------|------|
| 📡 Wi-Fi (Built-in Pi) | Sends data to cloud/dashboard |
| 🔗 I2C Protocol | Communication with ADS1115 & LCD |
| ⚙️ GPIO | LED & temperature sensor interfacing |

---

## 🧪 Software Dependencies (Hardware Interaction)

| Library | Purpose |
|--------|--------|
| 🐍 RPi.GPIO | GPIO control |
| 📡 busio / board | I2C communication |
| 📊 adafruit_ads1x15 | ADC interfacing |
| 🌡️ w1thermsensor | Temperature sensor |
| 🖥️ RPLCD | LCD display control |

---

## 📦 Summary

- 🍓 Raspberry Pi 5 as central controller  
- 📊 ADS1115 for analog sensor interfacing  
- 🌊 5 Water quality sensors integrated  
- 📡 I2C + GPIO based communication  
- 🔔 Real-time alerts and display system  

---

🚀 *This component selection ensures high accuracy, scalability, and real-time monitoring capability for smart aquaculture systems.*
