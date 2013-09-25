import getpass 
import sys 
import telnetlib 

HOST = '10.193.183.222'  # this is the hostname for device, to be changed
#to read from file when figure that out 
user = raw_input('Username: ') 
#password = getpass.getpass()
password = 'nbv12345'

tn = telnetlib.Telnet(HOST) #make less typing for me 

tn.read_until('login: ') #expected prompt after telnetting to the router 
tn.write(user + '\r\n')  #hopefully write username and pass character return 

raw_input('ENTER to continue') # just to see if it makes this far 

# this is where the program appears to hang 

tn.read_until('Password: ') #expected prompt after putting in the username 
tn.write(password + '\r\n') 

tn.read_until("#") #expected prompt is "hostname>" 

tn.write('sh int status\n') #run this command, read this from file when i figure out how 

tn.read_until('#') #prompt once above command has finished running, useful when reading multiple commands 

tn.write('exit\n') #disconnect from the session 

print tn.read_all() #prints out something, maybe needs to be prior to "exit" command 

tn.close() 