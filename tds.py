import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ADS1115 setup
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1

# TDS signal connected to ADS1115 A2
tds = AnalogIn(ads, 2)

while True:
    voltage = tds.voltage

    # Temperature compensation
    temperature = 25.0
    compensation = 1.0 + 0.02 * (temperature - 25.0)
    compensated_voltage = voltage / compensation

    # TDS calculation
    tds_value = (
        133.42 * compensated_voltage**3
        - 255.86 * compensated_voltage**2
        + 857.39 * compensated_voltage
    ) * 0.5

    if tds_value < 0:
        tds_value = 0

    print("--------------------------------")
    print("TDS Voltage : {:.3f} V".format(voltage))
    print("ADC Value   : {}".format(tds.value))
    print("TDS         : {:.1f} ppm".format(tds_value))
    print("--------------------------------")

    time.sleep(2)