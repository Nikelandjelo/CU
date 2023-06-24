#!/usr/bin/env python3 
import socket
import ssl
import threading
import os
import sys
from time import sleep


class Client():
    '''Client class managing the connection on the client-side,
    as well as running the tasks given by the controller.

    Funcs:
        __init__    :   Initialising the class with default values host, port and cert.
        start       :   Opens a secure socket and tries to connect to the server.
        run_command :   Once the server is connected the receiver can pass system commands which will be run from this function.
        disconnect  :   If the controller passes the command for disconnection, this function will make sure that the socket is closed appropriately.
        receive     :   Once the client has connected with the controller, this function listens for new commands.
    '''

    def __init__(self, host = '127.0.0.1', port = 9090, cert = './cert.pem'):
        self.host = host
        self.port = port
        self.cert = cert

    def start(self):
        '''Attempting to connect to a controller. Going through an infinite loop with an exception for
        ConnectionRefusedError and ConnectionResetError in case the controller is down.

        Return:
            client  :   An ssl class of the connection with the controller.
        '''

        while True:
            try:
                context = ssl.SSLContext() #Defaults to TLS 
                context.verify_mode = ssl.CERT_REQUIRED
                context.load_verify_locations(self.cert)
                client = socket.create_connection((self.host, self.port))

                #Create secure socket
                client=context.wrap_socket(client, server_hostname=self.host)
                return client

            except (ConnectionRefusedError, ConnectionResetError):
                pass


    def run_command(self, command):
        '''A function that runs past system commands.

        Args:
            command :   A command to run.

        Return:
            msg     :   A result message from the run command.
        '''

        msg = str(os.popen(command).read())
        return msg


    def disconnect(self, client):
        '''A function that disconnects the client from the controller. It stops for 0.5 seconds in order for the server to close the connection first,
        Then shutdowns and closes the socket.

        Args:
            client  :   A connected socket.
        '''

        sleep(0.5)
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        print("Disconnecting!")

    
    def receive(self, client):
        '''Listens for messages from the controller and do the appropriate actions for given messages.

        Args:
            client  :   A connected socket.
        '''
        print("Connected to server!")
        while True:
            try:
                # Receive message from controller
                message = client.recv(1024).decode('ascii')

                # Sending hostname
                if message == 'HOST':
                    client.send(socket.gethostname().encode('ascii'))

                # Sending result from list of commands
                elif message in ['ID', 'LS', 'PWD', 'IP']:
                    command = {'ID': 'id', 'LS': 'ls', 'PWD': 'pwd', 'IP': 'ip a'}
                    msg = self.run_command(command[message])
                    client.send(msg.encode('ascii'))

                # Disconnecting from controller
                elif message == 'DISSCL' or not len(message):
                    try:
                        self.disconnect(client)
                        break
                    except:
                        break

            except:
                self.disconnect(client)
                break


def start_client():
    '''Starts the client from the client class and passes it to a thread
    for the receiving function.
    '''

    while True:
        cl = Client().start()
        client_thread = threading.Thread(target=Client().receive, args=(cl,))
        client_thread.start()
        client_thread.join()
        print("-"*10)


if __name__ == '__main__':
    start_client()