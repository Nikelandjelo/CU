#!python3 
import pty
import os #used to automate linux commands within python files
from plugins import Enumeration #using generic class from plugins file
class NetworkEnumeration(Enumeration): #using generic enumeration class for specific enumeration class
	def __init__(self): #constructor to initialise class
		Enumeration.__init__(self)
		self.name="Network Enumeration" #overriding generic info from enumeration class and replacing with meaningful info
		self.author="Joe Conteh"
		self.description="Provides the user with the network configuration display information and cpu architecture"
		self.version="0.1 alpha"
	
	
	def execute(self): # when called on, displays info contained in function
		cpu=os.system("lscpu") #provides cpu architecture
		network=os.system("ifconfig") #provides network configuration
	