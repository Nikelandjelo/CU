#!/bin/python3
import time
import threading
from os import system, scandir
from rich import print as rprint

######### Not working due to /proc beeing pseudo-file system
#import sys
#from watchdog.observers import Observer
#from watchdog.events import FileSystemEventHandler
#
#class Handler(FileSystemEventHandler):
#    def on_created(self, event):
#        rprint(f"| {event.event_type}\t|{event.src_path}")
#    def on_deleted(self, event):
#        rprint(f"| {event.event_type}\t|{event.src_path}")
#    def on_modified(self, event):
#        rprint(f"| {event.event_type}\t|{event.src_path}")
#    def on_moved(self, event):
#        rprint(f"| {event.event_type}\t|{event.src_path}")
#
#def PROCMON():
#    rprint("|\n+-WAITING FOR NEW PROCESSES\n+-----------------------------\n|")
#
#    event_handler = Handler()
#    observer = Observer()
#    observer.schedule(event_handler, path='/proc/', recursive=True)
#    observer.start()
#
#    try:
#        while True:
#            time.sleep(5)
#
#    except KeyboardInterrupt:
#        rprint("\n+-----------------------------\n+-STOP MONITORING /proc\n")
#    observer.stop()
#    observer.join()


### Displays the CPU info
def CPU():
    rprint("+--------------------------CPU-INFO---------------------------")
    # Opens /proc/cpuinfo
    with open('/proc/cpuinfo', 'r') as cpu: 
        cpuDATA = ["vendor_id", "model name", "cpu MHz", "cache size", "cpu cores", "siblings"]
        cpuInfo = cpu.readlines()
        for i in cpuDATA:
        #Geting the neseccery lines and displays the formatted info
            for line in cpuInfo:
                if i in line:
                    line = line.split(':')
                    rprint(f"| {line[0].strip()}\t: {line[1].strip()}", end='\n')
                    break
        #Closes the file
        cpu.close()

### Displays System Load info
def SYSLOAD():
    rprint("+--------------------------SYS-LOAD---------------------------")
    # Opens /proc/loadavg, formats the content and displays
    with open('/proc/loadavg', 'r') as load:
        loadInfo = load.read()
        loadInfo = loadInfo.split(' ')
        rprint(f"| Load 1m \t: {loadInfo[0]}")
        rprint(f"| Load 5m \t: {loadInfo[1]}")
        rprint(f"| Load 15m\t: {loadInfo[2]}")
        load.close()

### Displays porcess info
def PROCINFO():
    rprint("+--------------------------PROCCESSES---------------------------")
    # Checks the max allowed number for PID
    with open('/proc/sys/kernel/pid_max', 'r') as kernel:
        rprint(f"| Max Processes\t: {kernel.read()}", end='')
        kernel.close()

    # Checks number of currently running processes
    i=0
    for j in getPS():
        i+=1
    rprint(f"| Processes\t: {i}")

### Monitoring for starting tasks
def psStart():
    while stop_threads == False:
        time.sleep(0.01)
        for d in scandir('/proc'):
            if not d.name in PROCS and d.is_dir() and str(d.name).isdigit():
                try:
                    PROCS.append(d.name)
                    p = open(f'/proc/{d.name}/status', 'r')
                    c = open(f'/proc/{d.name}/cmdline', 'r')
                    prc = p.readline()
                    cmd = c.readline()
                    prc = prc.split()
                    cmd = cmd.strip(prc[1])
                    rprint(f"| {time.ctime()} | START | {d.name} | {prc[1]}\t| {cmd}")
                    p.close()
                    c.close()
                except FileNotFoundError:
                    rprint(f"| {time.ctime()} | START | MISS |")

### Monitoring for stopping tasks
def psStop():
    while stop_threads == False:
        time.sleep(0.01)
        for p in PROCS:
            if not p in getPS():
                PROCS.remove(p)
                rprint(f"| {time.ctime()} | STOP  | {p} |")


### Gets current tasks
def getPS():
    PROCS = []
    for d in scandir('/proc'):
        if d.is_dir() and str(d.name).isdigit():
            PROCS.append(d.name)
    return PROCS

### Combines psStart and psStop
def PS():
    # Global var used to terminate threads
    global stop_threads
    stop_threads = False

    # Global var that contains all processes
    global PROCS
    PROCS = getPS()

    # Defining the threads
    t1 = threading.Thread(target=psStart)
    t2 = threading.Thread(target=psStop)
  
    try:
        rprint("|\n+-WAITING FOR NEW PROCESSES\n+-----------------------------\n|")
        # Starting all threads
        t1.start()
        t2.start()
        # Threads waiting for each other to finish
        t1.join()
        t2.join()
    except KeyboardInterrupt:
        rprint("\n+-----------------------------\n+-STOP MONITORING /proc\n")
        # Stopping all threads
        stop_threads = True

def main():
    system("clear")
    CPU()
    SYSLOAD()
    PROCINFO()
    PS()

if __name__ == "__main__":
    main()
