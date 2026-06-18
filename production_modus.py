from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import threading
import time

store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [25]*10) #set memblock to 10 values, set initial to 25
)
context = ModbusServerContext(slaves=store, single=True) #setup sgl modbus device using store settings

def monitor():
    while True:
        value = context[0].getValues(3, 0, count=1)[0] #read hr, start from 0, once
        print(f"Temperature: {value}")

        if value > 100:
            print("WARNING!! OVERHEATING!") #for counterscript to see changes in rl

        time.sleep(2)

threading.Thread(target=monitor, daemon=True).start() #keep monitor action in the bkg

StartTcpServer(context, address=("0.0.0.0", 5020)) #listen on all networks
