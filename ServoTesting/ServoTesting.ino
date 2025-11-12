// This project uses 2 push-buttons to control the position of a servo

// Preprocessor
#include <Servo.h>

// Pin definitions
#define button1 2
#define button2 3
#define servoControl 6

#define speed 2

// Variables
Servo servo;

int currAngle = 0;

void setup() {
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(servoControl, OUTPUT);

  servo.attach(servoControl);
  servo.write(90);
}

void loop() {
  currAngle = servo.read();

  if(!digitalRead(button1)) {
    currAngle -= speed;
  }
  
  else if(!digitalRead(button2)) {
    currAngle += speed;
  }

  servo.write(currAngle);

  delay(10);
}
