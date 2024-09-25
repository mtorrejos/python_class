import RPi.GPIO as GPIO
import time

PButton = 16
LED1 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(PButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(PButton) == GPIO.HIGH:
			GPIO.output(LED1, GPIO.HIGH)
			print("Hello")
		else:
			GPIO.output(LED1, GPIO.LOW)
			print("World")
		time.sleep(0.5)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
