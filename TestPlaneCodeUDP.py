#!/usr/bin/python

import sys
import time

import socket
try:
   import cPickle as pickle
except:
   import pickle

# Setup Variables & Socket
IP = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, 5000))
print ("Ready")
PWM_OUTPUT = 0
SERVO_MIN = 1.250 #ms
SERVO_MAX = 1.750 #ms
navio.util.check_apm()


while True:
   raw_message,data = s.recvfrom(1024)
   (data_x, data_y, data_s, data_z, JoyButton_0, JoyButton_1, JoyButton_2) = pickle.loads(raw_message)
   if JoyButton_0 == 1:
      print("heelo")
   if JoyButton_1 == 1:
      print("Potato")
   if JoyButton_2 == 1:
      print("Dog")

   Aileron_Servo = (0.0025*data_x)+1.5
   Elevator_Servo = (0.0025*data_y)+1.5
   Throttle_Servo = (0.005*data_s)+1.250
   Rudder_Servo = (0.0025*data_z)+1.5
   

   if 1.250 <= Aileron_Servo <= 1.750:
      print (Aileron_Servo)
   #if 150 <= Elevator_Servo <= 600:
   #   Servo1 = Elevator_Servo
   #   pwm.setPWM(1, 0, Elevator_Servo)
   #if 150 <= Throttle_Servo <= 600:
   #   Servo2 = Throttle_Servo
   #   pwm.setPWM(2, 0, Throttle_Servo)
   #if 150 <= Rudder_Servo <= 600:
   #   Servo3 = Rudder_Servo
   #   pwm.setPWM(3, 0, Rudder_Servo)
      




