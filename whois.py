import os


#function to get the domain information

def get_whois(url):
    command="whois" + url
    process=os.popen(command)
    results=str(process.read())

    #Returning the information
    print("WhoisDone")
    return results

#End of whois.py file