#! C:/python27

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kluitel"
__date__ ="$Sep 23, 2013 10:30:14 PM$"

if __name__ == "__main__":
    print "Hello World";

'''
function vs method
funtion -> standalone fnction
method -> inside a class

oop has a design pattern => python undehood module are build in oop
inheritance fron superclass in a subclass ... finally instance of subclass .. first look up in own class if not then in parent class

method override is allowed

'''
class Car(object):
    def __init__(self,year, make, model):
        '''  this is the constuctor'''
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = 'constant car data'
    def __str__(self):
        ''' formate a nice string '''
        return 'String representation: %s %s %s' % (self.year,self.make,self.model)
    def printcar(self):
        ''' Echos back the full name of the vehicle. '''
        print('{0} {1} {2}'.format(self.year,self.make,self.model)) 
        print self.static;
        
ks = Car('2013','Kia','Sorento')
str(ks)
print(ks) 
print(ks.static)
ks.printcar()