# Ejercicio #8.
# Componentes utilizados: Led RGB y Resistor.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.
import time
import board
import digitalio

red_led = digitalio.DigitalInOut(board.GP11)
red_led.direction = digitalio.Direction.OUTPUT
yellow_led = digitalio.DigitalInOut(board.GP14)
yellow_led.direction = digitalio.Direction.OUTPUT
green_led = digitalio.DigitalInOut(board.GP13)
green_led.direction = digitalio.Direction.OUTPUT

while True:
    red_led.value = True
    time.sleep(5)
    yellow_led.value = True
    time.sleep(2)
    red_led.value = False
    yellow_led.value = False
    green_led.value = True
    time.sleep(5)
    green_led.value = False
    yellow_led.value = True
    time.sleep(3)
    yellow_led.value = False
