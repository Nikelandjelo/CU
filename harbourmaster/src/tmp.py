#!python
"""Simple program for scanning ports on a given host and acting on results"""

from h_sockets import testPort
import colored

if __name__=="__main__":
    target="172.17.0.2"

    for p in range(1,100):
        message=colored.fg("red")+"Closed"
        
        result=testPort(target,p)
        if not result is None:
            message=colored.fg("green")+"Open"
            if len(result)>0:
                message+=colored.fg("yellow")
                message+=" - Data recieved"
                for i in result:
                    message+="\n"+i
                message+="\n"
        message+=colored.attr('reset')
        print(f"{p}: {message}")
        
              
