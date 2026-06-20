import serial
import time

print("Opening serial...")

arduino = serial.Serial('/dev/ttyACM0',9600)

time.sleep(2)

print("Sending ON")
arduino.write(b'ON\n')

time.sleep(3)

print("Sending OFF")
arduino.write(b'OFF\n')

print("Done")