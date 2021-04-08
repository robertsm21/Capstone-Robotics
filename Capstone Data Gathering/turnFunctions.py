import time
import board
from adafruit_motorkit import MotorKit
from usfs import USFS_Master
import math

MAG_RATE = 100 #Hz
ACCEL_RATE = 200 #Hz
GYRO_RATE = 200 #Hz
BARO_RATE = 50 #Hz
Q_RATE_DIVISOR = 3 #1/3 gyro rate

usfs = USFS_Master(MAG_RATE, ACCEL_RATE, GYRO_RATE, BARO_RATE, Q_RATE_DIVISOR)

#Start the USFS in master mode
if not usfs.begin():
    print(usfs.getErrorString())
    exit(1)

wheels = MotorKit(i2c = board.I2C())

class robotManuevers:
    def turnLeft90Over():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = 0.80
        wheels.motor4.throttle = -0.67
        time.sleep(.84)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def turnLeft90():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = 0.7
        wheels.motor4.throttle = -0.65
        time.sleep(.93)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def turnLeft90USFS():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        for count in range(1000)
            usfs.checkEventStatus()
        
            if usfs.gotError():
                print('ERROR: ' + usfs.getErrorString())
                exit(1)
            if (usfs.gotQuaternion()):
                qw, qx, qy, qz = usfs.readQuaternion()
                angle = math.atan2(2.0*(qx*qy+qw*qz), qw*qw+qx*qx-qy*qy-qz*qz)
                angle*=180.0
                angle+=9.1
                if angle < 0: angle += 360.0
                startAngle = angle
        print('Start angle: ', startAngle)
        time.sleep(.05)
        while abs(startAngle - angle) < 90:
            usfs.checkEventStatus()
            if usfs.gotError():
                print("ERROR: " + usfs.getErrorString())
            if (usfs.gotQuaternion()):
                qw, qx, qy, qz = usfs.readQuaternion()
                angle = math.atan2(2.0*(qx*qy+qw*qz), qw*qw+qx*qx-qy*qy-qz*qz)
                angle*=180.0
                angle+=9.1
                if angle < 0: angle += 360.0
                print("current angle: ", angle)
                print("start angle: ", startAngle)
                print("difference: ", abs(startAngle - angle))
                wheels.motor3.throttle = 0.7
                wheels.motor4.throttle = -0.65
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
        
    def turnRight90():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = -0.68
        wheels.motor4.throttle = 0.67
        time.sleep(.89)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def goStraight():
        wheels.motor3.throttle = 0.64
        wheels.motor4.throttle = 0.54
#         time.sleep(0.5)
#         wheels.motor3.throttle = 0
#         wheels.motor4.throttle = 0
#         time.sleep(0.5)
    
    def goStraightVeerLeft():
        wheels.motor3.throttle = 0.59
        wheels.motor4.throttle = 0.48
#         time.sleep(0.5)
#         wheels.motor3.throttle = 0
#         wheels.motor4.throttle = 0
#         time.sleep(0.5)

    def goBack():
        wheels.motor3.throttle = -0.75
        wheels.motor4.throttle = -0.75
        time.sleep(0.5)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(0.5)

    def turnAround():
        wheels.motor3.throttle = -0.75
        wheels.motor4.throttle = -0.75
        time.sleep(2)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(0.5)
        
    def stopMoving():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
 
    

# time.sleep(5)
#goStraight()
#goBack()
#turnLeft90()
#turnRight90()
#turnAround()
