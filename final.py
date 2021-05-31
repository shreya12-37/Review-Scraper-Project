import tkinter as tk
from tkinter import ttk
from tkinter import * 
import scrapy

root= tk.Tk()
root.title('Review Scraper')

canvas1 = tk.Canvas(root, width = 450, height = 230)
canvas1.pack()
Label(root, text='Enter Product URL :', font=('helvetica', 12, 'normal')).place(x=50, y=50)
entry1 = tk.Entry (root, text='Enter product URL:',bg='#F0F8FF')
entry1.config(font=('helvetica', 12))
entry1.place(x=220, y=50)
# canvas1.create_window(200, 100, window=entry1)
Label(root, text='Enter No. of pages :', font=('helvetica', 12, 'normal')).place(x=50, y=100)
entry2 = tk.Entry (root, text='Enter number of pages required:',bg='#F0F8FF')
entry2.config(font=('helvetica', 12))
entry2.place(x=220, y=100)
# canvas1.create_window(200, 150, window=entry2)

def reviewScraping ():  
    x = entry1.get()
    y = entry2.get()

    # Spider name
    name = "amazon_reviews"

    # Domain names to scrape
    allowed_domains = ["amazon.in"]

    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;amp;reviewerType=all_reviews&amp;amp;pageNumber="
    start_urls = []

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1, y):
        start_urls.append(myBaseUrl + str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css("#cm_cr-review_list")

        # Collecting product star ratings
        star_rating = data.css(".review-rating")

        # Collecting user reviews
        comments = data.css(".review-text")

        #collecting ratings 
        fivestarRating = data.css(".a-link-normal")
        fourstarRating = data.css(".a-link-normal")
        threestarRating = data.css(".a-link-normal")
        twostarRating = data.css(".a-link-normal")
        onestarRating = data.css(".a-link-normal")

        #total global ratings and reviews 
        globalRatingsReviews = data.css("span")

        #reviewer name
        reviewerName = data.css("span.a-profile-name")

        #review date
        date = data.css("span.a-size-base.a-color-secondary.review-date")

        #verified purchase status 
        verification = data.css("span.a-size-mini.a-color-state.a-text-bold")

        #review title
        title = data.css("span")

        #number of helpful votes
        helpfulVotes = data.css("span.a-size-base.a-color-tertiary")

        count = 0

        # Combining the results
        for review in star_rating:
            yield {
                "stars": "".join(review.xpath(".//text()").extract()),
                "comment": "".join(comments[count].xpath(".//text()").extract()),
                "fivestarRating": "".join(fivestarRating.xpath(".//text()").extract()),
                "fourstarRating": "".join(fourstarRating.xpath(".//text()").extract()),
                "threestarRating": "".join(threestarRating.xpath(".//text()").extract()),
                "twostarRating": "".join(twostarRating.xpath(".//text()").extract()),
                "onestarRating": "".join(onestarRating.xpath(".//text()").extract()),
                "globalRatingsReviews": "".join(globalRatingsReviews.xpath(".//text()").extract()),
                "reviewerName": "".join(reviewerName.xpath(".//text()").extract()),
                "date": "".join(date.xpath(".//text()").extract()),
                "verification": "".join(verification.xpath(".//text()").extract()),
                "title": "".join(title.xpath(".//text()").extract()),
                "helpfulVotes": "".join(helpfulVotes.xpath(".//text()").extract()),
            }
            count = count + 1


    #scraping code to be added 
    # canvas1.create_window(200, 200, window=label1)
    
button1 = tk.Button(text='Display reviews',font=('helvetica', 12, 'normal'), command=reviewScraping).place(x=150, y=150)
# canvas1.create_window(200, 200, window=button1)


root.mainloop()
