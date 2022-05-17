# Ejercicio #2.
# Componentes utilizados: DHT22.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.
from machine import Pin
from DHT20 import DHT20
from time import sleep

dht_sensor=DHT20(Pin(15))

while True:

    T, H = dht_sensor.read()

    if T is None:
        print("Error en el sensor!")
    else:
        print("{}'C  {}%".format(T,H))

    sleep(1)
