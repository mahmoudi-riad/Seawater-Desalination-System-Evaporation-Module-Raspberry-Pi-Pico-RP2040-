# 🌡️ LM35 Temperature-Controlled Evaporation System

This project uses an LM35 temperature sensor with a Raspberry Pi Pico (MicroPython) to control a relay for heating water.  
Originally, the system was meant to include a **pressure-based evaporation method**, allowing water to evaporate at **80 °C** by controlling both temperature and pressure.  
Due to limitations, the current version only controls temperature.

## 🔧 Hardware
- Raspberry Pi Pico (or compatible board)
- LM35 temperature sensor
- Relay module
- Heating element (e.g., immersion heater)
- (Planned) Pressure sensor / vacuum pump system
- Jumper wires

## ⚡ How It Works
1. The LM35 continuously measures the water temperature.
2. If the temperature is below 80 °C, the relay activates the heater.
3. When the temperature reaches 80 °C, the relay turns the heater off.
4. (Planned) The pressure sensor would work with a pump to adjust boiling point for evaporation at lower temperatures.
5. This cycle repeats to keep the temperature stable.

## 💻 Usage
1. Upload `main.py` to your board.
2. Connect the hardware as described in the code.
3. Adjust the temperature threshold in the code if necessary.
4. Start the system and monitor the process.

## 📜 License
MIT License
