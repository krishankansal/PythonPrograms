#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:00:11 2020

@author: krishan
"""
class Book:
    
    def __init__(self, pages):        
        self.pages = pages
        
    def __add__(self, other):
        return self.pages + other.pages
        
b1 = Book(100) # self
b2 = Book(200) # other
print(b1 + b2)
print(type(b1 + b2)) # <class 'int'>

##############################################
b3 = Book(300)
print(Book(b1 + b2) + b3)

b4 = Book(400)
print(Book(b1 + b2) + Book(b3+ b4))

b5 = Book(500)
print(Book(Book(b1 + b2) + Book(b3+ b4)) + b5)
