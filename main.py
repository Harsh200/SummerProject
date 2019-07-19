from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *


ROOT_DIR='companies'
create_dir(ROOT_DIR)
def gather_info(name,url):
    robots_txt=get_robots_txt(url)
    domain_name=get_domain_name(url)
    whois=get_whois(domain_name)
    ip_address=get_ip_address(domain_name)
    nmap=get_nmap("-F",ip_address)