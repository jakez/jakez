import scrapy
import pdfkit
import os 

class BlogarticleSpider(scrapy.Spider):
    name = "blogarticle"
    allowed_domains = ["saskiamaarse.com"]
    start_urls = ["https://saskiamaarse.com/blog"]

    def parse(self, response):

        # Parise all the articles
        for href in response.css("div.posts-container article h2.title a::attr(href)"):
            yield response.follow(href, callback=self.parse_article)

        # Get the next page of results
        next_page = response.css("div.next a::attr(href)").get()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
    
    def parse_article(self, response):
        title = response.css("h1::text").get()
        html_content_array = response.css("div.wpb_wrapper p").getall()
        file_path = f'{title}.pdf'

        # Check and create a directory for PDFs
        if not os.path.exists('pdfs'):
            os.mkdir('pdfs')

        html_content = ''.join(html_content_array)
        pdfkit.from_string(title + html_content, f'pdfs/{file_path}')

        yield {
            "title": title,
            "file_path": f'pdfs/{file_path}'
        }
