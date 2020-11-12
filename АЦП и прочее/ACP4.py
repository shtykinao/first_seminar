import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
LEDPin = [24, 25, 8, 7, 12, 16, 20, 21]
Comparator = 4
TroykaVoltPin = 17
GPIO.setup(TroykaVoltPin,GPIO.OUT)
GPIO.output(TroykaVoltPin,1)
GPIO.setup(Comparator,GPIO.IN)
for a in AnalogPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)
for a in LEDPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)

def dec(Value,Pins):
    value = int(Value)
    for a in Pins:
        GPIO.output(a,0)
    for i in range(7, -1, -1):
        x = 1 << i
        GPIO.output(Pins[i],(x&value) >> i)
def FindValue():
    l = 0
    r = 255
    dec(r, AnalogPin)
    while r-l > 1:
        c = (r+l)//2
        dec(c, AnalogPin)
        time.sleep(0.01)
        if GPIO.input(Comparator)==1:
            l = c+1
        else:
            r = c
    return (r+l)//2

try:
    while True:
        value = FindValue()
        voltage = float(value)/255*3.3
        print("Digital value: ",value,"Analog value: %.2f V" % (voltage))
        proc = value/255*8
        for a in LEDPin:
            GPIO.output(a,0)
        for a in range(0,int(proc)+1):
            GPIO.output(LEDPin[a],1)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Error KeyboardInterrupt")
except ValueError:
    print("Error ValueError")
finally:
    GPIO.cleanup()
    print("Programm successfully closed.")

        

        
    
    
    


        

        
    
    
    

