import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    
    # Spider name
    name = "amazon_reviews"
    # Domain names to scrape
    allowed_domains = ["amazon.in"]
    start_urls = []
    def __init__(self, url="", *args, **kwargs):
        super(AmazonReviewsSpider, self).__init__(*args, **kwargs)
        self.start_urls=[url]
    # Base URL for the MacBook air reviews
    # myBaseUrl = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/product-reviews/B0883JQQJQ/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8"
    # myBaseUrl = input()
    #Baseurl will be input from user
    # start_urls = [myBaseUrl]
    # Creating list of urls to be scraped by appending page number a the end of base url
    #number of pages to be taken from user
    # for i in range(1, 2):
    #     start_urls.append(myBaseUrl + str(i))
    # Defining a Scrapy parser
    print(start_urls)
    def parse(self, response):
        
        # print(self.url)
        # start_urls = []
        # for i in range(1, 2):
        #     start_urls.append(myBaseUrl + str(i))
        # print(self.url)
        data = response.css("#cm_cr-review_list")
        # Collecting product star ratings
        star_rating = data.css(".review-rating")
        # Collecting user reviews
        comments = data.css(".review-text-content")
        #reviewer name
        reviewerName = data.css(".a-profile-name")
        #review date
        date = data.css(".review-date")
        #review title
        title = data.css(".review-title")
        #number of helpful votes
        helpfulVotes = data.css(".cr-vote-text")
        count = 0
        # Combining the results
        for review in star_rating:
            yield {
                "reviewerName": "".join(reviewerName[count].xpath(".//text()").extract()).strip(),
                "title": "".join(title[count].xpath(".//text()").extract()).strip(),
                "stars": "".join(review.xpath(".//text()").extract()).strip(),
                "comment": "".join(comments[count].xpath(".//text()").extract()).strip(),
                "date": "".join(date[count].xpath(".//text()").extract()).strip(),
                "helpfulVotes": "".join(helpfulVotes[count].xpath(".//text()").extract()).strip()
            }
            count = count + 1

# Command to run scrappy
# scrapy runspider amazon_reviews.py -o reviews.csv