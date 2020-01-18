import time
import serial
import requests
import json

#Config for Serial
baud = 9600
port = '/dev/ttyS6'
#port = '/dev/tty.usbserial-1410'
#port = input("Enter COM port: ");

url = 'http://ec2-54-174-125-98.compute-1.amazonaws.com/'
url = 'http://localhost:3000'

#Serial initialization 
#ser = serial.Serial(port, baud)

def monitorCOM():
    message = ser.readline()

    #sendTel(message)
    print(message)

def sendTel(msg):
    msgSend = {"timestamp": msg[0:4], "id": int(msg[4:8], 16), "data": [ int(msg[8:10], 16), int(msg[10:12], 16), int(msg[12:14], 16), int(msg[14:16], 16), int(msg[16:18], 16), int(msg[18:20], 16), int(msg[20:22], 16), int(msg[22:24], 16) ]}
    r = requests.post(url, json=msgSend)
    print(r.status_code);

while(1):
#    monitorCOM()
    sendTel("000006230000005C2015211800006")
    time.sleep(5) 

sendTel("00000622000000014C81000000007")