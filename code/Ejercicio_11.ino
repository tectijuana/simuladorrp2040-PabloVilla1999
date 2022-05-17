/*
# Ejercicio #11.
# Componentes utilizados: LCD16x02 I2C y Resistor.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.*/
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

void setup() {
  lcd.begin(16, 2);
  lcd.print("Hello World!");

  lcd.setCursor(2, 1);
  lcd.print("> Pi Pico <");
}

void loop() {
  delay(1); // Adding a delay() here speeds up the simulation
}
