# micropython code for connecting servo motor and sensor to pyboard.

import pyb
import machine
from time import sleep
from pyb import Pin, ADC, DAC, UART
from pyb import Servo

float read_value
#Initializing servo pins on pyboard:
servo1 = pyb.Servo(1)
 
 #to change the angle of servo motor:
 
servo1.angle(45)
sleep(0.5) # providing delay
servo1.angle(-90)
 
 #or we can provide delay and angle in single line as shown below.
servo1.angle(50, 1000) # it take 1 m.sec to reach its angle from current degree.
 
 # for continuous rotation servo motors.
 #its need pulse width and direction like clockwise or counterclockwise
 #The direction and speed of rotation is set by the pulse width on the signal wire
servo1.speed(50) 
uart.write('Servo motor is rotating...') # print on UART port
 
 # or we can give min, max center pulse width to servo motor:
 
servo1.calibration(80,1400,1000,1500,1200)
 
 #Connect any sensor to pybaord.
 #Example:  connect mq2 gas sensor to pyboard. mq2 sensor siganl pin connected to y11 pin.
 #and ground to gnd of pybaord.
 
adc1=pyb.ADC(pyb.Pin.board.Y12)
read_value = adc1.read() #print the sensor values 
print(read_value)
if(read_value > 200):
   print("warning! --- Threshold exceeded. ")
else:
  print("Smoke detected..")
     
