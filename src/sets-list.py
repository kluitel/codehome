#! /usr/bin/python
'''
set is unorder colleciton of of unique immutable elements
- not a seq (str,list,tuple)
- not a mapping(dict)

myset = set ('python')
myset2 = set ([0,1,2,3,4])
'''

s1 = set([0,1,2,3,6])
print type(s1)
print s1
s2 =  set('cbtnuggets')
print s2
s3 = set([8,9,10,11])
s1.update(s3)
print s1
newset = set(s1)
print id(s1)
print id(newset)

s1.pop() # ramdomly pops the items nto good
s1.remove(10) # specify what you want to remove .. GOOD
print s1
print("##############################3")
print (11 not in s1)
s1.clear()
print s1
print("##############################3")
import wiper
wiper.w()
set1  = set()
set1.add(0)
set1.add(1)
set2 = set([2,3,4,5])
set1.update(set2)
print set1
wiper.w()
####################

lang  = ['python','c','python','c++','php']
l1 = set(lang)
morelang = ['ruby','perls','c','abc','php']
l2 = set(morelang)
print l1
print l2
l3 = l1 - l2
print l3
print (l1.intersection(l2))
l4 = l1.union(l2)
print(l2.issubset(l4))
wiper.w()
###########################
## set comprehension is short hand way of creating a new set
s2 = set([16,10,12,14])
print(type(s2))
setcom = {i*2 for i in s2}
print setcom
print(type(setcom))

#######################]
## ADCANCE SET 
## list compreshension - nifty short hand methoind of creating a new list
## is also used with map() function very poerfull
wiper.w()

'''
Oldway::: not good lgnthy
my_list = ['MIXeD','CASE','ElemenNTS']
t = []
for x in my_list:
    t.append(x.lower())
my_list = t

NEW WZAY ... list comprehension

#my_list = [action for-lpop]
my_list = [x.lower for x in my_list]
'''

alist = [1,2,3,4,5]
alist = [i*4 for i in alist]
print alist
print(type(alist))

phrase = "lorem ipsun sit amet asdf asdfa aditaaf elit".split(" ")
print (type(phrase))
print phrase
stuff = [[x.upper(), x.lower(), len(x)] for x in phrase]
print stuff

### dict comprehension
wiper.w()
dic1 = {'ay':1,'bee':2,'cee':3}
dic2 = {value:key for key, value in dic1.items()}
print dic2
wiper.w()
file = list(open("C:/Users/kluitel/Documents/NetBeansProjects/NewPythonProject/src/lang.txt"))
lang = [line.rstrip() for line in file]
print lang;







































