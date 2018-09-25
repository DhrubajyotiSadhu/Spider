import urllib2
from link_finder import LinkFinder
from utils import *

try:
    from urllib.request import urlopen
except ImportError:
     from urlparse import urlparse

class Spider:

    # Class variables shared among all instances or all spiders.
    project_name = ''
    domain_name = ''
    base_url = ''
    queued_file = ''
    crawled_file = ''
    queued = set()
    crawled = set()

    def __init__(self, project_name, domain_name, base_url):
        Spider.base_url = base_url
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.queued_file = Spider.project_name + 'queued.txt'
        Spider.crawled_file = Spider.project_name + 'crawled.txt'
        self.boot()
        self.crawl_pages('First Spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_directory(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queued = file_to_set(Spider.queued_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_pages(thread_name, page_url):
        if page_url not in Spider.crawled:
            print thread_name + " - Now Crawling - " + page_url
            print ":Currently in Queue - " + str(len(Spider.queued)) + \
                  " :Already Crawled - " + str(len(Spider.crawled))

            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queued.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_file()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getHeader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url )
            finder.feed(html_string)
        except:
            print "Cannot crawl the page" + page_url
            return set()

        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for urls in links:
            if links in Spider.queued:
                continue
            if links in Spider.crawled:
                continue
            if Spider.domain_name not in urls:
                continue
            Spider.queued.add(urls)

    @staticmethod
    def update_files():
        set_to_file(Spider.queued, Spider.queued_file)
        set_to_file(Spider.crawled, Spider.crawled_file)







