import socket
import select
import time

def checkStatus(sock):
    """ Return the number of bytes ready to be read from a socket

    Args:
      sock (socket): the socket to test for data

    Returns:
      int: the number of bytes ready to be read.
    """
    ready_to_read, ready_to_write, in_error = select.select([sock,], [sock,], [], 5)
    return len(ready_to_read)

def testPort(host:str,portnum:int, poke=None):
    """Given a host (IP or name) and a port number, connect if possible and return any data transmitted.
    
    Args:
      host (string): the host to scan. Can be an IP address or hostname
      portnum (int): the port number, between 0 and 65535
      poke (string): if given, the string to send to the server upon connection.

    Returns:
      list of strings or None: the data returned by the connection, or None if the connection failed. If a list is returned, it represents the sequence of responses. The first element is the reponse recieved immediately, the second is the response after sending any given data.
    """
    response=[]

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, portnum))
        if result == 0: #0 means no error
            time.sleep(0.1) #Give the server time to send
            if checkStatus(sock)>0:
                rcv = sock.recv(1024)
                response.append(rcv.decode("utf-8", "ignore"))
            if poke!=None:
                sock.sendall(str.encode(poke))
                time.sleep(1) #Give the server time to send
                ready_to_read, ready_to_write, in_error = select.select([sock,], [sock,], [], 5)
                if checkStatus(sock)>0:
                    rcv = sock.recv(1024)
                    response.append(rcv.decode("utf-8", "ignore"))

            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

            return response
        else:
            return None
    except socket.error:
        return None if response is [] else response
    return None
