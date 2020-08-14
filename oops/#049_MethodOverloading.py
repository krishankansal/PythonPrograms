#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:15:51 2020

@author: krishan
"""
class A:
   
    # No need for method overloading in python
    # we can always do like this
    def add(self, a = 0, b = 0, c=0, d=0):
        return a + b + c + d
    
    # or we can also do this
    # no limitation, we can supply any numbers we want to add
    def add_another_example(self, *x):
        total = 0
        for num in x:
            total = total + num
        return total
    
    def concat(self, a = '', b = '', c = '', d = ''):
        return f'{a} {b} {c} {d}'
    
      
# Uncommenting the below line shows an error     
# print(A().product(4, 5))      
# This line will call the second product method 

print(A().add(4, 5))
print(A().add(4, 5, 6))
print(A().add(4, 5, 6,7))
print(A().concat('Abdul'))
print(A().concat('Abdul','kalam'))
print(A().concat('Abdul','kalam','Mr.'))
print(A().concat('Abdul','kalam','Mr.','President'))
print(A().add_another_example())
print(A().add_another_example(4, 5))
print(A().add_another_example(4, 5, 6))
print(A().add_another_example(4, 5, 6,7))
print(A().add_another_example(4, 5, 6,7,7,7,7,7,7,7,7,7,7,7,7,7,7))

