import serial
class RFIDLib:
    def Connect(self, port):
        self.serial = serial.Serial(port, 9600, timeout = 5)
    def ReadData(self):
        data = self.serial.read(12)
        print(data.decode())
    def Close(self):
        self.serial.close()

RF = RFIDLib()
RF.Connect('COM4')
while True:
    RF.ReadData()
input()