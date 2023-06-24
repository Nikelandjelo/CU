#! /usr/bin/env python
import subprocess
import os
from plugins import Enumeration
#this will import the dircetions which is need for this python code to work
class Enum2(Enumeration):
    def __init__(self):
        Enumeration.__init__(self)
        self.name = "Enum2"
        self.author = "Kieran McGill"
        self.description = "Prints information about the users and the groups"
    def execute(self):
        '''This the secound tool for the enumation and this will output about the users and the groups that their are in'''
        
        #temp runs two linux comminds in the commind line
        temp = subprocess.Popen(['cat','/etc/group'], stdout = subprocess.PIPE)
        output = str(temp.communicate())
        Enum2().soutput(output)
        temp2 = subprocess.Popen(['lslogins'], stdout = subprocess.PIPE)
        output2 = str(temp2.communicate())
        Enum2().soutput(output2)
    def soutput(self,data):
        num = str(data)
        num = num.split("\n")
        num = num[0].split('\\')
        newlist = []
        for line in num:
            newlist.append(line)
            next
        for i in range(1,len(newlist)-1):
            print(newlist[i])
            next
        return()
class Enum1(Enumeration):
    def __init__(self):
        Enumeration.__init__(self)
        self.name = "Enum1"
        self.author = "Kieran McGill"
        self.description = "Prints information about software"
    def execute(self):
        ''' this first tool will output all about the system for the user'''
        output = os.uname()
        print(output)
        print("\n")
        temp = subprocess.Popen(['lscpu'], stdout = subprocess.PIPE)
        output2 = str(temp.communicate())
        Enum1().soutput(output2)
        print("\n")
        return ()
    def soutput(self,data):
        num = str(data)
        num = str(num).split("\n")
        num = str(num).split("\\\\n")
        newlist = []
        for line in num:
            newlist.append(line)
            next
        for i in range(1,(len(newlist)-1)):
            print(newlist[i])
            next
        return()
