#! /bin/sh

./apache-jmeter-2.9/bin/jmeter -n -t tests/seeitload01.jmx -R dev08,dev12,dev13
