import rrb3 as rrb
import time, random

# Change these for your setup.
BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

# Configure the RRB
rr = rrb.RRB3(9, 6)

tooClose = 20



while True:
    rr.set_motors(.7, 1, .7, 1)
    distance = rr.get_distance();
    print(distance)
    if distance < tooClose:
        rr.set_motors(0, 1, 0, 1)
        rr.forward(.5, .4)
        rr.right(2.3, .5)
        if rr.get_distance() < tooClose:
            rr.left(2.3, .5)
            if rr.get_distance() < tooClose:
                rr.forward(1, .3)
                rr.right(2.3, .5)
                rr.forward(4, .75)
    



