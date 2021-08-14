from pyi2c import I2CDevice

bus_n = 0
addr = 0x38
aht10 = I2CDevice(bus_n, addr)

print( aht10.read() )
