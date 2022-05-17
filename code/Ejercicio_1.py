# Ejercicio #1.
# Componentes utilizados: Led, Resistor, PushButton.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.

import time 
import board 
import digitalio

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
  print(button.value)
  time.sleep(0.5)
