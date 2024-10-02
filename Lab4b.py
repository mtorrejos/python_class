import serial
import time
import RPi.GPIO as GPIO

# Open the serial port (adjust the '/dev/ttyACM0' if necessary)
ser = serial.Serial('/dev/serial0', 9600, timeout=5)
time.sleep(2) # Wait for the connection to be established
# Continuously read data from Arduino and print it
try:
	while True:
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line)

except KeyboardInterrupt:
	pass

#finally:
	#ser.close()
	#GPIO.cleanup()



