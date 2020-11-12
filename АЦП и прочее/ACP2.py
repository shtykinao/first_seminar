import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
Comparator = 4
TroykaVoltPin = 17
GPIO.setup(TroykaVoltPin,GPIO.OUT)
GPIO.output(TroykaVoltPin,1)
GPIO.setup(Comparator,GPIO.IN)
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
def FindValue():
    for value in range(256):
        dec(value)
        time.sleep(0.005)
        if GPIO.input(Comparator)==0:
            return value
    return 0

try:
    while True:
        value = FindValue()
        voltage = float(value)/255*3.3
        print("Digital value: ",value,"Analog value: %.2f V" % (voltage))
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Error KeyboardInterrupt")
except ValueError:
    print("Error ValueError")
finally:
    GPIO.cleanup()
    print("Programm successfully closed.")

        

        
    
    
    


        

        
    
    
    

