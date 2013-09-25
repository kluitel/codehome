#! /usr/bin/python
#tuples =  index string () immutable sequence of data structure
# static cannot be modified dynamically 
#can be integratedwith disctionary but not list
def wiper():
    print ("\n"*100)
  
atuple = ("CBT", "Nuggets", "is", 1.0)
print type(atuple)
print type(atuple[3])
print atuple[2]
newt =  atuple[1:3]
print newt
print len(atuple)
print atuple.index("is")




#list [] mutable sequience
# can be modified dyncamically usind methods like append(),extend(),insert(),remove(), pop (), count(), sort()
wiper()  
alist = ["CBT", "Nuggets", "is", 1.0]
print type(alist)
blist = alist.append("added")
print alist
foo2 = alist[0:3]
foo2.remove("is")
print foo2
foo3 = tuple(foo2)
print foo3
print foo2.count("Nuggets")

a = foo2.insert(1,"khara")
print a
b = foo2.insert(10,"luitel")
print b
l1 = [1,3,4,5]
l2=['asdf','asdf','asdf']
l2.append(l1);
#alist.sort()
#alist.reverse

wiper() 



# distionary {} mutable  ; associated array OR Hash table
#key value pair ## no slicing allowed 
adict = {1:'jan',2:'feb',3:'mar'}
print type(adict)
print adict[2]
adict[4] = "apr"
print adict
print adict.keys()
print adict.values()
con = list(adict.values())
print con;
print type(con)
tup = ("asdf", "afds","3245")
adict[5]=tup
print adict;print len(adict)
aa = adict.pop('feb')
print aa


#print adict.key
# methos key(), items(), values(),pop(), clear()

# tuple as key because they are fixex and imutable but not a list as a key