import serial
import time

# Open the serial port (adjust the '/dev/ttyACM0' if necessary)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

time.sleep(2) # Wait for the connection to be established

# Continuously read data from Arduino and print it
try:
	while True:
		command = input("Enter 1 to turn on LED, 0 to turn off")
		ser.write(command.encode())

except KeyboardInterrupt:
	pass
	
finally:
	GPIO.cleanup()

