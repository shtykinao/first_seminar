import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
for a in AnalogPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)

def dec(Value):
    value = int(Value)
    for a in AnalogPin:
        GPIO.output(a,0)
    for i in range(7, -1, -1):
        x = 1 << i
        GPIO.output(AnalogPin[i],(x&value) >> i)

try:
    while True:
        print("Enter value (-1 to exit):", end=" ")
        value = int(input())
        if value == -1:
            break
        elif (value < 0)or(value > 255):
            
            print("Value is incorrect.")
            continue
        else:
            voltage = float(value)/255*3.3
            print(value," = %.2fV" % (voltage))
            dec(value)
except KeyboardInterrupt:
    print("Error KeyboardInterrupt")
except ValueError:
    print("Error ValueError")
finally:
    GPIO.cleanup()
    print("Programm successfully closed.")

        

        
    
    
    

