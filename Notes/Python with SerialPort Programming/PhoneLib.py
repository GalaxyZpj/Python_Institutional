import serial
import time
class PhoneLib:
    def Connect(self, port):
        self.serial = serial.Serial(port, 9600, timeout = 5)
    def PhoneDial(self, mobilenumber):
        self.serial.write("AT\r".encode())
        time.sleep(2)
        cmd = f"ATD{mobilenumber};\r"
        self.serial.write(cmd.encode())
        time.sleep(3)
    def SendSms(self, mobilenumber, message):
        self.serial.write("AT\r".encode())
        time.sleep(2)
        self.serial.write("AT+CMGF=1\r".encode())
        time.sleep(2)
        cmd = f"AT+CMGS=\"{mobilenumber}\"\r"
        self.serial.write(cmd.encode())
        time.sleep(4)
        cmd = f"{message}{chr(26)}\r"
        self.serial.write(cmd.encode())
        time.sleep(2)
    def SetReadSettings(self):
        self.serial.write("AT\r".encode())
        time.sleep(2)
        self.serial.write("AT+CMGF=1\r".encode())
        time.sleep(2)
        self.serial.write("AT\r".encode())
        time.sleep(2)
        self.serial.write("AT+CNMI=1,2,0,0,0\r".encode())
        time.sleep(2)
    def ReadMessage(self):
        data = self.serial.readline()
        time.sleep(0.5)
        if data.deode() == '+CMT':
            l = data.decode().split("\"")
        print(l)
        msg = self.serial.readline()
        time.sleep(0.5)
        print(msg.decode())
        return l[1], msg.decode()
    def Close(self):
        self.serial.close()

PH = PhoneLib()
PH.Connect('COM4')
#PH.PhoneDial("9301123085")
#PH.SendSms("9301123085", 'Hi')
PH.SetReadSettings()
while True:
    T = PH.ReadMessage()
input()
