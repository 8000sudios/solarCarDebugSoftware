import time
import serial

#Config for Serial
baud = 9600
port = '/dev/ttyS6'

#Config
rate = 4

#Serial initialization 
ser = serial.Serial(port, baud)

#So like when you establish a connection to and arduino via Serial,
#it does a soft reset and will re-run the bootloader -.-
#We need to wait for the bootloader to run the code
time.sleep(2)

#Sends a command (1 byte) on serial then will wait a moment then read the serial 
def request(byte):
    ser.write(byte)
    time.sleep(0.3) #Each byte will take about 1ms to send (0.3 is about 250 bytes)
    #print(ser.in_waiting)
    message = ser.read(ser.in_waiting)

    #Ok so this print so whatever reason will convert the bytes into ascii but only the ones it can
    #So the print result is a mix of raw hex and ascii
    print(message)

request(b'\x00')
