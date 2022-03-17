import serial
from time import sleep

arduino = serial.Serial('COM3', 115200, timeout=0.5)
sleep(1)
# a:motor1 clockwise rotate 36 degrees
# b:motor1 return to 0 degree
# c:motor1 anti-clockwise rotate 36 degrees
# d:motor2 clockwise rotate 36 degrees
# e:motor2 return to 0 degree
# f:motor2 anti-clockwise rotate 36 degrees
# signals being sent to the motor-driver


while 1:
    var = str(input())
    print('you entered :', var)

    if(var == 'a'):
        arduino.write(b'a')
        print('motor1 clockwise rotate 36 degrees')
        #sleep(0.1)
    elif(var == 'b'):
        arduino.write(b'b')
        print('motor1 return to 0 degree')
        #sleep(0.1)
    elif(var == 'c'):
        arduino.write(b'c')
        print('motor1 anti-clockwise rotate 36 degrees')
        #sleep(0.1)
    elif(var == 'd'):
        arduino.write(b'd')
        print('motor2 clockwise rotate 36 degrees')
        #sleep(0.1)
    elif(var == 'e'):
        arduino.write(b'e')
        print('motor2 return to 0 degree')
        #sleep(0.1)
    elif(var == 'f'):
        arduino.write(b'f')
        print('motor2 anti-clockwise rotate 36 degrees')
        #sleep(0.1)
    elif(var == 'g'):
        arduino.write(b'g')
        print('led lighten up')
        #sleep(0.1)
    else:
        print()

arduino.close()
