""" Template file for crating a plugins """

from plugins import PrivEsc, Enumeration





class Escalation(PrivEsc):
    """
    Template for PrivEsc plugin
    """
    def __init__(self):
        PrivEsc.__init__(self)
        self.name="Name of the metod"
        self.author="Authors name"
        self.description="Description of the method"
        self.version="0.0"

    def execute(self):
        print("Executing")
        #Code for executing the method
        print("Done")

class Enum(Enumeration):
    """
    Template for local enumeration plugin
    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="Name of the metod"
        self.author="Authors name"
        self.description="Description of the method"
        self.version="0.0"

    def execute(self):
        print("Executing")
        #Code for executing the method
        print("Done")
