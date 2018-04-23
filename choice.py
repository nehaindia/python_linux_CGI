#!/usr/bin/python

import commands
import cgi,time

print "Content-Type: text/html"
print ""

data=cgi.FieldStorage()

command=data.getvalue('c')

if command == "user":
	print "<a href ='http://192.168.10.128/choice1_user.html'>"
	print "click here to go"
	print "</a>"

elif command == "file":
        print "<a href ='http://192.168.10.128/choice2_file.html'>"
	print "click here to go"
	print "</a>"

elif command == "storage":
	print "<a href ='http://192.168.10.128/choice3_storage.html'>"
	print "click here to go"
	print "</a>"
