#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:27:03 2020

@author: krishan
"""
class Mammal:
    
    def legs(self):
        print("Two Legs")
        
    def run(self):
        print("Slow")
        
class Men(Mammal): pass


m = Men()
m.run()
m.legs()

                                