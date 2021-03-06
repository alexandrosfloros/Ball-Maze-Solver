 // Include the AccelStepper library:
#include <AccelStepper.h>

// Define stepper motor connections and steps per revolution:
#define dirPin_1 2
#define stepPin_1 3
#define dirPin_2 5
#define stepPin_2 6
#define led 4
#define motorInterfaceType 1
int angle;
String inByte;

// Create a new instance of the AccelStepper class:
AccelStepper stepper_1 = AccelStepper(motorInterfaceType, stepPin_1, dirPin_1);
AccelStepper stepper_2 = AccelStepper(motorInterfaceType, stepPin_2, dirPin_2);

void setup() {
  // Set the maximum speed in steps per second:
  stepper_1.setMaxSpeed(500);
  stepper_2.setMaxSpeed(500);

  Serial.begin(115200);
  // Set the current position to 0:
  stepper_1.setCurrentPosition(0);
  stepper_2.setCurrentPosition(0);
}

void loop() {



if(Serial.available()) { 
    //inByte = Serial.readStringUntil('\n'); //receive the signals from python files
    char command = Serial.read();
    
    switch (command){
    case 'a' :
      // clockwise rotate 36 degrees
      while(stepper_1.currentPosition() != 20)
      {
      stepper_1.setSpeed(70);
      stepper_1.runSpeed();
      }
      Serial.println(36);
      Serial.println(stepper_1.currentPosition());
      break;

    case 'b' :
      // return to 0 degree
      // detect the motor current position
      if (stepper_1.currentPosition() == 20){
        while(stepper_1.currentPosition() != 0)
        {
        stepper_1.setSpeed(-70);
        stepper_1.runSpeed();
        }
        Serial.println(0);
        Serial.println(stepper_1.currentPosition());
      }
      else if (stepper_1.currentPosition() == -20){
        while(stepper_1.currentPosition() != 0)
        {
        stepper_1.setSpeed(70);
        stepper_1.runSpeed();
        
        }
        Serial.println(0);
        Serial.println(stepper_1.currentPosition());
      }
      else {}
      break;

    case 'c' :
      // anti-clockwise rotate 36 degrees
      while(stepper_1.currentPosition() != -20)
      {
      stepper_1.setSpeed(-70);
      stepper_1.runSpeed();
      
      }
      Serial.println(-36);
      Serial.println(stepper_1.currentPosition());
      break;

    case 'd' :
      // clockwise rotate 36 degrees
      while(stepper_2.currentPosition() != 20)
      {
      stepper_2.setSpeed(70);
      stepper_2.runSpeed();
      
      }
      Serial.println(36);
      Serial.println(stepper_2.currentPosition());
      break;

    case 'e' :
      // return to 0 degree
      // detect the motor current position
      if (stepper_2.currentPosition() == 20){
        while(stepper_2.currentPosition() != 0)
        {
        stepper_2.setSpeed(-70);
        stepper_2.runSpeed();
        
        }
        Serial.println(0);
        Serial.println(stepper_2.currentPosition());
      }
      else if (stepper_2.currentPosition() == -20){
        while(stepper_2.currentPosition() != 0)
        {
        stepper_2.setSpeed(70);
        stepper_2.runSpeed();
        
        }
        Serial.println(0);
        Serial.println(stepper_2.currentPosition());
      }
      else {}
      break;

    case 'f' :
      // anti-clockwise rotate 36 degrees
      while(stepper_2.currentPosition() != -20)
      {
      stepper_2.setSpeed(-70);
      stepper_2.runSpeed();
      
      }
      Serial.println(-36);
      Serial.println(stepper_2.currentPosition());
      break;
    case 'g' :
    digitalWrite(led, true);
    delay(100);
    digitalWrite(led, false);
    break;
    Serial.flush();
    // already tried several values for the delay function
    delay(5);
    }
}
}

  
