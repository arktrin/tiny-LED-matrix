#!/usr/bin/env python

import RPi.GPIO as IO  
import time 

# IO.setwarnings(False)  #do not show any warnings

x = 1
y = 1

IO.setmode(IO.BOARD)  

row_select = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20]
row_pins = [40, 37, 38, 35, 36, 33, 32, 31, 29]
col_pins = [22, 21, 19, 18, 15, 16]
for pin in row_pins+col_pins:
    IO.setup(pin, IO.OUT)

C = [0b1001,0b0110,0b1001,0b0110,0b1001,0b0110]
C = [0b1101,0b1101,0b1101,0b1011,0b1011,0b1011]
A = [0b0110,0b1001,0b1001,0b1111,0b1001,0b1001]
numbers = {0:[0b0110,0b1001,0b1001,0b1001,0b1001,0b0110],
           1:[0b0010,0b0110,0b1010,0b0010,0b0010,0b0010],
           2:[0b1111,0b0001,0b0001,0b0010,0b0100,0b1111],
           3:[0b1111,0b0001,0b0010,0b0001,0b0001,0b1111],
           4:[0b0001,0b0011,0b0101,0b1111,0b0001,0b0001],
           5:[0b1111,0b1000,0b1110,0b0001,0b0001,0b1110],
           6:[0b0010,0b0110,0b1010,0b0010,0b0010,0b0010]
           }


def reset_rows():
    for pin in row_pins:
        IO.output(pin, 0)

def set_row(val):
    if (val&0x01 == 0x01): IO.output(row_pins[0], 1)
    else: IO.output(row_pins[0], 0)
    if (val&0x02 == 0x02): IO.output(row_pins[1], 1)
    else: IO.output(row_pins[1], 0)
    if (val&0x04 == 0x04): IO.output(row_pins[2], 1)
    else: IO.output(row_pins[2], 0)
    if (val&0x08 == 0x08): IO.output(row_pins[3], 1)
    else: IO.output(row_pins[3], 0)
    if (val&0x10 == 0x10): IO.output(row_pins[4], 1)
    else: IO.output(row_pins[4], 0)
    if (val&0x20 == 0x20): IO.output(row_pins[5], 1)
    else: IO.output(row_pins[5], 0)
    '''
    if (pin&0x10 == 0x10): IO.output(19,0)
                    else:
                                IO.output(19,1)
    if(pin&0x10 == 0x10):
                IO.output(19,0)
                    else:
                                IO.output(19,1)
    if(pin&0x10 == 0x10):
                IO.output(19,0)
                    else:
                                IO.output(19,1)

    '''

def set_cols(val):
    if (val&0x01 == 0x01): IO.output(col_pins[0], 0)
    else: IO.output(col_pins[0], 1)
    if (val&0x02 == 0x02): IO.output(col_pins[1], 0)
    else: IO.output(col_pins[1], 1)
    if (val&0x04 == 0x04): IO.output(col_pins[2], 0)
    else: IO.output(col_pins[2], 1)
    if (val&0x08 == 0x08): IO.output(col_pins[3], 0)
    else: IO.output(col_pins[3], 1)
    if (val&0x10 == 0x10): IO.output(col_pins[4], 0)
    else: IO.output(col_pins[4], 1)

def show(list_of_vals):
    for i in xrange(200):
        for y in xrange(len(list_of_vals)):
            set_cols(list_of_vals[y])
            set_row(row_select[y])
            time.sleep(0.0005)
            reset_rows()

while 1:
    show(numbers[0])
    show(numbers[1])
    show(numbers[2])
    show(numbers[3])
    show(numbers[4])
    show(numbers[5])
    show(numbers[6])

# IO.output(21, 1)
# IO.output(19, 1)
# IO.output(18, 1)
# IO.output(22, 0)


