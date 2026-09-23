import time
import board
import busio
import adafruit_dht
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# -------------------------
# DHT22
# -------------------------
dht = adafruit_dht.DHT22(board.D4)

# -------------------------
# ADS1115
# -------------------------
i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)
ads.gain = 1

# Turbidity sensor AOUT -> ADS1115 A0
turbidity = AnalogIn(ads, ADS.P0)

# -------------------------
# Read sensors continuously
# -------------------------
print("Hydroponics Sensor Monitoring")
print("==============================")
print("DHT22 + Turbidity Sensor")
print("Press Ctrl+C to stop")
print()

try:
    while True:

        # DHT22 reading
        try:
            temperature = dht.temperature
            humidity = dht.humidity
        except RuntimeError:
            temperature = None
            humidity = None

        # Turbidity reading
        voltage = turbidity.voltage
        adc_value = turbidity.value

        print("--------------------------------")
        
        if temperature is not None:
            print(f"Temperature : {temperature:.1f} °C")
            print(f"Humidity    : {humidity:.1f} %")
        else:
            print("DHT22       : Reading error")

        print(f"Turbidity V : {voltage:.3f} V")
        print(f"Turbidity ADC: {adc_value}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")

finally:
    dht.exit()