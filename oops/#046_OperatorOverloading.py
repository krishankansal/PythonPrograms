#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:19:36 2020

@author: krishan
"""
class Book:
    
    def __init__(self, pages):        
        self.pages = pages
        
    def __add__(self, other):
        total = self.pages + other.pages
        b = Book(total)
        return b
    
    def __mul__(self, other):
        total = self.pages * other.pages
        b = Book(total)
        return b
    
    def __str__(self):
        return str(self.pages)
        
b1 = Book(100) 
b2 = Book(200) 
b3 = Book(300)
b4 = Book(400)
b5 = Book(500)
print(b1 + b2 + b3 + b4 + b5)
print(b1 * b2 + b3 + b4 * b5)



