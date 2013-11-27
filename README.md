SeeIT-Load-Tests-Jmeter
=======================

Run /apache-jmeter-2.9/bin/jmeter

Open a test from the /tests folder

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
  
HEAP=-Xms2048m -Xmx2048m’
Please note if you increased the allocated JMeter heap memory remember that you need to have Java runtime environment 6 or above. What you may notice is you’re unable to allocate more than 2 GB of memory; this happened to me, JMeter refused to open, and was the cause of the JMeter only being able to use 1 CPU core. A quick fix for this is to install the 64 bit Java runtime environment, this should alleviate the problem.

I hope this helped you, for my testing it did. If you have any questions or just liked this article feel free to leave a reply. If you want more information on best practices with JMeter please take a look at this link:
  
