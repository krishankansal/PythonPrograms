#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:24:01 2020

@author: krishan
"""
class Student:
    
    collegeName = 'KITS'
    
    def __init__(self, name):
        self.name = name
    
# Aggregation[No need for object]
print(Student.collegeName)

s = Student('Arjun')

# Composition[Without object name cannot exist]
print(s.name)

