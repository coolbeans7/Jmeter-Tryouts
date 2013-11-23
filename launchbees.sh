#! /bin/sh

#dev64 - 172.20.3.145
#dev65 - 
#dev67 - 
#dev08 - 172.20.3.72
#dev12 - 172.20.3.71
#dev13 - 172.20.3.70
#dev14 -
./apache-jmeter-2.9/bin/jmeter -n -t tests/seeitload01.jmx -R dev08,dev12,dev13,dev14,dev65,dev67
