#!/usr/bin/env python3

from os import system
import platform
import sys

#Windows plugins
if platform.system()=="Windows":
    from mdcvxiv import *
    #from YOUR_PLUGINFILE import YOUR_PLUGINS

#Linux, BSID and Mac plugins
else:
    from mdcvxiv import *
    from kmPullings import Enum1, Enum2
    from kmprivage import Shadow
    from ja_plugins import WritableScripts        
    from ja_plugins import BasicHostInfo
    from ja_plugins import BasicNetworkInfo
    from ja_plugins import SudoRights
    from jcprivesc import PrivilegeEsc
    from jcsystemenum import SystemEnumeration
    from jcnetworkenum import NetworkEnumeration

    #from YOUR_PLUGINFILE import YOUR_PLUGINS




if len(sys.argv)>1:
    NoNinteractive(sys.argv[1:])


else:

    #Windows plugins
    if platform.system()=="Windows":
        #Make a list of available privescs
        ESCAL=[]
        #ESCAL.append(YOUR_PLUGIN)
        
        #Make a list of available enumerations
        ENUM=[]
        ENUM.append(SysServWIN())
        #ENUM.append(YOUR_PLUGIN)
    
    #Linux, BSID and Mac plugins
    else:
        #Make a list of available privescs
        ESCAL=[]
        ESCAL.append(vim_UNIX())
        ESCAL.append(grepSHADOW())
        ESCAL.append(Shadow())
        ESCAL.append(SudoRights())
        ESCAL.append(PrivilegeEsc())
        #ESCAL.append(YOUR_PLUGIN)

        #Make a list of available enumerations
        ENUM=[]
        ENUM.append(SysServUNIX())
        ENUM.append(POPS_UNIX())
        ENUM.append(Enum1())
        ENUM.append(Enum2())
        ENUM.append(BasicHostInfo())
        ENUM.append(BasicNetworkInfo())
        ENUM.append(WritableScripts())
        ENUM.append(SystemEnumeration())
        ENUM.append(NetworkEnumeration())
        #ENUM.append(YOUR_PLUGIN)
    

    
    quIt=False
    thisSystem=platform.system()

    #Menu
    while quIt==False:
        if thisSystem=="Windows":
            system("cls")
        else:
            system("clear")
        print("""\033[0;36m
                        ___
                     .-'   `'.
                    /         \\
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  ""'--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
          / /\         `) )    / / `"".`\\
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
        """)
        print(f"\033[3;32m \t\t\tYou are running {thisSystem}\033[0m\n\n")

        print(f"\033[1;34mSo, what are we doing today?\033[0m\n")
        print("\t\033[0;32m1: Privilege Escalation")
        print("\t\033[0;32m2: Local Enumeration")
        print("\n\t\033[0;31mq to quit")

        usrInput=input("\n\033[1;36mSoo?...: ")
        print("\033[0m")
        if usrInput.upper().strip()=='Q':
            quIt=True

        #PrivEsc option
        elif usrInput=='1':
            print("""\033[0;36m
                 ____       _       _____
                |  _ \ _ __(___   _| ____|___  ___
                | |_) | '__| \ \ / |  _| / __|/ __|
                |  __/| |  | |\ V /| |___\__ | (__
                |_|   |_|  |_| \_/ |_____|___/\___|
                """)
            index=[]
            for i in range(len(ESCAL)):
                try: print(f"\n\033[1;32m{i}: {ESCAL[i].name}")
                except AttributeError: print(f"\n\033[1;32m{i}: {ESCAL[i]}(No name)")
                index.append(str(i))

            print("\n\033[0;31mback to get back to the main menu")
            usrInput=input("\n\033[1;36mSoo?...: ")
            print("\033[0m")

            if usrInput.upper().strip()=='BACK':
                continue

            elif usrInput in index:
                chosen=ESCAL[int(usrInput)]
                try: print(f"\n\033[1;32m{chosen.info()}")
                except AttributeError: print(f"\n\033[1;32mNo Info about the plugin")
                yesno=input("\nEnter YES in capitals to execute...\033[0m")
                if yesno.strip().upper()=="YES":
                    try: chosen.execute()
                    except: print("ERROR: Something went wrong!")
                    input("")

            else:
                print("\n\033[1;31mUnknown command!")
                input("Press Enter to continue...")


        #Enum option
        elif usrInput=='2':
            print("""\033[0;36m
                 _____
                | ____|_ __  _   _ _ __ ___
                |  _| | '_ \| | | | '_ ` _ \\
                | |___| | | | |_| | | | | | |
                |_____|_| |_|\__,_|_| |_| |_|
                """)
            index=[]
            for i in range(len(ENUM)):
                try: print(f"\n\033[1;32m{i}: {ENUM[i].name}")
                except AttributeError: print(f"\n\033[1;32m{i}: {ENUM[i]}(No name)")
                index.append(str(i))

            print("\n\033[0;31mback to get back to the main menu")
            usrInput=input("\n\033[1;36mSoo?...: ")
            print("\033[0m")
    
            if usrInput.upper().strip()=='BACK':
                continue

            elif usrInput in index:
                chosen=ENUM[int(usrInput)]
                try: print(f"\n\033[1;32m{chosen.info()}")
                except AttributeError: print(f"\n\033[1;32mNo Info about the plugin")
                yesno=input("\nEnter YES in capitals to execute...\033[0m")
                if yesno.strip().upper()=="YES":
                    try: chosen.execute()
                    except: print("ERROR: Something went wrong!")
                    input("")
                    
            else:
                print("\n\033[1;31mUnknown command!")
                input("Press Enter to continue...")
