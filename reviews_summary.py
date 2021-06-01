import scrapy
import subprocess

class AmazonReviewsSpider(scrapy.Spider):
    # Spider name
    name = "reviews_summary"
    # Domain names to scrape
    allowed_domains = ["amazon.in"]
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/product-reviews/B0883JQQJQ/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&reviewerType=avp_only_reviews&pageNumber="
    start_urls = []
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1, 2):
        start_urls.append(myBaseUrl + str(i))
    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css("#cm_cr-review_list")
        product_name = data.css("")
        overall_rating = data.css("")
        global_rating_reviews = data.css("")
        # Collecting product star ratings
        five_stars = data.css("")
        four_stars = data.css(".a-profile-name")
        three_stars = data.css(".review-date")
        two_stars = data.css(".review-title")
        one_stars = data.css(".cr-vote-text")
        # Combining the results
        yield {
                "Product name": "".join(product_name.xpath(".//text()").extract()).strip(),
                "Overall rating": "".join(overall_rating.xpath(".//text()").extract()).strip(),
                "Number of global rating and reviews": "".join(global_rating_reviews.xpath(".//text()").extract()).strip(),
                "Number of five stars": "".join(five_stars.xpath(".//text()").extract()).strip(),
                "Number of four stars": "".join(four_stars.xpath(".//text()").extract()).strip(),
                "Number of three stars": "".join(three_stars.xpath(".//text()").extract()).strip(),
                "Number of two stars": "".join(two_stars.xpath(".//text()").extract()).strip(),
                "Number of one stars": "".join(one_stars.xpath(".//text()").extract()).strip(),
            }


            