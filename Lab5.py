import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pwmPin = 18

GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

try:
	while True:
		pwmPercent = float(input('PWM %: '))
		pwm.ChangeDutyCycle(pwmPercent)
		sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO cleared')