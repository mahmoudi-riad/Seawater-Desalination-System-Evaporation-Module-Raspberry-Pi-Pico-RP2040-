import machine  # For hardware interaction
import utime    # For delays and time functions

# Pin configuration
TEMP_SENSOR_PIN = 0   # LM35 sensor (ADC)
RELAY_PIN = 14        # Relay (digital output)

# Initialize components
temp_sensor = machine.ADC(TEMP_SENSOR_PIN)
relay = machine.Pin(RELAY_PIN, machine.Pin.OUT)

def read_temperature():
    """Read and convert LM35 temperature to °C."""
    adc_value = temp_sensor.read_u16()
    temperature = ((adc_value * 3.3) / 65536) * 100
    return temperature

def control_relay():
    """Control relay based on temperature."""
    temperature = read_temperature()
    print("Current temperature:", temperature)

    if temperature <= 75:   # Activate relay
        relay.value(1)
        print("Relay ON")
    elif temperature > 85:  # Deactivate relay
        relay.value(0)
        print("Relay OFF")

# Main loop
while True:
    control_relay()
    utime.sleep(5)  # Delay between checks
