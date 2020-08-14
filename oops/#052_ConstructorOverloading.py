#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:10:13 2020

@author: krishan
"""


class A:
    
    def __init__(self ,*a):
        x = len(a)
        print(f'{x} argument constructor called')
        print(f'Parameter passed = {a}')
        
   
        
        
A()
A(10)             
A(10,20)
A(10,20,'Jai')
A(10,20,'Jai',90.89)
A(10,20,'Jai',90.89,10,20,'Jai',90.89)

