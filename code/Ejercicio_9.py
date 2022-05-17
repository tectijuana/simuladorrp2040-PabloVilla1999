# Ejercicio #9.
# Componentes utilizados: Potentiometer.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.
import time
import board
import analogio

potentiometer = analogio.AnalogIn(board.GP26)

while True:
    print(potentiometer.value)
    time.sleep(2)
