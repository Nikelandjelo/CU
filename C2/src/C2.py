#!/bin/python3
#!/usr/bin/env python3
#import socket
#import ssl
#import sys
#import threading
#from queue import Queue
#from server import *
#from time import sleep
#from simple_term_menu import TerminalMenu
#import PySimpleGUI as sg
import sys
from menu import *
from gui import *

def arg_choose():
    USAGE="""Usage: C2.py <arg>

-h  --help      :   Prints this message
-g  --gui       :   Runs C2 with a pretty GUI
-c  --console   :   Runs C2 with a pretty commandline based menu
"""

    try:
        argv = sys.argv[1]
      
    except:
        print("ERROR!")
        print(USAGE)
        sys.exit(2)
    
    if argv == '-h' or argv == "--help": print(USAGE)
    elif argv == '-g' or argv == "--gui": gui_main()
    elif argv == '-c' or argv == "--console": menu_main()
    else: print(USAGE)

if __name__ == '__main__':
    arg_choose()