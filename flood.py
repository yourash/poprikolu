#!/usr/bin/python
import pyatspi, time, random

incrementor=1

def privet():
    reg(42, None, pyatspi.KEY_PRESSRELEASE)#42-russian "p"
    time.sleep(0.05)
    reg(43, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(56, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(40, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(28, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(57, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(1)
    reg(36, None, pyatspi.KEY_PRESSRELEASE)#

def hay():
    reg(34, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(41, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(24, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(1)
    reg(36, None, pyatspi.KEY_PRESSRELEASE)#

def lol():
    reg(45, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(44, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(45, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(1)
    reg(36, None, pyatspi.KEY_PRESSRELEASE)#

def kek():
    reg(27, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(28, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(0.05)
    reg(27, None, pyatspi.KEY_PRESSRELEASE)
    time.sleep(1)
    reg(36, None, pyatspi.KEY_PRESSRELEASE)#
      
time.sleep(3)
reg = pyatspi.Registry.generateKeyboardEvent
for i in range(12):#flood 12 times
    print(incrementor)
    incrementor+=1
    time.sleep(random.randint(1, 3))
    if random.randint(0, 3)== 0:
        privet()
    elif random.randint(0, 3)== 1:
        hay()
    elif random.randint(0, 3)== 2:
        lol()
    elif random.randint(0, 3)== 3:
        kek()

        #reg(36, None, pyatspi.KEY_PRESSRELEASE) - enter



