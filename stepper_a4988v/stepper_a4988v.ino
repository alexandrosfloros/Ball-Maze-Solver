 // Include the AccelStepper library:
#include <AccelStepper.h>
// =============================================
// packages used for implementing accelerometer 
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif
MPU6050 mpu;
//===============================================
// Define stepper motor connections and steps per revolution:
#define dirPin_1 2
#define stepPin_1 3
#define dirPin_2 5
#define stepPin_2 6
#define led 4
#define motorInterfaceType 1
VectorFloat gravity;    // [x, y, z]            gravity vector
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
bool dmpReady = false;  // set true if DMP init was successful
int angle;
Quaternion q;   // [w, x, y, z]  quaternion container
float ypr[3]; // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
//===============================================

// Create a new instance of the AccelStepper class:
AccelStepper stepper_1 = AccelStepper(motorInterfaceType, stepPin_1, dirPin_1);
AccelStepper stepper_2 = AccelStepper(motorInterfaceType, stepPin_2, dirPin_2);

void setup() {
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        Wire.setClock(400000); // 400kHz I2C clock.
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
  #endif
  

  Serial.begin(115200);
  while (!Serial);
  mpu.initialize();
  mpu.dmpInitialize();
  // supply your own gyro offsets here, scaled for min sensitivity
  mpu.setXGyroOffset(220);
  mpu.setYGyroOffset(76);
  mpu.setZGyroOffset(-85);
  mpu.setZAccelOffset(1788); // 1688 factory default for my test chip
  mpu.CalibrateAccel(6);
  mpu.CalibrateGyro(6);
  mpu.PrintActiveOffsets();
  mpu.setDMPEnabled(true);
  mpuIntStatus = mpu.getIntStatus();
  dmpReady = true;
  packetSize = mpu.dmpGetFIFOPacketSize();
  // Set the maximum speed in steps per second:
  stepper_1.setMaxSpeed(500);
  stepper_2.setMaxSpeed(500);
  // Set the current position to 0:
  stepper_1.setCurrentPosition(0);
  stepper_2.setCurrentPosition(0);
}

void loop() {
  if (!dmpReady) return;
    // read a packet from FIFO
    if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) { // Get the Latest packet 
// display Euler angles in degrees
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetGravity(&gravity, &q);
            mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    }

if(Serial.available()) { 
  
//    command used for save the latest serial command sent by laptop
    char command = Serial.read();
    switch (command){
    case 'a' :
      // anti-clockwise rotate 36 degrees
      stepper_1.moveTo(13);
      
      stepper_1.setSpeed(100);
      stepper_1.run();
      
  
      break;

    case 'b' :
      // return to 0 degree
      // detect the motor current position
      if (stepper_1.currentPosition() == 13){
        stepper_1.moveTo(0);
        stepper_1.setSpeed(-100);
        stepper_1.run();
        
        
      }
      else if (stepper_1.currentPosition() == -13){
        stepper_1.moveTo(0);
        stepper_1.setSpeed(100);
        stepper_1.run();
        
        
        
      }
      else {}
      break;

    case 'c' :
      // clockwise rotate 36 degrees
      stepper_1.moveTo(-13);
      stepper_1.setSpeed(-100);
      stepper_1.run();
      
      
      
      break;

    case 'd' :
      // anti-clockwise rotate 36 degrees
      stepper_2.moveTo(13);
      stepper_2.setSpeed(100);
      stepper_2.run();
      
      
      
      break;

    case 'e' :
      // return to 0 degree
      // detect the motor current position
      if (stepper_2.currentPosition() == 13){
        stepper_2.moveTo(0);
        stepper_2.setSpeed(-100);
        
        stepper_2.run();
        
        
      }
      else if (stepper_2.currentPosition() == -13){
        stepper_2.moveTo(0);
        stepper_2.setSpeed(100);
        stepper_2.run();
        
        
        
      }
      else {}
      break;

    case 'f' :
      // clockwise rotate 36 degrees
      stepper_2.moveTo(-13);
      stepper_2.setSpeed(-100);
      
      stepper_2.run();
      
      
      break;
    
    Serial.flush();
    // already tried several values for the delay function
    delay(5);
    }
}
}

  
