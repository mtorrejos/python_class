import serial
import time
import RPi.GPIO as GPIO

LED = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT) 

# Open the serial port (adjust the '/dev/ttyACM0' if necessary)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


time.sleep(2) # Wait for the connection to be established

# Continuously read data from Arduino and print it
try:
	while True:
		if ser. in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			
			if(line == "on"):
				GPIO.output(LED, GPIO.HIGH) 
			else:
				GPIO.output(LED, GPIO.LOW)

except KeyboardInterrupt:
	pass
	
finally:
	GPIO.cleanup()

