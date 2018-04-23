#!/usr/bin/python

import commands
import cgi,time

print "Content-Type: text/html"
print ""

data=cgi.FieldStorage()

command=data.getvalue('c')

if command == "ausers":
	print"executing..."
	time.sleep(2)
	print "<pre>"
	print commands.getoutput('compgen -u')
	print "</pre>"


elif command == "eusers":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('w')
	print "</pre>"

elif command == "suser":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('su - nikhil')
        print "</pre>"

elif command == "cpasswor":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('passwd')
        print "</pre>"





