#! /usr/bin/python
# for i in iterable
# iterable can be: string, list, tuple,dict
string = "asdfasdf"
for i in string:
    print i
    
tuplelist = [(1,2),(3,4),(5,6)]
for (i,j) in tuplelist:
    print (i,j)
for veg in ['celery','musroom','okra']:
    print ("current veg => ",veg)
print("############")
for i in range(1,5):
    print(i)
print("############")
for i in range(5):
    print(i)
    
import os
#for k, v  in os.environ.items():
   #print(k,v)

f = open("C:/Users/kluitel/Documents/NetBeansProjects/NewPythonProject/src/test.txt")
for line in f:
    print(line)
nm  = {'1':'value','2':'val2','3':'val3'}
for k, v in nm.items():
    print (k,v)
i = ["abc",123,(5,6),4.30]
query = [(5,6),3.14]
for key in query:
    if key in i:
        print (key, " found")
    else:
        print(key,"not found")

print("################")
        
x = 0
y = 13
while x < y:
    print x
    x= x+1
    
print("################")

a = 0
while a < 13:
    a += 1
    if a == 5:
        continue
    if a == 10:
        break
    print (a)

    
    

        
