#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kluitel"
__date__ ="$Sep 23, 2013 11:48:31 PM$"

if __name__ == "__main__":
    print "Hello World";
'''
advance topic

1. Generators
    
    . accelarates the function execution
    . resumable function
    . retunrs results one at a time
    . suspend/resume state !important
    
    Gene expression
        . return results on demand instead of a full list
        . works for function and expresion
        
        
    purpose :
        save memory
        save computin cycles
   example: 
   in for loop : hold on a place and go to another task and pick it up from there later
   def gensq(n):
        for i in range(n):
            yield i ** 2
 a = gensq(6)
 next(a) = one output at a time
 next(a)
 next(a)
 next(a)
 
   
    
2. decorators
    wrape other functions

'''