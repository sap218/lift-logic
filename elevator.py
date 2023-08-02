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

true_count = [0,0]
for n in range(20):
    attempt = choices(["PERSON INCOMING", "ALL GOOD"], weights=[0.1, 0.9], k=1)
    print(attempt)
    if attempt == "PERSON INCOMING":
        true_count[0] = true_count[0] + 1
    elif attempt == "ALL GOOD":
        true_count[1] = true_count[1] + 1


'''


sleeper = 1

def format_respons(response):
    response = response.lower().strip()
    return response
def check_if_int(response):
    print("you said:\t%s" % required_floor) 
    try:
        return int(response)
    except:
        return 

number_of_floors = randint(5,10)
print("there are %s floors in this building" % number_of_floors)
time.sleep(sleeper)

elevator_starts_on = randint(0,number_of_floors) # a <= N <= b
print("the elevator is on floor %s" %elevator_starts_on)
time.sleep(sleeper)

person_counter = 1
people_and_floors = {"person %s" % person_counter:0}


while True: 
    required_floor = format_respons(input("you are on the ground floor (0) - what floor do you need?\t"))
    required_floor = check_if_int(required_floor)
    if isinstance(required_floor,int) and required_floor <= number_of_floors:
        if required_floor < 1:
            print("\ni guess you didn't need the elevator after all...you wont learn about elevators today")
            time.sleep(3)
            exit()
        else:
            print("great!\n")
            time.sleep(2)
        break
    else:
        print('please give an appropriate floor number...') 
        time.sleep(1)


for n in range(elevator_starts_on, people_and_floors['person 1'] - 1, -1):
    if required_floor < 1:
        exit()
    elif n == 0:
        print(n)
        time.sleep(1)
        print("\nBZZZ ground floor")
        time.sleep(2)
        print("*doors open for you*")
        time.sleep(3)
    else:
        print(n)
        time.sleep(sleeper)
        attempt = choice([True, False])
        print(attempt)
    
print("\nheading to floor %s\n" % required_floor)
time.sleep(2)

for n in range(required_floor+1):
    print(n)
    time.sleep(sleeper)

time.sleep(1)
print("\nBZZZ floor %s" % required_floor)
time.sleep(2)
print("*doors open for you*")
time.sleep(3)
print("thank you for using the elevator - have a great day!")
time.sleep(5)
exit()

'''
