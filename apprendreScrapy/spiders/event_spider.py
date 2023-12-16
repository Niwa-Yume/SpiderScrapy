import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class EventSpider(scrapy.Spider):
    name = 'event_spider'
    start_urls = ['https://lagraviere.ch/']


def parse(self, response):
    for link in response.css('a::attr(href)').getall():
        yield {
            'link': response.urljoin(link)
        }


class EventSpider(scrapy.Spider):
    name = 'event_spider'
    start_urls = ['https://lagraviere.ch/']

    #regle pour ne pas crawler les liens qui ne sont pas de la page https://lagraviere.ch/evenements/
    rules = (
        Rule(LinkExtractor(allow=('/evenements/')), callback='parse_item')
    )

    
    def parse(self, response):
        #Parcours et récupère tous les liens de la page
        for link in response.css('a::attr(href)').getall():
            yield {
                'link': response.urljoin(link)
            }
        #Parcours et récupère tous les liens des pages suivantes
        for next_page in response.css('a.next-posts-link::attr(href)').getall():
            yield response.follow(next_page, self.parse)
        #affichier les liens crawler dans un fichier json nompage.json
        nompage = response.url.split("/")[-2]
        self.log(f'Saved file {nompage}')

        
