# 🌊 Neernaya: Smart Water Quality Monitoring System (Raspberry Pi 5)

![IoT](https://img.shields.io/badge/Domain-IoT-blue?style=for-the-badge)
![Embedded Systems](https://img.shields.io/badge/Field-Embedded%20Systems-green?style=for-the-badge)
![Raspberry Pi](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-red?style=for-the-badge&logo=raspberrypi)
![Python](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)
![Sensors](https://img.shields.io/badge/Focus-Sensors%20%26%20Data-orange?style=for-the-badge)

🚀 *IoT-Based Aquaculture Monitoring for Sustainable Fish Farming*

---

## 📌 Overview

**Neernaya** is an advanced **IoT-based Water Quality Monitoring System** built using the **Raspberry Pi 5**, designed for aquaculture environments. It continuously monitors essential water quality parameters and provides real-time insights to maintain optimal conditions for aquatic life.

The system integrates multiple sensors with cloud connectivity to enable **smart, automated, and remote monitoring**, reducing manual effort and improving efficiency.

---

## 🎯 Key Features

✅ Real-time monitoring of water parameters  
✅ Raspberry Pi 5 based processing and control  
✅ Remote data access via IoT dashboard  
✅ Smart alert system (LED / Buzzer / Notifications)  
✅ Scalable and modular design  
✅ Suitable for ponds, tanks, and aquaculture farms  

---

## 📊 Parameters Monitored

| Parameter | Importance |
|----------|-----------|
| 🌡️ Temperature | Controls metabolism and oxygen solubility |
| ⚗️ pH Level | Maintains chemical balance of water |
| 💧 Turbidity | Indicates impurities and clarity |
| 🫧 Dissolved Oxygen | Critical for aquatic life survival |
| 🧂 TDS (Total Dissolved Solids) | Measures dissolved salts and water quality |

---

## 🧠 System Architecture

Sensors → Signal Conditioning → ADC (if required) → Raspberry Pi 5
↓
Data Processing (Python)
↓
Cloud / Dashboard (IoT)
↓
Alerts (LED / Buzzer)

---

## 🔧 Hardware Components

- 🍓 Raspberry Pi 5 (Main Controller)  
- 🌡️ Temperature Sensor (DS18B20 / LM35)  
- ⚗️ pH Sensor Module  
- 💧 Turbidity Sensor  
- 🫧 Dissolved Oxygen Sensor  
- 🧂 TDS Sensor  
- 📟 ADC Module (e.g., ADS1115 – for analog sensors)  
- 🔔 Buzzer & LED Indicators  
- 🔌 Power Supply (5V regulated)  
- 🧪 Signal Conditioning Circuits (Op-Amps, Filters if needed)  

---

## 💻 Software & Technologies

- 🐍 Python (Main Programming Language)  
- 📡 Raspberry Pi OS  
- 🌐 IoT Platforms:
  - ThingSpeak  
  - Firebase  
  - Custom Web Dashboard  
- 📊 Data Visualization Tools  
- 🔗 Communication Protocols:
  - I2C (ADC interface)  
  - GPIO (Digital I/O)  
  - Wi-Fi (HTTP / MQTT)  

---

## ⚙️ Working Principle

1. Sensors continuously measure water parameters  
2. Analog sensor outputs are converted using ADC (ADS1115)  
3. Raspberry Pi 5 reads sensor data via GPIO/I2C  
4. Python scripts process and calibrate data  
5. Data is uploaded to cloud/dashboard via Wi-Fi  
6. Threshold conditions trigger alerts (LED/Buzzer/Notification)  

---

## 🔔 Alert System

| Condition | Action |
|----------|--------|
| ✅ Safe | No alert |
| ⚠️ Moderate | LED indication |
| 🚨 Critical | Buzzer + Notification |

---

## 📈 Applications

- 🐟 Smart Fish Farming  
- 🏞️ Aquaculture Monitoring Systems  
- 🧪 Environmental & Water Research  
- 🌍 Smart Agriculture & Sustainability Projects  

---

## 🌟 Future Enhancements

- 📱 Mobile App Integration  
- 🤖 AI-based Water Quality Prediction  
- ☁️ Advanced Cloud Analytics  
- 🔋 Solar-powered System  
- 📡 GSM / SMS Alert Integration  

---

## 🚀 Getting Started

### 🔌 Hardware Setup

- Connect sensors to Raspberry Pi GPIO / ADC (ADS1115)  
- Ensure proper voltage levels (3.3V logic for Pi)  
- Calibrate pH, TDS, and DO sensors  
- Verify power supply stability  

---

## 🧪 Sensor Interfacing Summary

| Sensor | Type | Interface |
|-------|------|----------|
| Temperature | Digital/Analog | GPIO / ADC |
| pH Sensor | Analog | ADC (ADS1115) |
| Turbidity | Analog | ADC |
| DO Sensor | Analog | ADC |
| TDS Sensor | Analog | ADC |

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork this repository and submit pull requests.

---

## 📜 License

MIT License © 2026 Ratnakar Sahoo

---

## 👨‍💻 Author

**Ratnakar Sahoo**  
B.Tech | Embedded Systems | IoT | FPGA  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
