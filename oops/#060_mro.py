#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:50:07 2020

@author: krishan
"""
class A: pass
class B: pass
class C: pass
class X(A,B): pass
class Y(B,C): pass
class P(X,Y,C): pass

print(P.mro())

