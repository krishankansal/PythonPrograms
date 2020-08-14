#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:25:17 2020

@author: krishan
"""
class Mammal(object):
  def __init__(self):
    print('warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
   
    
d1 = Dog()

