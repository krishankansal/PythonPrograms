#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:02:09 2020

@author: krishan
"""
class AverageList(list):
    
    @property
    def average(self):
        return sum(self) / len(self)
    

a = AverageList([1,2,3,4])
print(a.average)