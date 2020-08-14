#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:23:21 2020

@author: krishan
"""

class A:
    
    def __init__(self, s):        
        self.s = s
        
    def __add__(self, other):
        concat = f'{self.s} {other.s}'
        a = A(concat)
        return a
    
    def __str__(self):
        return str(self.s)
        
b1 = A('This') 
b2 = A('is') 
b3 = A('a')
b4 = A('python')
b5 = A('string')
print(b1 + b2 + b3+ b4 + b5)



