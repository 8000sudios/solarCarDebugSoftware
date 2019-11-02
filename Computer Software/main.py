import time
import serial

#Config for Serial
baud = 9600
#port = '/dev/ttyS6'
#port = '/dev/tty.usbserial-1410'
port = input("Enter COM port: ");

#Options
rate = 4

#Serial initialization 
ser = serial.Serial(port, baud)

#Sends a command (1 byte) on serial then will wait a moment then read the serial 
def request(byte):
    ser.write(byte)
    time.sleep(0.3) #Each byte will take about 1ms to send (0.3 is about 250 bytes)
    message = ser.read(ser.in_waiting)

    #Note that is print will automatically convert hex to ascii if it can
    print(message)

def monitorCOM():
    message = ser.readline()

    print(message)


while(1):
    monitorCOM()
