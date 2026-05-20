import can
from datetime import datetime

print("Automotive CAN Bus Analyzer Started...")
print("Waiting for CAN messages...\n")

bus = can.interface.Bus(channel='vcan0', interface='socketcan')

try:
    while True:
        message = bus.recv()

        if message:
            timestamp = datetime.now().strftime('%H:%M:%S')

            print("====================================")
            print(f"Time      : {timestamp}")
            print(f"CAN ID    : {hex(message.arbitration_id)}")
            print(f"DLC       : {message.dlc}")
            print(f"Data      : {message.data.hex().upper()}")
            print("====================================\n")

except KeyboardInterrupt:
    print("CAN Analyzer Stopped")
