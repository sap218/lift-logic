#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:09:19 2021

@author: samantha
"""

import time
from random import randint
from random import choice
from random import random

from random import choices

'''
true_count = [0,0]
for n in range(20):
    attempt = choices(["PERSON INCOMING", "ALL GOOD"], weights=[0.1, 0.9], k=1)
    print(attempt)
    if attempt == "PERSON INCOMING":
        true_count[0] = true_count[0] + 1
    elif attempt == "ALL GOOD":
        true_count[1] = true_count[1] + 1
    print(true_count)
'''

sleeper = 1

print("Hello and welcome to the !@#=%+ Building")

number_of_floors = randint(5,10)
print("There are %s floors in this building" % number_of_floors)
time.sleep(sleeper)

elevator_starts_on = randint(0,number_of_floors) # a <= N <= b
print("The elevator is currently on floor %s" %elevator_starts_on)
time.sleep(sleeper)

#person_counter = 1
#people_and_floors = {"person %s" % person_counter:0}

########################

sleeper = 1

def format_response(response):
    response = response.lower().strip()
    try:
        return int(response)
    except:
        response = False
        return  response


required_floor = False
while required_floor == False or required_floor > number_of_floors:
    required_floor = format_response(input("What floor do you need? (you are currently on ground floor (0)\t"))
    if not required_floor or required_floor > number_of_floors: print("Hmmm that is not an appropriate repsonse - please try again...")
print("You said you need to go to floor:\t%s" % required_floor) 

########################

print("\nLift going down\n")

for n in range(elevator_starts_on, -1, -1):
    time.sleep(1)
    print(n)
    if n == 0:
        time.sleep(1)
        print("\nBZZZ ground floor")
        time.sleep(2)
        print("*doors open for you*")
        time.sleep(3)
    #else:
    #    print(n)
    #    time.sleep(sleeper)
    #    attempt = choice([True, False])
    #    print(attempt)
    
#print("\nlift going up to floor %s\n" % required_floor)
print("\nLift going up\n")
time.sleep(2)

for n in range(required_floor+1):
    print(n)
    time.sleep(sleeper)
    if n == required_floor:
        time.sleep(1)
        print("BZZZ floor %s" % required_floor)
        time.sleep(2)
        print("*doors open for you*")
        time.sleep(2)
        print("thank you for using the elevator - have a great day!")
        time.sleep(4)


# end of script