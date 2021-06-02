from flask import Flask, render_template,request
import subprocess
import amazon_reviews 

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def user_response():
    data= request.form.to_dict()
    url = data["url"]
    pages = data["pages"]

@app.route('/download csv file')
def scrape():
    process = subprocess.run(f'scrapy runspider amazonReviews.py -o output.csv -a url={url}', shell= True)
    
@app.route('/download summary')
def summary():

