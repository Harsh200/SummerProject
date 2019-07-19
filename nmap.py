import os

#function  for getting nmap port Scan
def get_nmap(options,ip):
    command="nmap" + options + ""+ip
    process=os.popen(command)
    results=str(process.read())

