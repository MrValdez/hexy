#!/usr/bin/python

import math

import pygame

resolution = [800, 600]
pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

channels = {}

class PWM :
  def update_pygame(self):
    #clock.tick(60)
    pygame.display.flip()
    
    screen.fill([0, 0, 0])
    events = pygame.event.get()
    
    origin = [resolution[0] / 2, resolution[1] / 2]
    leg_distance = 20
    def translate_joints():            
        joints = []
        
        for key, angle in channels.items():
            start_pos = [0, 0]
    
            ##############
            # translate joints to their apropriate position
            # hardcoded warning: this is based on core.joint_properties
            current_index = key - self.STARTING_LED
            
            # we are only interested in every 3rd index
            print (current_index)
            if current_index % 4 != 2: continue
            
            # translate to left or right
            if ((0 <= current_index < 12) or
                (24 < current_index < 36) or
                (48 < current_index < 60)):
                # left side
                position = -1
            else:
                # right side
                position = +1

            # hip, knee, ankle
            if current_index % 3 == 0:
                # hip
                offset = leg_distance * 0
                color = (255, 128, 128)
            elif current_index % 3 == 1:
                # knee
                offset = leg_distance * 1
                color = (255, 128, 255)
            elif current_index % 3 == 2:
                # ankle
                offset = leg_distance * 2
                color = (255, 255, 255)

            start_pos[0] += (50 + offset + ((current_index%3) * 10)) * position
            
            # translate backward
            if (0 <= current_index < 24):
                offset = 0
            if (24 <= current_index < 48):
                offset = 20
            if (48 <= current_index < 72):
                offset = 40
            
            start_pos[1] -= offset
            ##############

            # add rotation from angle
#            x = end_pos[0] * math.cos(angle) - end_pos[1] * math.sin(angle)
#            y = end_pos[0] * math.sin(angle) + end_pos[1] * math.cos(angle)
#            end_pos = [x, y]

            angle = math.radians(angle)
            x = leg_distance * math.cos(angle)
            y = leg_distance * math.sin(angle)
            end_pos = [x + start_pos[0], y + start_pos[1]]

            # translate to origin
            for index, value in enumerate(origin):
                start_pos[index] += value
                end_pos[index] += value
                        
            joints.append([color, start_pos, end_pos])            
        return joints

    joints = translate_joints()
    from pprint import pprint
    #pprint(joints)
    #raw_input()
    for color, start_pos, end_pos in joints:
        color = pygame.Color(*color)
        pygame.draw.line(screen, color, start_pos, end_pos)

  @classmethod
  def softwareReset(cls):
    "Sends a software reset (SWRST) command to all the servo drivers on the bus"
    if (self.debug):
      print ("reset")
    
  #def __init__(self, address=0x40, debug=False):
  def __init__(self, address=0x40, debug=True):
    self.debug = debug
    

  def setPWMFreq(self, freq):
    "Sets the PWM frequency"
    if (self.debug):
      print("setPWMFreq")

  __LED0_ON_L          = 0x06
  __LED0_ON_H          = 0x07
  __LED0_OFF_L         = 0x08
  __LED0_OFF_H         = 0x09
  
  STARTING_LED         = __LED0_ON_L

  def setPWM(self, channel, on, off):
    "Sets a single PWM channel"

    channel_targets = [self.__LED0_ON_L+4*channel, 
                       self.__LED0_ON_H+4*channel,
                       self.__LED0_OFF_L+4*channel,
                       self.__LED0_OFF_H+4*channel]
    # add channel if it isn't in the dictionary
    for c in channel_targets:
        if c not in channels:
            channels[c] = 0
    
    channels[channel_targets[0]] = on & 0xFF
    channels[channel_targets[1]] = on >> 8
    channels[channel_targets[2]] = off & 0xFF
    channels[channel_targets[3]] = off >> 8

    self.update_pygame()

    if 1:
      for c in channel_targets:
        print("{}: {}".format(c, channels[c]))
      
  def setAllPWM(self, on, off):
    "Sets a all PWM channels"
    if (self.debug):
      print("setAllPwm")

  def getPWM(self, channel):
    if (self.debug):
      print("getPWM")
      
    if channel > 15:
      return
