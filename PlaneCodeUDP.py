#!/usr/bin/python

import sys
import time

import navio.pwm
import navio.util

import socket
try:
   import cPickle as pickle
except:
   import pickle

# Setup Variables & Socket
IP = '192.168.0.113'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, 5000))
print ("Ready")

# Servo Vars
pwm = navio.pwm.PWM(0)
pwm.set_period(50)
SERVO_MIN = 1.250 #ms
SERVO_MAX = 1.750 #ms
Aileron_Servo_No = 0
Elevator_Servo_No = 1
Throttle_Servo_No = 2
Rudder_Servo_No = 3

while True:
   raw_message,data = s.recvfrom(1024)
   (data_x, data_y, data_s, data_z, JoyButton_0, JoyButton_1, JoyButton_2) = pickle.loads(raw_message)
   if JoyButton_0 == 1:
      print("heelo")
   if JoyButton_1 == 1:
      print("Potato")
   if JoyButton_2 == 1:
      print("Dog")

   Aileron_Servo = (2.25*data_x)+375
   Elevator_Servo = (2.25*data_y)+375
   Throttle_Servo = (4.5*data_s)+150
   Rudder_Servo = (2.25*data_z)+375
   

   if 150 <= Aileron_Servo <= 600:
      pwm = navio.pwm.PWM(Aileron_Servo_No)
      pwm.set_duty_cycle(Aileron_Servo)
   if 150 <= Elevator_Servo <= 600:
      pwm = navio.pwm.PWM(Elevator_Servo_No)
      pwm.set_duty_cycle(Elevator_Servo)
   if 150 <= Throttle_Servo <= 600:
      pwm = navio.pwm.PWM(Throttle_Servo_No)
      pwm.set_duty_cycle(Throttle_Servo)
   if 150 <= Rudder_Servo <= 600:
      pwm = navio.pwm.PWM(Rudder_Servo_No)
      pwm.set_duty_cycle(Rudder_Servo)
      




