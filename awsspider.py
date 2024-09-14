import scrapy
from scrapy.crawler import CrawlerProcess

class AWSSpider(scrapy.Spider):
    # The name of the spider, used for identifying it
    name = 'aws_spider'
    
    # Domains this spider is allowed to crawl
    allowed_domains = ['aws.amazon.com']
    
    # Starting URL(s) for the spider to begin crawling
    start_urls = ['https://aws.amazon.com']

    # Custom settings for the spider's behavior
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # Delay between consecutive requests (in seconds)
        'CONCURRENT_REQUESTS': 1  # Number of concurrent requests (only one at a time)
    }

    def parse(self, response):
        """
        Parse the response from the starting URL.
        Extracts all the links on the page and yields requests to crawl those links.
        """
        # Extract all links from the page
        links = response.css('a::attr(href)').getall()
        
        # Create absolute URLs from the relative URLs
        valid_links = [response.urljoin(link) for link in links]

        # Limit to the first 10 links for testing
        for link in valid_links[:10]:
            yield scrapy.Request(url=link, callback=self.parse_subpage)

    def parse_subpage(self, response):
        """
        Parse the response from subpages.
        Extracts and yields the URL and HTML content of the page.
        """
        # Decode the response body to UTF-8
        page_content = response.body.decode('utf-8')

        # Yield the URL and the HTML content
        yield {
            'url': response.url,
            'html': page_content
        }

# Create and configure the crawler process
process = CrawlerProcess(settings={
    'FEEDS': {
        'output.json': {'format': 'json'},  # Output the results to a JSON file
    },
    'LOG_LEVEL': 'INFO'  # Set logging level to INFO
})

# Start the crawling process with the defined spider
process.crawl(AWSSpider)
process.start()
