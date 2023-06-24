#!python
"""A simple scanner for HTTP/S servers and WYDAH malware"""

from h_sockets import testPort
import colored
from colored import stylize
import harbourmaster
import time

if __name__=="__main__":
    inPut=harbourmaster.ARGS()
    target=inPut[0]
    harbourmaster.ipCheck(target)

    #Valid input check
    if len(inPut)<=1: print(stylize('Enter the ports after the target IP\nEX: 255.255.255.255 portNum1 portNum2 ...',colored.fg('red')))
    
    #Loop for every port
    for p in inPut[1:]:
        print(f'Scanning: {target} {p}\n')
        message=colored.fg("red")+"Closed"
        flag=''
        #log file generated for every port
        logFile=open(f'./logs/{time.ctime()}-{target}:{p}.log', 'w+')

        #If any of WYNDAH's ports is open 'SHADOW' and 'GET /index.html' are executed on thath port
        if int(p) in [37000, 37102, 37204, 37306, 37408, 37510, 37612, 37714, 37816]:
            result=testPort(target,int(p), poke="SHADOW\r\n\r\n")
            #Looks like James loves hidden messages :D
            flag=testPort(target,int(p), poke="GET")

        #If http/80 or https/443 are open, 'GET /index.html' is executed
        elif int(p) in [80, 443]: result=testPort(target,int(p), poke="GET /index.html HTTP/1.0\r\n\r\n")
        #Else, just target port info is taken
        else: result=testPort(target,int(p))

        if not result is None:
            message=colored.fg("green")+"Open"

            if len(result)>0:
                message+=colored.fg("yellow")
                message+=f": (response follows)\n"
                response=""

                for i in result:
                    response+=colored.fg("green")+i+"\n"
                    logFile.write(response)

                if len(response)>1000:
                    #Trim it down if it's too long
                    response=response[:maxResponse]

                message+=response

        message+=colored.attr("reset")
        print(f"{p}: {message}\n\n")

        #Flag output
        if flag!='':
            print(stylize(f"Flag: {' / '.join(flag)}",colored.fg('red')))
            logFile.write('Flag: ')

            for c in flag:
                logFile.write(c)

        logFile.close()
        print(stylize('\nTHIS INFO IS WRITTEN IN .log FILES INTO ./logs/!\n', colored.fg('blue')))
