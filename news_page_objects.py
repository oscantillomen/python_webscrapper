import bs4
import requests

from common import config

class HomePage:
    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self.visit(url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepages_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)
        
        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        self._html.select(query_string)

    def visit(self, url):
        response  = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
