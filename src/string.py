#! /usr/bin/python
# string advance
# imutable
import wiper
str1 = '            this is sample stringis.            '
print str1.capitalize()
print str1.count('is')
print str1.count(' is ')
print str1.find('amp')
#print str1.isuper()
print str1.lstrip()
print str1.rstrip()
days = ['Monday','Tuesday','Wednesday']
print days
week = ' '.join(days)
print(week)

## string fotmating(sf) - days
#s.f expression
wiper.w()
s= "%s has %d vacation days left" % ('Khara',14)
print s
#sf method call ## must be zero indexed
ss = "{0} has {1} vacation days left".format("Khara",'sarasre')
print ss