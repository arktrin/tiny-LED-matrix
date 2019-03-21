#!/usr/bin/env python

import RPi.GPIO as IO  
import time 

# IO.setwarnings(False)  # do not show any warnings
IO.setmode(IO.BOARD)  

col_select = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20]
row_select = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x100, 0x200]
row_pins = [40, 37, 38, 35, 36, 33, 32, 31, 29, 23]
col_pins = [22, 21, 19, 18, 15, 16]
for pin in row_pins+col_pins:
    IO.setup(pin, IO.OUT)

all_ones = 10*[0b111111]
numbers = {0:[0b001100,0b010010,0b100001,0b100001,0b100001,0b100001,0b100001,0b100001,0b010010,0b001100],
           1:[0b000100,0b000100,0b000100,0b000100,0b000100,0b000100,0b000100,0b000100,0b000100,0b000100],
           2:[0b011110,0b100001,0b000001,0b000001,0b000010,0b001100,0b010000,0b100000,0b100000,0b111111],
           3:[0b111111,0b000001,0b000010,0b000100,0b001110,0b000001,0b000001,0b000001,0b100001,0b011110],
           4:[0b000001,0b000011,0b000101,0b001001,0b010001,0b100001,0b111111,0b000001,0b000001,0b000001],
           5:[0b111111,0b100000,0b100000,0b010000,0b001100,0b000010,0b000001,0b000001,0b100001,0b011110],
           6:[0b000010,0b000100,0b001000,0b010000,0b111110,0b100001,0b100001,0b100001,0b100001,0b011110],
           7:[0b111111,0b000001,0b000010,0b000010,0b000010,0b000100,0b000100,0b000100,0b001000,0b001000],
           8:[0b011110,0b100001,0b100001,0b010010,0b001100,0b010010,0b100001,0b100001,0b100001,0b011110],
           9:[0b011110,0b100001,0b100001,0b100001,0b100001,0b011111,0b000010,0b000100,0b001000,0b010000]
           }

for i in xrange(10):
    numbers[i] = numbers[i][::-1]

def reset_rows():
    for pin in row_pins:
        IO.output(pin, 0)

def set_row(val):
    if (val&0x01 == 0x01): IO.output(row_pins[9], 0); IO.output(row_pins[0], 1);
    elif (val&0x02 == 0x02): IO.output(row_pins[0], 0); IO.output(row_pins[1], 1);
    elif (val&0x04 == 0x04): IO.output(row_pins[1], 0); IO.output(row_pins[2], 1);
    elif (val&0x08 == 0x08): IO.output(row_pins[2], 0); IO.output(row_pins[3], 1);
    elif (val&0x10 == 0x10): IO.output(row_pins[3], 0); IO.output(row_pins[4], 1);
    elif (val&0x20 == 0x20): IO.output(row_pins[4], 0); IO.output(row_pins[5], 1);
    elif (val&0x40 == 0x40): IO.output(row_pins[5], 0); IO.output(row_pins[6], 1);
    elif (val&0x80 == 0x80): IO.output(row_pins[6], 0); IO.output(row_pins[7], 1);
    elif (val&0x100 == 0x100): IO.output(row_pins[7], 0); IO.output(row_pins[8], 1);
    else: IO.output(row_pins[8], 0); IO.output(row_pins[9], 1);

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
    if (val&0x20 == 0x20): IO.output(col_pins[5], 0)
    else: IO.output(col_pins[5], 1)

def show(list_of_vals, cycles=100, t_on=0.0005, t_off=0):
    for i in xrange(cycles):
        for y in xrange(len(list_of_vals)):
            set_cols(list_of_vals[y])
            set_row(row_select[y])
            time.sleep(t_on)
            reset_rows()
            time.sleep(t_off)

def show_pulse(list_of_vals):
    for j in range(20)+range(19,-1,-1):
        show(list_of_vals, cycles=3, t_on=0.002-j*0.0001, t_off=j*0.0001)

while 1:
    for i in xrange(10):
        show_pulse(numbers[i])
