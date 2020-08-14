#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:38:06 2020

@author: krishan
"""

class A: 
    def __init__(self, a): 
        self.a = a 
    
    def __eq__(self, other): 
        if(self.a == other.a): 
            return "Both are equal"
        else: 
            return "Not equal"
   
ob1 = A(4) 
ob2 = A(4) 
print(ob1 == ob2) 
