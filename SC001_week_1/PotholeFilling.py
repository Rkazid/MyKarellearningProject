"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():

    for i in range(3):
        go_in()
        put_99()
        go_out()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole ,facing EAST
    post-condition:Karel is at the pothole,facing SOUTH
    """
    move()
    turn_right()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99():
    for i in range(99):
        put_beeper()


def go_out():
    """
    pre-condition:Karel is at the pothole,facing SOUTH
    post-condition:Karel is at the upper left of the pothole ,facing EAST
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()






















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
