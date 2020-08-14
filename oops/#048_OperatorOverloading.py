#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:50:06 2020

@author: krishan
"""
class Emp:
    
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
        
    def __mul__(self, wd):
        return self.sal * wd.days
        
class WorkingDays:
    
    def __init__(self, name, days):
        self.name = name
        self.days = days    
        
    def __mul__(self, emp):
        return self.days * emp.sal
        
        
e = Emp('Manu', 1000)
d = WorkingDays('Manu', 25)

print('Salary of ' + e.name + ' is = ' + str(e*d))
print('Salary of ' + e.name + ' is = ' + str(d*e))

