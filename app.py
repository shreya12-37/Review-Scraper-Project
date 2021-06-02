from flask import Flask, render_template,request
import subprocess
import amazon_reviews 
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/download csv file',methods=['POST'])
def scrape():
    data= request.form.to_dict()
    url = data["url"]
    pages = data["pages"]
    process = subprocess.run(f'scrapy runspider amazonReviews.py -o output.csv -a url= {url}', shell= True)
    
@app.route('/download summary',methods=['POST'])
def summary():
    data=request.form.to_dict()
    my_url = data["url"]
    r = requests.get(my_url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    product_title = soup.find(class_=['a-text-ellipsis']).get_text()
    overall_rating = soup.find(class_=['averageStarRating']).get_text()
    global_rating_reviews = soup.find(class_=['a-row a-spacing-base a-size-base']).get_text().strip()
    five_star = soup.find(class_ =['5star'])['title']
    four_star = soup.find(class_ =['4star'])['title']
    three_star = soup.find(class_ =['3star'])['title']
    two_star = soup.find(class_ =['2star'])['title']
    one_star = soup.find(class_ = ['1star'])['title']

    summary = {'product name': product_title, 'overall rating': overall_rating, 'number of global reviews and ratings': global_rating_reviews, 'five stars': five_star, "four stars" : four_star, "three stars": three_star, "two stars": two_star, "one stars": one_star}
    return summary 




