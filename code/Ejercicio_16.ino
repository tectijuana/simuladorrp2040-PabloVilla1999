/*
# Ejercicio #16.
# Componentes utilizados: LCD20x04.
# Alumno: Jesus Pablo Ramirez Villa. 
# Materia: Sistemas Programables.
# Docente: Rene Solis Reyes.*/
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  Wire.setSDA(8);
  Wire.setSCL(9);
  Wire.begin();

  lcd.init();
  lcd.backlight();
  lcd.begin(0,2);
  lcd.print("Hello World!");

  lcd.setCursor(2, 1);
  lcd.print("> Pi Pico <");
}

void loop() {
  delay(1); // Adding a delay() here speeds up the simulation
}
