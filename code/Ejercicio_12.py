# Ejercicio #12.
# Componentes utilizados: Slide Potentiometer y Servo.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.
from machine import Pin, PWM,ADC
from time import sleep

adc = ADC(Pin(28))
    
servoPin = PWM(Pin(16))
servoPin.freq(50)

def servo(degrees):
    # limit degrees beteen 0 and 180
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    # set max and min duty
    maxDuty=9000
    minDuty=1000
    # new duty is between min and max duty in proportion to its value
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    # servo PWM value is set
    servoPin.duty_u16(int(newDuty))

while True:
  value=adc.read_u16()
  print(value)
  degree=value*180/65500
  servo(degree)
  sleep(0.001)
