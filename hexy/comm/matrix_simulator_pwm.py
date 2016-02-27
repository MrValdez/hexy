#!/usr/bin/python

import math

import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

class PWM :
  def update_pygame():
    #clock.tick(60)
    pygame.display.flip()
    
    screen.fill([0, 0, 0])
    events = pygame.event.get()

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

  def setPWM(self, channel, on, off):
    "Sets a single PWM channel"
    if 0:
      print(self.__LED0_ON_L+4*channel, on & 0xFF)
      print(self.__LED0_ON_H+4*channel, on >> 8)
      print(self.__LED0_OFF_L+4*channel, off & 0xFF)
      print(self.__LED0_OFF_H+4*channel, off >> 8)
      raw_input()

    #if (self.debug):
    #  print ("setPWM")
    
    self.update_pygame()

  def setAllPWM(self, on, off):
    "Sets a all PWM channels"
    if (self.debug):
      print("setAllPwm")

  def getPWM(self, channel):
    if (self.debug):
      print("getPWM")
      
    if channel > 15:
      return
