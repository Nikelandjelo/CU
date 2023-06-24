#!/usr/bin/env python3
#import socket
#import ssl
#import sys
#import threading
#from queue import Queue
from server import *
from time import sleep
from simple_term_menu import TerminalMenu

# Quits the program.
def quit():
    print("[LOG]: Quitting...")
    sys.exit(0)

# Gets all the clients listed on the server and returns them in appropriate format
def cl_list():
    options=[]
    ls = Server().client_ls()
    for i in ls:
        options.append((f"[{i}] {ls[i][0]}", i, ls[i][1]))
    return options


def menu(q_data, q_msg, q_dest):
    # Menu layout
    options = [("[s] Start server",),
        ("[a] Add new client",),
        ("[l] List connected clients",),
        ("[i] Run `id`", "ID"),
        ("[p] Run `ls`", "LS"),
        ("[p] Run `pwd`", "PWD"),
        ("[p] Run `ip a`", "IP"),
        ("[d] Disconnect client", "DISSCL"),
        ("[b] Set broadcast ON/OFF",),
        ("[k] Stop server",),
        ("[q] Quit",)]


    tm = TerminalMenu([i[0] for i in options])
 
    server=""
    broadcast=False
    while True:
        
        menuIndex = tm.show()
        
        # Option for starting the server
        if menuIndex==0:
            if server != "":
                print("[INFO]: Server is already running!")
            else:
                server = Server().start()

        # Adding a new client option
        elif menuIndex==1:
            if server != "":
                q_dest.put(server)
                q_msg.put("NEWCL")
            else: print("[INFO]: Server is not running!")

        # Option for listing all connected clients
        elif menuIndex==2:
            if server != "":
                q_msg.put("CONS")
            else: print("[INFO]: Server is not running!")

        # API commands option
        elif menuIndex in [3, 4, 5, 6, 7]:
            log = {3: "Running `id` on",
                4: "Running `ls` on",
                5: "Running `pwd` on",
                6: "Running `ip a` on",
                7: "Disconnecting from"}

            # Submenu for all clients (not displaied in case the broadcast is on)
            if server != "":
                if broadcast == False:
                    opt = cl_list()
                    si = TerminalMenu([i[0] for i in opt])
                    subIndex = si.show()
                    if subIndex!=None:
                        print(f"[LOG]: {log[menuIndex]} {opt[subIndex][0]}")
                        q_dest.put((opt[subIndex][1], opt[subIndex][2]))
                        q_msg.put(options[menuIndex][1])
                        sleep(0.1)
                        Server().read_data(q_data)
                elif broadcast == True:
                    print(f"[LOG]: {log[menuIndex]} all clients")
                    q_dest.put("ALL")
                    q_msg.put(options[menuIndex][1])
                    sleep(0.1)
                    Server().read_data(q_data)

            else: print("[INFO]: Server is not running!")

        # Broadcast option (sets a variable to True or False in order to turn ON or OFF the broadcast)
        elif menuIndex == 8:
            if broadcast == False:
                broadcast = True
                br = "ON"
            elif broadcast == True:
                broadcast = False
                br = "OFF"
            print(f"[LOG]: Broadcast is {br}")

        # Stop server option
        elif menuIndex == 9:
            if server != "":
                q_dest.put(server)
                q_msg.put("KILLSURV")
                server=""
            else: print("[INFO]: Server is not running!")

        # Exit option
        elif menuIndex==10:
            if server != "":
                q_dest.put(server)
                q_msg.put("KILLSURV")
                server=""
            q_msg.put("EXIT")
            quit()

# Creates the required queues, starts an API thread and runs the menu
def menu_main():
    q_data, q_msg, q_dest = Queue(), Queue(), Queue()
    API_thread = threading.Thread(target=Server().API, name="API", args=(q_msg, q_data, q_dest))
    API_thread.start()

    menu(q_data, q_msg, q_dest)


if __name__ == '__main__':
    menu_main()