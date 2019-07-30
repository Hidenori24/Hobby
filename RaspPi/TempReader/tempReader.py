import time
import RPi.GPIO as GPIO

TempData_PIN = 13
LED_Blink_PIN = 26

GPIO.setmode( GPIO.BCM )
GPIO.setup( TempData_PIN, GPIO.IN )
GPIO.setup( LED_Blink_PIN, GPIO.OUT )

while ( True ):
		nowData = GPIO.input( TempData_PIN )
		print( nowData )
		time.sleep(5)
