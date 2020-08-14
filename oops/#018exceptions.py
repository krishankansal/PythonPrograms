#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:51:19 2020

@author: krishan
"""

class InvalidWithdrawal(Exception):
    'Defining our own exception'
    def __init__(self, balance, amount):
        '''
        The Exception.__init__ method is designed to accept any arguments 
        and store them as a tuple in an attribute named args .
        '''
        super().__init__(f"Account doesn't have ${amount}.")
        self.amount = amount
        self.balance = balance
        
    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print(f"I'm sorry, but your withdrawal is more than your balance by ${e.overage()}")

    


