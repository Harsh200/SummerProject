from tld import get_tld

#function get_domain_name
def get_domain_name(url):
    domain_name=get_tld(url)
    return domain_name

print(get_domain_name('https://www.facebook.com'))

#End of domain_name.py file