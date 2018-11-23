import scrapy

class BrickSetSpider(scrapy.Spider):
  name = "leroy_pages_spider"
  start_urls = ['https://www.leroymerlin.com.br/']

  def parse(self, response):
    MENU_SELECTOR = '.m-main-menu-wrapper div ul li ul li a'
    for brickset in response.css(MENU_SELECTOR):
      URL_SELECTOR = '::attr(href)'
      yield {
        'url': brickset.css(URL_SELECTOR).extract_first(),
      }