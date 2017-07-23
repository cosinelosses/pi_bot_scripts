import time
from rrb3 import *
import time


rr = RRB3(9, 6)

def get_valid(direct):
    valid = False; 
    if direct == 'w':
        valid = True
    if direct == 'a':
        valid = True
    if direct == 's':
        valid = True
    if direct == 'd':
        valid = True

    return valid
         
        

while True:
    direction = raw_input("which way?")

    if get_valid:    
        if direction == 'w':
            rr.reverse(3, .5)
        if direction == 'ww':c
        rr.reverse(6, .5)
        if direction == 'wwf':
            rr.reverse(6, 1)
        if direction == 'wc':
            rr.reverse(3, .1)
        if direction == 'a':
            rr.left(1.2, .5)
        if direction == 's':
            rr.forward(3, .75)
        if direction == 'd':
            rr.right(1.2, .5)


