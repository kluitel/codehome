#! /usr/bin/python
## os.open is ths function for opening files

## 3 importnat muldes 1. os, 2. sys (path) 3. shutil (batch copy/removal etc)
import os
print os.getcwd()
#print os.chdir("c:/")
#print os.listdir()
print os.path.join('c:/','files')
a = os.listdir("C:\\Users\\kluitel\\Documents\\NetBeansProjects\\NewPythonProject\\src")
print(a)

print os.name
import sys
print sys.platform
#print dir(os)
items = list(os.environ.keys())
#for params in list(os.environ.keys())
import wiper
wiper.w()
cd =  os.getcwd()
print cd
print (os.listdir(os.curdir))

os.chdir("c:/")
print os.getcwd();
print (os.listdir(os.curdir))
os.chdir("C:\\Users\\kluitel\\Documents\\NetBeansProjects\\NewPythonProject\\src")
#os.remane("oldfile.txt","name.txt")
wiper.w()
print os.getcwd()
#os.mkdir('morefiles')
#os.mkdir('deleteme')
print os.listdir(os.getcwd())
#os.rmdir('deleteme')
#os.remove("khara.txt")

############################
##
## Files are in here
##
############################
wiper.w()
mf = open('C:\\Users\\kluitel\\Documents\\NetBeansProjects\\NewPythonProject\\src\\khara.txt','w')
mf.write("First line\n") ## one line at a time
mf.write("second line\n")
mf.write("Third lin\n")
mf.write("Fouth line\n")
# list as a parameters
mf.writelines('asdf sdfasdf\n')
mf.close()
f = open("khara.txt")
print f.readline();
print f.readline(); # only one line at a time in a file
print f.readlines() 
#mf.readlines() # entire file but outputs one line into list of string per line
f.seek(0) # put the file pointer to top of the file
print f.read() # entire file at a time and output in one string
f.close()
g = open("khara.txt",'a')
g.write('''
jati lekhar ni hunchha
asdfasdf  asdfasfd
asdf
 34735b3reyberybe fthd
 asdf
 asfd asfdasfd alskfdh 
 dsaffdsa
''')
g.close()
namelist = ['tim','susan','zzoey']
f = open('khara.txt','a')
f.writelines(namelist)
f.seek(0)
f.close()
wiper.w()
for line in open("khara.txt").readlines():
    print(line);
   
    
#print f.read()

## must best way is iterator as content of the files