import os

#get ip address module
def get_ip_address(url):
    command="host"+url
    process=os.popen(command)
    results=str(process.read())
    marker=results.find('has address') + 12


#Returning the top level ip address