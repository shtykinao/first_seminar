import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
for a in AnalogPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)
try:
    while True:
        while True:
            print("Insert value: ", end = "")
            value = int(input())
            if (value < -1)or(value > 255):
                print("Value is incorrect.")
            else:
                break
        if value == -1:
            break  
        print("Value is correct")
        for a in AnalogPin:
            GPIO.output(a,0)
        for i in range(7, -1, -1):
            x = 1 << i
            GPIO.output(AnalogPin[i],(x&value) >> i)
except KeyboardInterrupt:
    print("Error stop 000000000")
except ValueError:
    print("Error stop 000000000")
finally:
    GPIO.cleanup()
    
    print("Programm successfully closed.")
        

        
    
    
    

