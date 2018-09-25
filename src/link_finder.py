from html5lib.html5parser import HTMLParser
try:
    from urllib.parse import urlparse, urljoin
except ImportError:
     from urlparse import urlparse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super.__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.link = set()

    def parseError(self, errorcode="XXX-undefined-error", datavars={}):
        pass

    # This function is defined in the HTMLParser and is used so that only the start tag is considered and not the closing tag <HTML></HTML>
    # Here </HTML> will not be considered
    def handle_starttag(self, tag, attribute):
        if tag == 'a':
            for (attr, value) in attribute:
                if attr == 'href':
                    url = urljoin(self.base_url, self.page_url) ## Construct a full (“absolute”) URL by combining a “base URL” (base) with another URL (url).
                    self.link.add(url)

    def page_links(self):
        return self.link





