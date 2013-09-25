#! /usr/bin/python
fmenu = {'spam':2.50,'ham':1.99,'eggs':0.99}
corder = raw_input("What do you ;lokek to have todsay: ")
if corder == 'spam':
    print ("For the spam., that will be $ ","%1f" % fmenu.get('spam'),' please ')
elif corder == 'ham':
    print ("For the ham., that will be $ ","%1f" % fmenu['ham'],' please! ')
else:
    print ("For the eggs., that will be $ ","%1f" % fmenu.get('eggs'),' please! ')
    
    