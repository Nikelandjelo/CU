#!/usr/bin/env python3 
import socket
import ssl
import sys
import threading
from queue import Queue

class Server():
    '''Server class managing the connection on the controller-side.

    Funcs:
        __init__    :   Initialising the class with default values port and cert, key, password, and clients.
        start       :   Opens a secure socket and starts listenning for new connections.
        broadcast   :   Sends a message to all clients
        close_srv   :   Disconnects all clients and stops the server
        close_con   :   Disconnects a client
        rm_client   :   Based on a argument send, it uses close_con to disconnect a single client, or all of them
        handle      :   Handles the result from the client
        receive     :   Accepts new connection trying to connect to the server
        client_ls   :   Returns a dictinary of all clients
        read_data   :   Reads the data from the handler
        API         :   Sends commands to the client
    '''

    def __init__(self, port=9090, cert="./cert.pem", key="./key.pem", paswd="bleh", clients={}):
        self.port = port
        self.cert = cert
        self.key = key
        self.paswd = paswd
        self.clients = clients


    def start(self):
        #Needs cert and key generated:
        #openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
        try:
            context = ssl.SSLContext()
            context.load_cert_chain(certfile=self.cert, keyfile=self.key, password=self.paswd)
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.settimeout(10)
            self.server.bind(('127.0.0.1', self.port))
            self.server.listen()
            self.server = context.wrap_socket(self.server, server_side=True)
            print("[LOG]: Server is starting...")
            return self.server

        except OSError:
            print("[ERR]: SERVER IS BUSY!")
            return ''
    

    # Sending Messages To All Connected Clients
    def broadcast(self, message):
        for client in self.clients:
            client = self.clients[client][1]
            message = f"{message}"
            client.send((message.encode('ascii')))


    def close_srv(self, server):
        try:
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            print("[LOG]: Server is stopping...")
        except AttributeError:
            print("[ERR]: Server can't be stopped!")
    

    def close_con(self, index):
        self.clients[index][1].shutdown(socket.SHUT_RDWR)
        self.clients[index][1].close()
        print(f'[LOG]: {self.clients[index][0]} disconnected!')


    def rm_client(self, index):
        if index == "ALL":
            for i in self.clients:
                self.close_con(i)
            self.clients.clear()

        else:
            self.close_con(index)
            del self.clients[index]


    # Handling Messages From Clients
    def handle(self, index, client, data):
        while True:
            try:
                client[1].settimeout(100)
                data.put(client[1].recv(1024).decode('ascii'))

                # Removes client from the list if the client is dead
                if data.queue[0] == "":
                    data.get()
                    self.rm_client(index)
                    break

            except:
                #self.rm_client(index)
                break
    

    # Receiving / Listening Function
    def receive(self, server, data):
        try:
            # Accept Connection
            client, address = server.accept()
            print(f"[LOG]: Connected with {(str(address))}")

            # Request And Store Nickname
            client.send('HOST'.encode('ascii'))
            hostname = client.recv(1024).decode('ascii')

            # Print And Broadcast Hostnames
            print("[LOG]: Hostname is {}".format(hostname))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            index = len(self.clients)+1
            self.clients |= {index: (hostname, client)}
            self.handle(index, self.clients[index], data)

        except socket.timeout:
            print("[ERR]: Timeout | No connected client")

    def client_ls(self):
        return self.clients
    
    def read_data(self ,data):
        if data.empty() is False:
            while True:
                print(data.get())
                if data.empty() is True:
                    break
        else:
            print("[LOG]: No data has been received!")
    

    def API(self, q="", data="", destination=""):
        while True:
            message=""
            if q.empty() is True: pass
                #msg = input("# ")
                #message = q.put(msg)
            else: message = q.get()
            

            if message == "CONS":
                print("-"*10)
                for i in self.clients:
                    print(f"[CON]: {i}: {self.clients[i][0]}")
                print("-"*10)

            elif message == "KILLSURV":
                client = "ALL"
                if destination == "":
                    print("[ERR]: Missing a Server object")
                else:
                    d = destination.get()
                    self.rm_client(client)
                    self.close_srv(d)
                    #break

            elif message == "DISSCL":
                if destination == "":
                    print("[ERR]: No client specified!")
                else:
                    d = destination.get()
                    if d == "ALL":
                        self.broadcast(message)
                        self.rm_client(d)
                    else:
                        d[1].send(message.encode('ascii'))
                        self.rm_client(d[0])

            elif message == "NEWCL":
                if data == "" or destination == "":
                    print("[ERR]: Missing a Queue object")
                else:
                    d = destination.get()
                    print("[LOG]: Listening for a new connection...")
                    listen_thread = threading.Thread(target=self.receive, args=(d, data))
                    listen_thread.start()
            
            elif message in ["ID", "LS", "PWD", "IP"]:
                if destination == "":
                    print("[ERR]: No client specified!")
                else:
                    d = destination.get()
                    if d == "ALL":
                        self.broadcast(message)
                    else:
                        d[1].send(message.encode('ascii'))

            elif message == "READD":
                if data.empty() is False:
                    print(data.get())
                else:
                    print("No data!")
            
            elif message == "EXIT":
                break
            
            elif message == "":
                pass

            else:
                print("[DEBUG]: Unknown message passed to the API!")

            



if __name__ == '__main__':
    server = Server().start()

    data = Queue()
    message = Queue()
    destination = Queue()
    API_thread = threading.Thread(target=Server().API, name="API", args=(message, data, destination))
    API_thread.start()