import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(8) # Initialization
try:
  while True:
    p.ChangeDutyCycle(8)
    time.sleep(0.5)
    p.ChangeDutyCycle(8.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(9)
    time.sleep(0.5)
    p.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(10.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(11.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(12)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(13)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(12)
    time.sleep(0.5)
    p.ChangeDutyCycle(11.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(10.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(9)
    time.sleep(0.5)
    p.ChangeDutyCycle(8)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
