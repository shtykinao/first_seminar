import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt

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
        while True:
            print("Insert Duration: ", end = "")
            Duration = float(input())
            if Duration < -1:
                print("Value is incorrect.")
            else:
                break
        while True:
            print("Insert Frequency of discretization: ", end = "")
            Freq = float(input())
            if Freq < 0:
                print("Value is incorrect.")
            else:
                break  
        while True:
            print("Insert Frequency of impulse: ", end = "")
            ImpulseFreq = float(input())
            if ImpulseFreq < 0:
                print("Value is incorrect.")
            else:
                break 
        print("Value is correct")
        
        tm = np.arange(0, Duration, 1/Freq)
        amplitude = 127*np.sin(ImpulseFreq*tm*2*math.pi) + 127
        for i in amplitude:
            print(ImpulseFreq)
            dec(i)
            time.sleep(1/Freq)
        plt.plot(tm, amplitude)
        plt.title('Синус')
        plt.xlabel('Время')
        plt.ylabel('Амплитуда sin(time)')
        plt.show()
except KeyboardInterrupt:
    print("Error stop 000000000")
except ValueError:
    print("Error stop 000000000")
finally:
    GPIO.cleanup()
    
    print("Programm successfully closed.")
        

        
    
    
    

