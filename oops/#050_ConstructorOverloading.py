#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:01:58 2020

@author: krishan
"""
class A:
    
    def __init__(self):
        print('Zero argument constructor called')
        
    def __init__(self, x):
        print('One argument constructor called')
        
    def __init__(self, x, y):
        print('Two argument constructor called')
        
        
#A()
#A(10)             
A(10,20)

