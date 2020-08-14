#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:54:37 2020

@author: krishan
"""
class P1:
    
    def m(self):
        print(" m of P1 called")
        
class P2:
    def m(self):
        print(" m of P2 called")
        

class C(P1, P2):
    def m(self):
        print("m of C called")

c = C()
c.m()

