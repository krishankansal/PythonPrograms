#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 07:24:23 2020 author: krishan
"""
class Employee:
    
    salary_raise = 1.04
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary        
        
    @property
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    @fullname.setter
    def fullname(self, fullname):
        fname, lname = fullname.split(' ')
        self.fname = fname
        self.lname = lname
    
    @property
    def email(self):
        return  f'{self.fname}.{self.lname}@company.com'
    
    def __str__(self):
        return f'Employee : {self.fullname}'
    
emp_1 = Employee('krishan','kansal',80000)
emp_2 = Employee('corey','shafer',60000)

emp_1.fullname = 'john kwin'

print(emp_1.email)
print(emp_1.fullname)
print(emp_2)
print(emp_1.__class__.__name__)

