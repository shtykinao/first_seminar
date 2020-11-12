import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

AnalogPin = [10, 9, 11, 5, 6, 13, 19, 26]
LEDPin = [24, 25, 8, 7, 12, 16, 20, 21]
ListV = []
ListT = []
Comparator = 4
TroykaVoltPin = 17
GPIO.setup(TroykaVoltPin,GPIO.OUT)
GPIO.output(TroykaVoltPin,0)
GPIO.setup(Comparator,GPIO.IN)
for a in AnalogPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)
for a in LEDPin:
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,0)

def num2pins(pins, Value):
    value = int(Value)
    for a in pins:
        GPIO.output(a,0)
    for i in range(7, -1, -1):
        x = 1 << i
        GPIO.output(pins[i],(x&value) >> i)

def adc():
    l = 0
    r = 255
    while r-l > 1:
        c = (r+l)//2
        num2pins(AnalogPin, c)
        time.sleep(0.01)
        if GPIO.input(Comparator)==1:
            l = c+1
        else:
            r = c
    return (r+l)//2





try:
    GPIO.output(TroykaVoltPin,1)
    Tstart = time.time()
    print("Capacitor is charging")
    Volt = adc()
    while Volt < 240:
        Volt = adc()
        ListV.append(Volt)
        ListT.append(time.time() - Tstart)
        print(Volt)
    print("Capacitor is charged")
    GPIO.output(TroykaVoltPin,0)
    while Volt > 5:
        Volt = adc()
        ListV.append(Volt)
        ListT.append(time.time() - Tstart)
        print(Volt)
    open("/home/gr006/Desktop/Scripts/Budkin & Polygalov/settings.txt","w").write("deltaV = 3.3V, dT = %.3f" % ListT[0])
    Data = open("/home/gr006/Desktop/Scripts/Budkin & Polygalov/data.txt","w")
    Data.write("1 experiment: dV = %.6fV; " % (ListV[0]/255*3.3))
    Data.write("dT = %.3f s \n" % (ListT[0]))
    for i in range(1,len(ListV)):
        dV = float(ListV[i]- ListV[i-1])/255*3.3
        dT = ListT[i]- ListT[i-1]
        Data.write(str(i+1)+" experiment: dV = %.3fV; " % dV)
        Data.write("dT = %.3f s \n" % (ListT[0]))
    plt.plot(ListT, ListV)
    plt.title('Condensator')
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.show()
    
except KeyboardInterrupt:
    print("Error KeyboardInterrupt")
except ValueError:
    print("Error ValueError")
finally:
    GPIO.output(TroykaVoltPin,0)
    GPIO.cleanup()
    print("Programm successfully closed.")
