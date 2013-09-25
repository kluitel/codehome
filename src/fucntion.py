#! /usr/bin/python
'''
If nothing is rettunrd ........ then none is retunr by default

single-value returnf
retun x


multiple-value return -> tuple
return x,y
'''
def uc(a):
    if type(a) == int:
        print "This is interger"
    elif type(a) == str:
        print "this is string"
uc('khara')
uc(2)

def fun(name,location,year=2012):
    dd = "%s/%s/%d" % (name,location,year)
    print dd
    return dd


fun(location='LA',name="khara")
