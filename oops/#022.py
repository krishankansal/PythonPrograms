#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:46:35 2020
@author: krishan
"""
import requests

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None
        
    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = requests.get(self.url).text
        return self._content
    
