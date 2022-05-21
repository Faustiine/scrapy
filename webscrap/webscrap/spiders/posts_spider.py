from fileinput import filename
import scrapy

class Marmiton(scrapy.Spider):
    name="nom_recette"
    num=2
    start_urls=["https://www.marmiton.org/recettes/index/categorie/dessert/"]
    url="https://www.marmiton.org/recettes/index/categorie/dessert/"
##récuperation des pages web split pour le separateurdu numero de page
#    def parse(self,response):
#        page=response.url.split('=')[-1]
#        filename='posts-%s.html' %page
#        with open(filename,'wb') as f:
#            f.write(response.body)
    
    def parse(self,response):
        
        yield{
            'nom_recette': response.css('h4::text').getall(),
            'etoiles': response.css('.mrtn-stars').getall(),
            'review': response.css('.mrtn-font-discret::text').getall()
            }
        
        next_page = self.url + str(self.num)##incrementation du numero de page
        if self.num <= 9:
            self.num += 1
            yield scrapy.Request(next_page, callback=self.parse)
        
##response.css('h4::text').getall() ##tous les h4
## par class :response.css('.recipe-card__title::text').getall()
##class="mrtn-stars" etoile puis traduire
##nbre de reviews: response.css('.mrtn-font-discret::text').getall()

##response.xpath('//h4/text()').extract() ou getall()

##nom_recette=response.css('h4::text').getall()
#etoiles=response.css('.mrtn-stars').getall()
# review=response.css('.mrtn-font-discret::text').getall()

##scrapy crawl nom_recette -o nom_recette.csv ( suppr apres o pour pas enregstré)