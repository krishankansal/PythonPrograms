#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:48:55 2020

@author: krishan
"""

def divide_with_exception(number, divisor):
    try:
        
        print(f"{number} / {divisor} = {divisor * 1.0}")
      
    except ZeroDivisionError:
        print("You can't divide by zero")
    
def divide_with_if(number, divisor):
    '''We could avoid a ZeroDivisionError ever being thrown by testing 
       for it with an if statement.'''
       
    if divisor == 0:
        print("Yyou can't divide by zero")
    else:
        print(f"{number} / {divisor} = {divisor * 1.0}")
        

divide_with_exception(12, 0)
divide_with_if(14, 0)