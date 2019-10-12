import serial

baud = 9600

with serial.Serial('/dev/tty.usbserial-1410', baud, timeout=3) as sr:
    print(sr.name)
    print(sr.readline())
    sr.write(b'\xFF\x04')
