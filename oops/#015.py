
"""
Created on Thu Jun 18 08:15:30 2020 @author: krishan
"""

class EvenOnly(list):
    '''This class extends the list built-in'''
    
    def append(self, integer):
        '''
        overrides the append method to check two conditions that ensure the item is an
        even integer
        '''
        if not isinstance(integer,int):
            raise TypeError("Only integers can be added")
            
        if integer % 2:
            raise ValueError("Only even numbers can be added")
            
        super().append(integer)
    
        
        

        
        
        


