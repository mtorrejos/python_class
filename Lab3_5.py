import RPi.GPIO as GPIO
import time


PButtonA = 16
LED1 = 18
PButtonB = 13
LED2 = 15
currentLED = None

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(PButtonA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PButtonB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(PButtonA) == GPIO.HIGH and GPIO.input(PButtonB) == GPIO.HIGH:
			continue
		elif GPIO.input(PButtonA) == GPIO.HIGH:
			GPIO.output(LED1, GPIO.HIGH)
			GPIO.output(LED2, GPIO.LOW)
			currentLED = LED1
		elif GPIO.input(PButtonB) == GPIO.HIGH:
			GPIO.output(LED2, GPIO.HIGH)
			GPIO.output(LED1, GPIO.LOW)
		else:
			GPIO.output(LED1, GPIO.LOW)
			GPIO.output(LED2, GPIO.LOW)
		time.sleep(0.5)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()

