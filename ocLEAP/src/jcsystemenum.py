#!python3
import pty
import os
from plugins import Enumeration
class SystemEnumeration(Enumeration):
	def __init__(self):
		Enumeration.__init__(self)
		self.name="System Enumeration"
		self.author="Joe Conteh"
		self.description="Provides the user with the system information and hostname"
		self.version="0.1 alpha"
		
	def execute(self):
		os.system("uname -a")
		os.system("hostname")

