#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:15:37 2020

@author: krishan
"""
class ContactList(list):
    
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    '''this class is responsible for maintaining a list of all contacts 
    in a class variable all_contacts'''
    
    all_contacts = ContactList()
    def __init__(self, name, email):    

        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    
    def order(self, order):
        print("If this were a real system we would send "
        "'{}' order to '{}'".format(order, self.name))
