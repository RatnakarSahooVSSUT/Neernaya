# 🔌 Hardware Connections & GPIO Mapping (Raspberry Pi 5)

![Hardware](https://img.shields.io/badge/Focus-Hardware%20Connections-orange?style=for-the-badge)
![Raspberry Pi](https://img.shields.io/badge/Board-Raspberry%20Pi%205-red?style=for-the-badge&logo=raspberrypi)
![Sensors](https://img.shields.io/badge/Sensors-pH%20%7C%20TDS%20%7C%20DO%20%7C%20Turbidity-blue?style=for-the-badge)
![Protocol](https://img.shields.io/badge/Protocols-I2C%20%7C%20GPIO-green?style=for-the-badge)

📍 *Project: Neernaya – Smart Water Quality Monitoring System*

---

## 🧠 Controller

- 🍓 **Raspberry Pi 5**
- ⚡ Logic Level: **3.3V (Critical)**

---

## 🔗 Communication Overview

| 🔌 Interface | 📡 Usage |
|------------|--------|
| I2C | ADS1115 ADC + LCD |
| GPIO | LED + Temperature Sensor |
| Analog (via ADC) | pH, TDS, Turbidity, DO |

---

## 📡 I2C Bus Connections

### 🔹 ADS1115 (ADC)

| Pin | Connection |
|-----|-----------|
| VCC | 3.3V (Pin 1) |
| GND | GND (Pin 6) |
| SDA | GPIO2 (Pin 3) |
| SCL | GPIO3 (Pin 5) |

---

### 🔹 LCD Display (I2C - PCF8574)

| Pin | Connection |
|-----|-----------|
| VCC | 5V (Pin 2) |
| GND | GND (Pin 9) |
| SDA | GPIO2 (Pin 3) |
| SCL | GPIO3 (Pin 5) |

📌 **I2C Addresses**
- 🖥️ LCD → `0x27`  
- 📊 ADS1115 → `0x48` (default)

---

## 📊 ADC Channel Mapping (ADS1115)

| 🌊 Sensor | 📥 Channel | 💻 Code Mapping |
|----------|----------|----------------|
| 💧 Turbidity | A0 | `AnalogIn(ads, 0)` |
| 🧂 TDS | A1 | `AnalogIn(ads, 1)` |
| 🫧 Dissolved Oxygen | A2 | `AnalogIn(ads, 2)` |
| ⚗️ pH | A3 | `AnalogIn(ads, 3)` |

---

## 🔌 Sensor Wiring

### 💧 Turbidity Sensor
- 🔴 VCC → 5V  
- ⚫ GND → GND  
- 🟡 OUT → ADS1115 A0  

---

### 🧂 TDS Sensor
- 🔴 VCC → 5V  
- ⚫ GND → GND  
- 🟡 OUT → ADS1115 A1  

---

### 🫧 Dissolved Oxygen Sensor
- 🔴 VCC → 5V  
- ⚫ GND → GND  
- 🟡 OUT → ADS1115 A2  

---

### ⚗️ pH Sensor
- 🔴 VCC → 5V  
- ⚫ GND → GND  
- 🟡 OUT → ADS1115 A3  

---

## 🌡️ Temperature Sensor (DS18B20)

| Pin | Connection |
|-----|-----------|
| 🔴 VCC | 3.3V (Pin 1) |
| ⚫ GND | GND (Pin 6) |
| 🟡 DATA | GPIO4 (Pin 7) |

📌 **Important:**
- Add **4.7kΩ pull-up resistor** between DATA and VCC  

---

## 💡 LED Indicator

| Component | Connection |
|----------|-----------|
| 🔴 LED (+) | GPIO17 (Pin 11) |
| ⚫ LED (-) | GND |

📌 Use **220Ω resistor** in series  

---

## 🔔 Buzzer (Optional)

| Component | Connection |
|----------|-----------|
| 🔊 Buzzer (+) | GPIO27 (Pin 13) |
| ⚫ Buzzer (-) | GND |

---

## ⚠️ Important Notes

⚡ Raspberry Pi GPIO is **3.3V ONLY**  
🚫 Never connect 5V directly to GPIO pins  

⚡ ADS1115 handles all analog sensors safely  

⚡ Ensure **common ground** across all components  

⚡ Sensor calibration is required for accurate results  

---

## 🔄 System Flow

Sensors → ADS1115 → Raspberry Pi 5 → Python Processing → Cloud → Alerts

---

## ✅ Quick Summary

- 📡 I2C → ADS1115 + LCD  
- 🌡️ GPIO4 → DS18B20  
- 💡 GPIO17 → LED  
- 📊 ADC Channels → All analog sensors  

---

🚀 *Designed for real-time, scalable, and intelligent aquaculture monitoring systems.*
