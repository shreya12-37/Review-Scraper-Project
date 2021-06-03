import requests
from bs4 import BeautifulSoup

my_url = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/product-reviews/B0883JQQJQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
#print(htmlcontent)
base_url = my_url + "&pageNumber="

star_rating = []
# comments = []
# ReviewerName = []
# date = []
# title = []

start_url = []
for i in range (1,2):
    start_url.append(base_url + str(i))
count = 0 
for url in start_url:
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    # s = soup.find_all(class_=["review-rating"])
    # for a in s:
    #     star_rating.append(a)
    # print(star_rating)
    for j in soup:
        star_rating.append(soup.find_all_next(class_=["review-rating"]).text)
        count = count+1
        #comments.append(soup.find(class_=["review-text-content"]).text)
        #ReviewerName.append(soup.find(class_=["a-profile-name"]).text)
        # date.append(soup.find(class_=["review-date"]).get_text())
        # title.append(soup.find(class_=["review-title"]).get_text()) 

#print(star_rating)
