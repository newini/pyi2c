#!/bin/env python3
# -*- coding: utf-8 -*-
# tests/i2c.py
"""
Test for I2C
"""

import time
from pyi2c import I2C

i2c = I2C(0)

# Scan
print( i2c.scan() )

# Use AHT10
AHT10_ADDR = 0x38

# Init
i2c.write(AHT10_ADDR, 0xe1)
time.sleep(1)

# loop
while True:
    # Trigger
    i2c.write(AHT10_ADDR, [0xac, 0x33, 0x00])
    time.sleep(.1)

    # Get 6 bytes of data
    read_data = i2c.read(AHT10_ADDR, 6)

    # Fill data
    humidity_data = (read_data[1] << 12) + (read_data[2] << 4) + (read_data[3] & 0xf0)
    temperature_data = ((read_data[3] & 0x0f) << 16) + (read_data[4] << 8) + read_data[5]

    # Convert
    humidity = humidity_data/(2**20)*100 # in %
    temperature = temperature_data/(2**20)*200 - 50 # in C

    print('{0:.2f} %, {1:.2f} C'.format(humidity, temperature))

    if temperature > 85:
        # Reset
        i2c.write(AHT10_ADDR, 0xba)

    time.sleep(.9)
