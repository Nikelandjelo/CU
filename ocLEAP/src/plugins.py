""" Template classes for plugins and useful functions """

#import pty



    
## A couple of optional super classes and a general item class to represent them more abstractly
## Can be used to add common functionality to privesc/enumeration plugins

class Item:
    """A generic privelege escalation/enumeration class. Include common
    functionality here"""
    def __init__(self):
        self.name="No Name"
        self.author="Anonymous"
        self.description="Your description"
        self.version="0.0"
    
    def execute(self):
        """Execute the privelege escalation/enumeration, dropping the user
        into a shell or displaying collected info.
        """
        print("This should be overridden in your plugin")

    def info(self):
        """Return useful information on the plugin, suitable for the user to
        read"""
        return f"{self.name}: {self.version}, by {self.author}.\n{self.description}"

class PrivEsc(Item):
    def info(self):
        return "PRIVESC: "+Item.info(self)
    
class Enumeration(Item):
    def info(self):
        return "ENUMERATION: "+Item.info(self)
