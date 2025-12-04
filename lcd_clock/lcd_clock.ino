// program for displaying current time on LCD
// time is gotten from Serial Console in Unix Time format w/ leading 'T' character

// TODO:
// check time examples for grabbing time from serial

#include <LiquidCrystal.h>
#include <TimeLib.h>

#define TIME_HEADER "T"

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

int backlight = 6;
int buzzerPin = 3;
int buttonPin = 2;
int oldHour;

int beats = 1000;

bool nightMode = false;

unsigned long currTime;

void setup() {
  Serial.begin(9600);

  pinMode(backlight, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  lcd.begin(16, 2);
  lcd.clear();
  digitalWrite(backlight, HIGH);

  setTime(currTime);
}

void loop() {
  if (Serial.available()) {
    currTime = processSyncMessage();
    setTime(currTime - 25200);
  }

  if (digitalRead(buttonPin) == LOW) {
    nightMode = !nightMode;
    if (nightMode) {
      digitalWrite(backlight, LOW);
    } else {
      digitalWrite(backlight, HIGH);
    }

    while (digitalRead(buttonPin) == LOW) {
      delay(50);
    }
  }

  int years = year();
  int months = month();
  int days = day();
  int hours = hour();
  int minutes = minute();
  int seconds = second();

  if (oldHour != hours && !nightMode) {
    chime(hours);
    oldHour = hours;
    return;
  }

  String monthText = "";

  switch (months) {
    case 1:
      monthText = "Jan";
      break;
    case 2:
      monthText = "Feb";
      break;
    case 3:
      monthText = "Mar";
      break;
    case 4:
      monthText = "Apr";
      break;
    case 5:
      monthText = "May";
      break;
    case 6:
      monthText = "Jun";
      break;
    case 7:
      monthText = "Jul";
      break;
    case 8:
      monthText = "Aug";
      break;
    case 9:
      monthText = "Sep";
      break;
    case 10:
      monthText = "Oct";
      break;
    case 11:
      monthText = "Nov";
      break;
    case 12:
      monthText = "Dec";
      break;
  }

  lcd.clear();
  lcd.setCursor(4, 0);

  if (hours < 10) {
    lcd.print("0");
  }

  lcd.print(hours);
  lcd.print(":");

  if (minutes < 10) {
    lcd.print("0");
  }

  lcd.print(minutes);
  lcd.print(":");

  if (seconds < 10) {
    lcd.print("0");
  }

  lcd.print(seconds);

  lcd.setCursor(2, 1);

  if (days < 10) {
    lcd.print("0");
  }
  lcd.print(days);
  lcd.print(" ");
  lcd.print(monthText);
  lcd.print(", ");
  lcd.print(years);

  oldHour = hours;

  delay(1000);
}

void chime(int hours) {
  lcd.clear();
  lcd.setCursor(0, 0);

  switch (hours) {
    case 0:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("midnight!");
      break;
    case 1:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("one am!");
      break;
    case 2:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("two am!");
      break;
    case 3:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("three am!");
      break;
    case 4:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("four am!");
      break;
    case 5:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("five am!");
      break;
    case 6:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("six am!");
      break;
    case 7:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("seven am!");
      break;
    case 8:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("eight am!");
      break;
    case 9:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("nine am!");
      break;
    case 10:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("ten am!");
      break;
    case 11:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("eleven am!");
      break;
    case 12:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("noon!");
      break;
    case 13:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("one pm!");
      break;
    case 14:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("two pm!");
      break;
    case 15:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("three pm!");
      break;
    case 16:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("four pm!");
      break;
    case 17:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("five pm!");
      break;
    case 18:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("six pm!");
      break;
    case 19:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("seven pm!");
      break;
    case 20:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("eight pm!");
      break;
    case 21:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("nine pm!");
      break;
    case 22:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("ten pm!");
      break;
    case 23:
      lcd.print("It is now");
      lcd.setCursor(0, 1);
      lcd.print("eleven pm!");
      break;
  }

  tone(buzzerPin, 494, beats);
  delay(beats);
  tone(buzzerPin, 392, beats);
  delay(beats);
  tone(buzzerPin, 440, beats);
  delay(beats);
  tone(buzzerPin, 294, beats);
  delay(beats);
  tone(buzzerPin, 0, beats);
  delay(beats);
  tone(buzzerPin, 294, beats);
  delay(beats);
  tone(buzzerPin, 440, beats);
  delay(beats);
  tone(buzzerPin, 494, beats);
  delay(beats);
  tone(buzzerPin, 392, beats);
  delay(beats);
}

unsigned long processSyncMessage() {
  unsigned long pctime;

  if (Serial.find(TIME_HEADER)) {
    pctime = Serial.parseInt();
  }

  return pctime;
}