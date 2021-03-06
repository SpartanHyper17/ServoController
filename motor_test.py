from __future__ import division
import time

# Import the PCA9685 module.
from PCA9685ROBOT import PCA9685ROBOT


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685ROBOT()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_med = 600  # Max pulse length out of 4096
servo_max = 2000

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
try:
    while True:
       # Move servo on channel O between extremes.
       pwm.set_pwm(0, 0, servo_min)
       time.sleep(2)
       pwm.set_pwm(0,0, servo_med)
       time.sleep(2)
       pwm.set_pwm(0, 0, servo_max)
       time.sleep(5)

except KeyboardInterrupt:
    print('Attempt Program interrupt')
    pwm.set_pwm(0, 0, 0)
    print('Program interrupted')
