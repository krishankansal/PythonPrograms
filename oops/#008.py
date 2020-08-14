#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:34:33 2020

@author: krishan
"""


class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
        
obj1 = Sample()

#dir(obj1)