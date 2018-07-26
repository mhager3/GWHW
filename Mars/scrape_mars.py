# Dependencies
import pandas as pd
import requests
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup as bs

def scrape():
    # setup return variable
    results = {}

    # url for Nasa
    url = 'http://mars.nasa.gov/news'

    # splinter setup
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # Beautiful soupify it
    html = browser.html
    soup = bs(html, 'lxml')

    # extract the title and the teaser body
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # capture extracted data
    results['news_title'] = news_title
    results['news_p'] = news_p

    # jpl - feature image
    # setup url and base url
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    jpl_base_url = 'https://www.jpl.nasa.gov'

    # splinter to get image
    browser.visit(jpl_url)

    # splinterizing and soupifying
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, 'lxml')

    # get the featured image
    featured_img = jpl_base_url + jpl_soup.find(id='full_image')['data-fancybox-href']

    # capture extracted data
    results['featured_img_url'] = featured_img

    # twitter url to visit
    twitter_url = 'https://twitter.com/marswxreport?lang=en'

    # splinter to get object
    browser.visit(twitter_url)

    # splinterizing and soupifying
    twitter_html = browser.html
    twitter_soup = bs(twitter_html, 'lxml')

    # get the tweet text
    mars_weather = twitter_soup.find(class_='tweet-text').text

    results['mars_weather'] = mars_weather

    # url to visit
    facts_url = 'http://space-facts.com/mars/'

    # scrape table from html
    table = pd.read_html(facts_url)

    # create df with columns' headers
    temp_df = table[0]
    temp_df.columns = ['Label','Value']

    # set index to the label column
    df = temp_df.set_index('Label')

    # convert to html table
    facts_table = df.to_html()

    # capture extracted data
    results['facts_table'] = facts_table

    # USGS Astrogeology url
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # splinter to get object
    browser.visit(usgs_url)

    # splinterizing and soupifying
    usgs_html = browser.html
    usgs_soup = bs(usgs_html, 'lxml')

    # use css notation with select() to get all items
    items = usgs_soup.select('div.item')

    # setup image url list
    image_urls = []

    # loop through every item of html, parse out title and get url for image
    for item in items:
        
        # extract the title and truncate
        title = (item.find('h3').text).replace(' Enhanced', '')
            
        # splinterize: use splinter to click on the link
        # (http://splinter.readthedocs.io/en/latest/elements-in-the-page.html)
        browser.click_link_by_partial_text(title)
        
        # soupify
        soup = bs(browser.html, 'html.parser')
        
        # find the image anchor by text attribute
        img = soup.find('a', text='Sample')
        
        # extract url from img
        img_url = img['href']
        
        #make a dict and append to the list
        image_urls.append({'title': title, 'image_url': img_url})


    # capture extracted data
    results['image_urls'] = image_urls





    return results