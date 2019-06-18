#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

RelayPin = 11  

def setup():
	ADC.setup(0x48)
	
def setupRelay():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RelayPin, GPIO.OUT)
	GPIO.output(RelayPin, GPIO.HIGH)

def loop():
	status = 1
	while True:
                print('Value:', ADC.read(0))
                Value = ADC.read(0)
                if Value > 250:
##                if ADC.read(0) < 120:
                    print('...relayd on')
                    GPIO.output(RelayPin, GPIO.LOW)
                else:
                    print('relay off...')
                    GPIO.output(RelayPin, GPIO.HIGH)
                outvalue = map(Value,0,255,120,255)
                ADC.write(outvalue)
                time.sleep(0.2) 
		
def destroy():
	ADC.write(0)
	
def destroyRelay():
	GPIO.output(RelayPin, GPIO.HIGH)
	GPIO.cleanup()  

def map(x, in_min, in_max, out_min, out_max):
        '''To map the value from arange to another'''
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ == '__main__':
	try:
		setup()
		setupRelay()
		loop()
	except KeyboardInterrupt: 
		destroy()
		destroyRelay()
