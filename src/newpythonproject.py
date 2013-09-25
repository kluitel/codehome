# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kluitel"
__date__ ="$Sep 19, 2013 3:00:56 PM$"

#if __name__ == "__main__":
#    print "Hello World"
import telnetlib
print("asdf")
tn = telnetlib.Telnet("10.193.183.222") 

tn.write("admin") 
#tn.write("nbv12345\n")
#print tn.read_all()
