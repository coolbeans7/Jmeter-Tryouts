SeeIT-Load-Tests-Jmeter
=======================

Run /apache-jmeter-2.9/bin/jmeter

Open a test from the /tests folder

Be sure to set the server ip variable as without it the slave nodes can get confused in the cable/plaxo domain wierdness.
here: apache-jmeter-2.9/bin/jmeter-server, edit this property RMI_HOST_DEF=-Djava.rmi.server.hostname=xxx.xxx.xxx.xxx

dev64:master
dev08:slave
dev12:slave
dev13:slave

modifty seeitload01.jmx on local box, upload to dev64 /SeeIT-Load-Tests-Jmeter/tests/

exec /SeeIT-Load-Tests-Jmeter/apache-jmeter-2.9/bin/launchbees

todo:
figure out how to reliably run jmeter server in background

create armbees => 
  specify server list (user must have key creds on servers)
  logins into servers
  git clone project
  start server in background
  add server to local jmeter.properties and launchbees script
  print "Bee's ARMED"

idea: create loadout =>
  specify parameters for threading users
  modifies .jmx script with correct loadup
  

  
