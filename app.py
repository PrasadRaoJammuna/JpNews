#from bs4 import BeautifulSoup
#from newsapi import NewsApiClient
from flask import Flask,request,render_template,url_for,redirect
import requests

#newsapi = NewsApiClient(api_key='65729ab9862c408a85621220be43ee5f')

#top_headlines = newsapi.get_top_headlines(q='bitcoin',
  #                                        sources='bbc-news,the-verge',
  ##                                        category='business',
   #                                       language='en',
   #                                       country='in')

app = Flask(__name__)

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=65729ab9862c408a85621220be43ee5f')
def get_data(url):
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return articles

articles = get_data(url)

@app.route('/')
def home():
    return render_template('index.html',articles=articles)

@app.route('/invalid')
def invalid():
    return "<center><h2 style='color:green;'>something went wrong..!</h2></center>"

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method =='POST':
            data =request.form['search']
            if not data:
                return redirect(url_for('invalid'))
            else:
                url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=65729ab9862c408a85621220be43ee5f')
                articles = get_data(url)
                return render_template('search.html',articles=articles,data=data)
        
    #print(get_data(url)) 
    #else:
      #  redirect(url_for('index.html'))
      
    


if __name__ == '__main__':
    app.run(debug=True)