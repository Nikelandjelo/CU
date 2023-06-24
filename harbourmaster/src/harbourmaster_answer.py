#!python
"""Simple program for scanning ports on a given host and acting on results"""

from h_sockets import testPort
import colored

if __name__=="__main__":
    target="172.17.0.2"

    for p in [x for x in range(1,100)]+[37000, 37102, 37204, 37306, 37408, 37510, 37612, 37714, 37816]:
        message=colored.fg("red")+"Closed"
        found=False
        result=testPort(target,p)
        if not result is None:
            found=True
            if len(result)>0 and result[0]=="57 65 6c 63 6f 6d 65 20 74 6f 20 57 79 64 61 68":
                message=colored.fg("green")+"WYDAH MALWARE DETECTED"
            else:
                message=colored.fg("yellow")+"Open: non-Wydah"
            
            message+=colored.attr('reset')

            if len(result)>0:
                #Add a few characters from anything returned
                lenSample=10
                data=result[0].strip()

                # if len(data)>lenSample:
                #     data=data[:lenSample]+"..."
                message+=f" ({colored.fg('blue')+data+colored.attr('reset')})"
        message+=colored.attr('reset')
        if found:
            print(f"{p}: {message}")
        
              
