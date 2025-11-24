#include <LiquidCrystal.h>

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

void setup() {
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Memory is empty");
  lcd.setCursor(0, 1);
  lcd.print("Load program");
}

void loop() {
}