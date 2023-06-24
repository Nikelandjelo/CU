#! /usr/bin/env python
import subprocess
import os
from plugins import Enumeration
class Shadow(Enumeration):
     def __init__(self):
        Enumeration.__init__(self)
        self.name = "Shadow"
        self.author = "Kieran McGill"
        self.description = "Changes user primary group to shadow"
     def soutput(self):
        ''' open the file shadow and then prints line by line of the contents of shadow'''
        temp = subprocess.Popen(['cat','/etc/shadow'], stdout = subprocess.PIPE)
        output = str(temp.communicate())
        num = output
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
     def execute(self):
        ''' changes the user primiler group to shadow which then will allow the user to read the contents of restaried file'''
        temp2 = subprocess.Popen(['sudo','adduser','student','shadow'],stdout = subprocess.PIPE)
        output = str(temp2.communicate())
        print(output)
        temp3 = subprocess.run(['newgrp','shadow'])
        print("your user can read shadow")
        for i in range(2):
            print("\n")
        answer = input("would you like to see the contents of shadow")
        if answer == "yes":
           Shadow().soutput()
