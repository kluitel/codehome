##! /usr/bin/python
import os
 # recursive dir structuresa
import glob 
#glob.glob(pattern, exclude); # wildcard processsing like "*.txt"
#pickle modules: dump and load
#a = ['wre',2431,'test',23.324]
#import pickle
#f = open('c:/files/pick.txt','wb')
#pickle.dump(a,f)
#f.close()
#f2 = open('c:/files/pic.txt','r')
#a = pickle.load(f2)#
#f2.close()
print os.getcwd()
for root, dirs, files in os.walk(os.curdir):
    print('{0} has {1} files and {2} sub-folders'.format(root, len(files), len(dirs)))

import wiper
wiper.w()

for files in glob.glob(os.curdir + "/*.py"):
    print files
    