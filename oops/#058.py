#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:34:33 2020

@author: krishan
"""
normal_list=[1,2,3,4,5]

class CustomSequence():
    def __len__(self):
        return 5
    def __getitem__(self, index):
        return "x{0}".format(index)
class FunkyBackwards():
    def __reversed__(self):
        return "BACKWARDS!"
    
for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end="")
for item in reversed(seq):
    print(item, end=", ")

