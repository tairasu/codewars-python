# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python


def zero(op=None):
    if op:
        return op(0)
    else:
        return 0

def one(op=None):
    if op:
        return op(1)
    else:
        return 1

def two(op=None):
    if op:
        return op(2)
    else:
        return 2

def three(op=None):
    if op:
        return op(3)
    else:
        return 3

def four(op=None):
    if op:
        return op(4)
    else:
        return 4

def five(op=None):
    if op:
        return op(5)
    else:
        return 5

def six(op=None):
    if op:
        return op(6)
    else:
        return 6

def seven(op=None):
    if op:
        return op(7)
    else:
        return 7

def eight(op=None):
    if op:
        return op(8)
    else:
        return 8

def nine(op=None):
    if op:
        return op(9)
    else:
        return 9

def plus(second):
    return lambda first: first + second

def minus(second):
    return lambda first: first - second

def times(second):
    return lambda first: first * second

def divided_by(second):
    return lambda first: first // second