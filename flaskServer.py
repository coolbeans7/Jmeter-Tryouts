from flask import Flask
from os.path import expanduser
app = Flask(__name__)
home = expanduser("~")

@app.route("/startserver")
def hello():
    from subprocess import call
    call(["./start_server.sh"])

    return "Server: OK"

@app.route("/stopserver")
def shuterdown():
    from subprocess import call
    call(["pkill", "java"])

    return "Server: Shutdown"

@app.route("/status")
def status():

    data = ""

    with open (home+"/jmeterServer.out", "r") as myfile:
        data=myfile.read
        return data

if __name__ == "__main__":
    app.run(debug=True)
