SeeIT-Load-Tests-Jmeter
=======================

Run /apache-jmeter-2.9/bin/jmeter

Open a test from the /tests folder

Be sure to set the server ip variable as without it the slave nodes can get confused in the cable/plaxo domain wierdness.
here: apache-jmeter-2.9/bin/jmeter-server, edit this property RMI_HOST_DEF=-Djava.rmi.server.hostname=xxx.xxx.xxx.xxx
