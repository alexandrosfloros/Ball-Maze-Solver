import serial
from time import sleep

arduino = serial.Serial('COM3', 115200, timeout=0.5)
sleep(5)
# 1:motor1 clockwise rotate 36 degrees
# 2:motor1 return to 0 degree
# 3:motor1 anti-clockwise rotate 36 degrees
# -1:motor2 clockwise rotate 36 degrees
# -2:motor2 return to 0 degree
# -3:motor2 anti-clockwise rotate 36 degrees
angles = [1, 2, 3, -1, -2, -3, 1, 2, 3]
# signals being sent to the motor-driver

for angle in angles:
    command = str(angle)
    arduino.write(bytes(str(angle), 'utf-8'))
    sleep(1)

arduino.close()
