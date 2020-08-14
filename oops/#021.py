#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:34:53 2020

@author: krishan
"""
class Silly:
    
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly
    
    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value
        
    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly