from urllib.parse import urlparse

def get_domain_name(url):
    try:
        name = get_sub_domain_name(url).split('.')
        return name[-2] + '.' + name[-1]
    except:
        return ''
# get sub domain
def get_sub_domain_name(url):
    try:
        return urlparse(url).netlock
    except:
        print "Cannot Return Sub domain"
        return ''
