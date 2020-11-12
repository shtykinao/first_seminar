import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
for a in AnalogPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)

def dec(value):
    for a in AnalogPin:
        GPIO.output(a,0)
    for i in range(7, -1, -1):
        x = 1 << i
        GPIO.output(AnalogPin[i],(x&value) >> i)
try:
    while True:
        while True:
            print("Insert repeationsNumber: ", end = "")
            repeationsNumber = int(input())
            if repeationsNumber < -1:
                print("Value is incorrect.")
            else:
                break
        if repeationsNumber == -1:
            break  
        print("Value is correct")
        for n in range(repeationsNumber):
            for i in range(256):
                dec(i)
                time.sleep(0.01)
            for i in range(255,-1,-1):
                dec(i)
                time.sleep(0.01)
except KeyboardInterrupt:
    print("Error stop 000000000")
except ValueError:
    print("Error stop 000000000")
finally:
    GPIO.cleanup()
    
    print("Programm successfully closed.")
        

        
    
    
    

