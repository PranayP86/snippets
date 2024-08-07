import paramiko
import imp

host = ""
username = ""
password=  ""
accounts = {}

# Reads files for secrets
def getSecretsFromFile(filename):
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()

# Runs SSH commands, looping through account directories
def sshRunAll():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    except Exception as e:
        print(str(e))
        client = paramiko.SSHClient()

    for account in accounts:
        client.connect(host, username=username, password=password)
        # Command to execute in account
        res = runCommand(client, "")
        print(res)
        client.close()

# Send command to client shell
def runCommand(client, cmd: str = "whoami"):
    _stdin, _stdout,_stderr = client.exec_command(cmd)
    return _stdout.read().decode()

sshRunAll('hosts-and-accounts.txt')
