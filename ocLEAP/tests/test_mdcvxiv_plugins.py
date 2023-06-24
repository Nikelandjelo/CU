""" Tests for SysServUNIX plugin """

import pytest
import sys
sys.path.append("./src/")
from mdcvxiv import *
import plugins

import os
import platform
import time

#Dependance and Automatization------------------------------------------
thisSys=platform.system() #Used as a global var

def ContentCheck(plug, command):
    content=plug.execute(out=True)
    cm=os.popen(command)
    com=''
    
    blackList=[
        "systeminfo",
        "ps -eF | grep root",
        "ps -eF",
        "netstat -antup",
        "grep -v -e '^$' /etc/sudoers |grep -v '#'",
        "ls -ahl /root/",
        "echo '' | sudo -S -l -k"
        ]
    if command in blackList:
        if command==blackList[0]:
            for i in range(15):
                com+=cm.readline()
        
        if command==blackList[1] or command==blackList[2]:
            com=cm.readline()

        if command==blackList[3] or command==blackList[4] or command==blackList[5] or command==blackList[6]:
            command=subprocess.Popen(command, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result, err = command.communicate()
            com=err.decode()

    else: com=cm.read()
    
    time.sleep(2) ##Sometimes the command requres time, often in Windows
    assert com in content

class plugin_simulator():
    def execute(self, **out):
        out=out.get("out", False)
        a="Test content"
        return a





#fileIn Test------------------------------------------
def test_fileIn():
    fileIn(plugin_simulator())
    File=None
    FileName=""
    if thisSys=="Windows":
        FileName="winLog.txt"
        assert open("winLog.txt", "r")
        File=open("winLog.txt", "r")

    else:
        FileName="unxLog.txt"
        assert open("unxLog.txt", "r")
        File=open("unxLog.txt", "r")

    assert plugin_simulator().execute(out=True)==File.read()
    File.close()
    os.remove(FileName)





#NoNinteractive Test------------------------------------------
def test_incorect():
    err=None
    if thisSys=="Windows": err=os.popen("python .\\src\\ocLE4P.py err")
    else: err=os.popen("python3 src/ocLE4P.py err")
    assert "Incorrect argument!" in err.read()

def test_numArgs():
    err=None
    if thisSys=="Windows": err=os.popen("python .\\src\\ocLE4P.py err err")
    else: err=os.popen("python3 src/ocLE4P.py err err")
    assert "Only one argument is required!" in err.read()

def test_help():
    h="-h"
    for i in range(2):
        err=None
        title="ocLE4P:"
        desc="""
            Custome python script for Local Enumeration and PrivEsc
            Running ocLE4P.py with no arguments will run the main menu with every option
            For NoNinteractive mod you can run:
            """
        hpMen="-h   /   --help               : Print this menu"

        opt={
        "--linux-enumeration":
        """
        Exexute every plugin in 'mdcvxiv.py' for Linux enumeration
        """,
        "--linux-service-enumeration":
        """
        Execute SysServUNIX plugin from 'mdcvxiv.py'.
        Plugin for local system services enumeration for Linux
        Shows the current user, the host info + desctop env.,
        running services, all services and the unit files.
        """,
        "--linux-pops-enumeration":
        """
        Gets root processes+ALL. Shows the open ports status.
        Reads the content of /etc/passwd and checks for any hashes in it.
        Search for any admin and root accounts. Trying to reed /etc/sudoers
        and /etc/shadow. Trying sudo without password.
        """,
        "--win-enumeration":
        """
        Exexute every plugin in 'mdcvxiv.py' for Windows enumeration
        """,
        "--win-service-enumeration":
        """
        Execute SysServWIN plugin from 'mdcvxiv.py'.
        Plugin for host info and host servces enumeration
        """
        }

        linEn, sysServUNIX, popsUNIX, winEn, sysServWIN=opt.items()

        if thisSys=="Windows": err=os.popen(f"python .\\src\\ocLE4P.py {h}")
        else: err=os.popen(f"python3 src/ocLE4P.py {h}")

        assert desc and desc and hpMen and linEn[0] and sysServUNIX[0] and popsUNIX[0] and winEn[0] and sysServWIN[0] in err.read()
        h="--help"

def test_options():
    err=None
    FileName=""
    if thisSys=="Windows":
        FileName="winLog.txt"
        err=os.popen("python .\\src\\ocLE4P.py --win-enumeration")
        time.sleep(6)
    else:
        FileName="unxLog.txt"
        err=os.popen("python3 src/ocLE4P.py --linux-enumeration")
        time.sleep(2)
    
    log=open(FileName, "r")
    assert log
    log.close()
    os.remove(FileName)





#TempFile Tests------------------------------------------

def test_gen():
    TempFile().gen()
    if thisSys=="Windows": path=os.listdir(".\\")
    else: path=os.listdir("./")
    assert "tmp.txt" in path
  
def test_rem():
    time.sleep(2)
    TempFile().rem()
    if thisSys=="Windows": path=os.listdir(".\\")
    else: path=os.listdir("./")
    assert "tmp.txt" not in path






########################################################################################################################
#                                                                                                                      #
#                                               Test_Plugins/Linux                                                     #
#                                                                                                                      #
#<--------------------------------------------------------------------------------------------------------------------->
if thisSys=="Linux":
    #<-----------------------------------------------Enumeration-------------------------------------------------------->
    #<-------------------------------------------Tests for all enumeration plugins-------------------------------------------------->
    @pytest.mark.parametrize(
        "plug",
        [
            SysServUNIX(),
            POPS_UNIX(),
        ])
    def test_enum_ClassRealtions_Info_UNIX(plug):
        assert isinstance(plug, plugins.Enumeration)
        assert isinstance(plug, plugins.Item)
        assert "Nick" in plug.info()
        content=plug.execute(out=True)
        assert len(content)!=0
    
    

    #SysServUNIX Tests------------------------------------------
    @pytest.mark.parametrize(
    "command",
    [
        "whoami",
        "hostnamectl",
        "echo $XDG_CURRENT_DESKTOP",
        "systemctl list-units --type=service --state=running",
        "systemctl list-units --type=service --all",
        "systemctl list-unit-files"
    ])
    def test_SysServUnix_content(command):
        ContentCheck(SysServUNIX(), command)
        time.sleep(1)




    #POPS_UNIX Tests------------------------------------------
    @pytest.mark.parametrize(
    "command",
    [
        "ps -eF | grep root",
        "ps -eF",
        "netstat -antup",
        "cat /etc/passwd",
        "grep -v '^[^:]*:[x]' /etc/passwd",
        'echo -e "$grpinfo" | grep "(adm)"',
        "grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0 { print $1}'",
        "grep -v -e '^$' /etc/sudoers |grep -v '#'",
        "ls -ahl /root/",
        "echo '' | sudo -S -l -k"
    ])
    def test_POPS_UNIX_content(command):
        ContentCheck(POPS_UNIX(), command)
        time.sleep(1)
    
    #<-------------------------------------------------PrivEsc----------------------------------------------------------->
    #<-------------------------------------------Tests for all privescs plugins-------------------------------------------------->
    @pytest.mark.parametrize(
        "plug",
        [
            vim_UNIX(),
            grepSHADOW()
        ])
    def test_privesc_ClassRealtions_Info_UNIX(plug):
        assert isinstance(plug, plugins.PrivEsc)
        assert isinstance(plug, plugins.Item)
        assert "Nick" in plug.info()
    
    
    
    @pytest.mark.parametrize(
    "b",
    [
        "vim",
        "grep"
    ])
    def test_SUID_check(b):
        grepOut=SUID_check(b)
        Out=os.popen("find / -perm -u=s -type f 2> /dev/null")
        Out=Out.read()
        for i in grepOut:
            assert i in Out
        time.sleep(1)








########################################################################################################################
#                                                                                                                      #
#                                              Test_Plugins/Windows                                                    #
#                                                                                                                      #
#<--------------------------------------------------------------------------------------------------------------------->
elif thisSys=="Windows":    
    #<-----------------------------------------------Enumeration-------------------------------------------------------->
    #<-------------------------------------------Tests for all enumerations plugins-------------------------------------------------->
    @pytest.mark.parametrize(
        "plug",
        [
            SysServWIN()
        ])
    def test_ClassRealtions_Info_WIN(plug):
        assert isinstance(plug, plugins.Enumeration)
        assert isinstance(plug, plugins.Item)
        assert "Nick" in plug.info()
        content=plug.execute(out=True)
        assert len(content)!=0
    
    
    
    #SysServWIN Tests------------------------------------------
    @pytest.mark.parametrize(
    "command",
    [
        "whoami",
        "systeminfo",
        "sc queryex type= service",
        "sc queryex type= service state= all",
        "sc queryex type= driver"
    ])
    def test_SysServWIN_content(command):
        ContentCheck(SysServWIN(), command)
        time.sleep(1)
    
    
    
    #<-------------------------------------------------PrivEsc----------------------------------------------------------->
    #<-------------------------------------------Tests for all privescs plugins-------------------------------------------------->
    #@pytest.mark.parametrize(
    #    "plug",
    #    [
    #        
    #    ])
    #def test_ClassRealtions_Info_WIN(plug):
    #    assert isinstance(plug, plugins.PrivEsc)
    #    assert isinstance(plug, plugins.Item)
    #    assert "Nick" in plug.info()