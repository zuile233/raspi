import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
    global address 
    address = Addr

def read(chn): #channel
    if chn == 0:
        bus.write_byte(address,0x40)
    if chn == 1:
        bus.write_byte(address,0x41)
    if chn == 2:
        bus.write_byte(address,0x42)
    if chn == 3:
        bus.write_byte(address,0x43)
    bus.read_byte(address) # dummy read to start conversion
    return bus.read_byte(address)

def write(val):
    temp = val # move string value to temp 
    temp = int(temp) # change string to integer 
    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp)
