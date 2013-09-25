#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kluitel"
__date__ ="$Sep 24, 2013 8:33:23 PM$"

if __name__ == "__main__":
    print "Hello World";
    '''
     sqlite is directly transfarable to rdms like mysql or oracle or mssql
    
    Python DB API 2.0 is needed for connecting to rdms dbase
    Connectivity to:
        mysql for Python
        cx - Oracle
        adodbapi (mssql)
        PyGreSQL
    
    '''
## using already shiped sqlite3 accessed through db api 2.0
import os
import sqlite3
os.chdir("c:/Python27/sqlite3")
conn = sqlite3.connect("db_app1")
db_hdl = conn.cursor()
db_hdl.execute('''create table if not exists `users` 
(id int not null primary key, first_name varchar(50), last_name varchar(50), username varchar(50), password varchar(50), email varchar(50)) ''')
for i in range(10,100):
    db_hdl.execute("insert into users values ("+str(i)+",'khara','Luitel','kluitel','alyssa','kluitel@cisco.com') ");
for r in db_hdl.execute("select * from users "):
    print r;
db_hdl.execute("select * from users")
rows = db_hdl.fetchall()
for value in rows:
    print value
conn.close()