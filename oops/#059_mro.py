#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:41:51 2020

@author: krishan
"""
class A:
    def m(self):
        print('Parent')
        
class B(A): pass

class C(A): pass

class D(B,C): pass

print(D.mro())

