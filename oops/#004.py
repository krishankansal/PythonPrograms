#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:06:35 2020

@author: krishan
"""
class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(0, 0)
        
# Constructing a Point
point = Point(y=45)
print(point.x, point.y)

