#!python
"""Simple program for scanning ports on a given host and acting on results"""

from h_sockets import testPort
import socket
import colored
import argparse
from os import system
import ipaddress


#Arguments input
def ARGS():
    parser = argparse.ArgumentParser(description="Simple program for scanning ports on a given host and acting on results")
    parser.add_argument('IP', metavar='255.255.255.255', type=str, nargs='+')
    args = parser.parse_args()
    arguments=args.IP

    #Chech the input data if it's correct IP or port
    for target in arguments:
        socket.inet_aton(target)

    return arguments


#Valid tarrget IP checker
def ipCheck(trgIP):
    if ipaddress.ip_address(trgIP) is False: print('Error')



if __name__=="__main__":
    args=ARGS()
    openPorts=[]
    print("Scanning:" + ' '.join(args))

    #Loop for scanning every inputed IP
    for target in args:
        ipCheck(target)
        print('\n',"Scanning ", target)
        print('\n',"Scanning ports 0 to 99:",'\n')

        for p in range(1,100):
            message=colored.fg("red")+"Closed"
            result=testPort(target,p)

            if not result is None:
                message=colored.fg("green")+"Open"
                openPorts.append(p)

                if len(result)>0:
                    message+=colored.fg("yellow")
                    message+=" - Data recieved"

                    for i in result:
                        message+="\n"+i

                message+="\n"
                
            message+=colored.attr('reset')
            print(f"{p}: {message}")
        
    
        print('\n\n',"Scanning for WYDAH:", '\n')
        for p in [37000, 37102, 37204, 37306, 37408, 37510, 37612, 37714, 37816]:
            message=colored.fg("red")+"Closed"
            result=testPort(target,p)
        
            if not result is None:
                openPorts.append(p)

                #WYNDAH checker
                if len(result)>0 and result[0]=='57 65 6c 63 6f 6d 65 20 74 6f 20 57 79 64 61 68':
                    message=colored.fg("green")+"WYDAH MALWARE DETECTED"
                
                else:
                    message=colored.fg("yellow")+"Open: non-wydah"
            
                for i in result:
                    message+="\n"+i
                
                message+="\n"
            
            message+=colored.attr('reset')
            print(f"{p}: {message}")


        if len(openPorts)>0:
            print(f"\nTarget:{target}\nPort/s", *openPorts, "is/are open, do you want to scann for raspond?(y/n):")
            resp=input()
            print('\n')

            if resp.strip().upper()=='Y' or resp.strip().upper()=='YES':
                for port in openPorts:
                        system(f'python3 webscan.py {target} {port}')

        openPorts=[]