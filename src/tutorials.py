#! /usr/bin/python
#data type
#tuple,list,disctpory
#distionary is key value pair
#math modules fraction and math - NumPy and SinPY
div = 6/8;
print isinstance(div,int)
''' this is multiple fi;les 
sadf kj dsafkja h
asdf ;lhasfdkja hsf
'''

#string operation
s = 'asdfafds'
print len(s)

#+ is overloaded adds string and numbers 
# s*5 repetation
i = 19
a = str(i) # type casting
#print (a+10) # error
n = "cisco "
print n*5
################
# string slicing
st = "CBT Nuggets"
print st[4]; 
print st[-6]
print st[6:10]
print st[-11:-7]; print st[0:3]
print st[4:]
##############
#string method
print st.find('ugg') ; # gives offset id
print st.replace('ugg','UGGs')
exp = st.split(" ") ; # the result is list
print exp[0];
print st.upper()
print st.lower()
###############
## you user input
ui = input("Enter a number: ")
print "Original  "; print type(ui)
uconv = int(ui)
print ("New aftetr conversion: ", (type(uconv)))

power =  (uconv ** 8)
print (ui, "raised poer 8 = ", power)
############ data type advance



