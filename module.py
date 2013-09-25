#! /usr/bin/python
'''
Mdules
has - classes, f(x) and variables
benefits -  code reuse, shared components, avoiding name collisions

notes:
import modules run on 1st import so may have prints out etc - fix __main__ tricks
compiled pythin code can be imported and are fast extension = .pyc (bytecode)

2 ways to import
1. import os => a) all lib imported and b) call by os.Telnet(host)
2. from os import telnetlib => a) only telnetlib in impoted b) direct call of f(x) like Telnet(host)

'''
#! /usr/bin/python

__author__="kluitel"
__date__ ="$Sep 23, 2013 8:03:37 PM$"

if __name__ == "__main__":
    print "Hello World";
else:
    print "this is not displayed"
import imp
imp.reload(module1)
## start live
'''

import sys
dir(sys)
sys.platform;

from os import chdir
chdir("c:/files")
getcwd();# fails because only chdir is imported

# reloading the modules in python shell
import imp
imp.reload('module_name')
    list (append. remove)
    
.pth file 
    install dir
    site-package
    


module search path
ORDER:
1) PYTHON PATH
2) SYS PATH => import sys .. sys.path .. to add sys.path.append("c:/khara")  ..  now i can put modules files in c:/khara and import them in pythin script .. 
    but scope is only valid till it run .. closed finished
3).PTH PATH

sys.path (envirn vriable path)

'''



