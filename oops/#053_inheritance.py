#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:31:18 2020

@author: krishan
"""

class Mammal:
    
    def __init__(self, age):
        self.age = age
    
    def legs(self):
        print("Two Legs")
        
    def run(self):
        print("Slow")
        
class Men(Mammal): 
    
    def __init__(self, age, color):
        super().__init__(age)
        self.color = color
    
    def run(self):
        print("Fast")


m = Men(5, 'blonde')
m.run()
m.legs()
print(m.age)
print(m.color)


