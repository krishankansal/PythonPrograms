#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:45:48 2020

@author: krishan
"""
class P1:
    
    def m(self):
        print(" m of P1 called")
        
class P2:
    def m(self):
        print(" m of P2 called")
        
# Try by changing order of P1,P2
class C(P1, P2): pass

c = C()
c.m()
    

