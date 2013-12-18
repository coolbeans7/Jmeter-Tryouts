Bees-With-Machine-Guns
=======================

Step 1: Email IT@plaxo.com and get access to `dev64, dev65, dev67, dev13`

Step 2: `git clone` this project on each server

Step 3: Login to `dev65`, `cd` to the project directory

Step 4: execute `./start_server.sh`

Repeat for `dev67, dev13`

Upload a .jmx test to `dev64` `cd` to `~/Bees-With-Machine-Guns/tests`

Example Run: `./apache-jmeter-2.9/bin/jmeter -n -t tests/seeitload01.jmx -R dev65,dev67,dev13 -l results.csv`

Replace `seeitload01.jmx` with your test name you uploaded and execute.

You can now retrive `results.csv` which will contain the test results