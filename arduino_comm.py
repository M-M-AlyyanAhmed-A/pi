import smbus

class ArduinoComm:
    def __init__(self, address):
        self.address = address
        self.bus = smbus.SMBus(1)

    def send_command(self, command):
        try:
            self.bus.write_byte(self.address, command)
            print(f"Command {command} sent to Arduino.")
        except Exception as e:
            print(f"Failed to send command: {e}")
