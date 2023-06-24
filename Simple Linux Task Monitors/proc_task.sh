#!/bin/bash

#Get CPU info using /proc
#Vendor
CPU_v=`grep -m 1 "vendor_id" /proc/cpuinfo | awk '{printf "| CPU vendor: " substr($0, 13)}'`
#CPU model
CPU_m=`grep -m 1 "model\ name" /proc/cpuinfo | awk '{printf "| CPU model: " substr($0, 13)}'`
#CPU speed
CPU_s=`grep -m 1 "cpu\ MHz" /proc/cpuinfo | awk '{printf "| CPU speed: " $NF "MHz"}'`
#Cash size
CPU_cash=`grep -m 1 "cache\ size" /proc/cpuinfo | awk '{printf "| Cahse Size: " substr($0, 13)}'`
#Amount of cores
CPU_cores=`grep -m 1 "cpu\ cores" /proc/cpuinfo | awk '{printf "| Cores: " $NF}'`
#Amount of virtual cores
CPU_vcores=`grep -m 1 "siblings" /proc/cpuinfo | awk '{printf "| Virtual cores: " $NF}'`
#All processors
CPU_c=`grep "processor" /proc/cpuinfo | awk '{printf "| CPU: " $NF "\t"}'`

#Avr system load using /proc
LOAD1=`cat /proc/loadavg | awk '{printf $1}'`
LOAD5=`cat /proc/loadavg | awk '{printf $2}'`
LOAD15=`cat /proc/loadavg | awk '{printf $3}'`
#Count the current running proccesses using /proc
MAX_PROC=`cat /proc/sys/kernel/pid_max`
PROC_COUNT=`find /proc/ -maxdepth 1 -type d -name "[0-9]*" | wc -l` #Same solution with less checks |ls -ld /proc/[0-9]* 

#Display CPU info
echo "---------------------------CPU-INFO--------------------------"
echo $CPU_v
echo $CPU_m
echo $CPU_s
echo $CPU_cash
echo $CPU_cores
echo $CPU_vcores
printf "|\n| CPUs\n"
echo $CPU_c
echo

#Display avr system load
echo "---------------------------SYS-LOAD--------------------------"
echo '| Average over 1m: ' $LOAD1
echo '| Average over 5m: ' $LOAD5
echo '| Average over 15m:' $LOAD15
echo 

#Dosplay cirrent rinning proccesses
echo "---------------------------PROCCESSES--------------------------"
echo '| Maximum Proccess Alowed:' $MAX_PROC
echo '| Proccess Count:' $PROC_COUNT
