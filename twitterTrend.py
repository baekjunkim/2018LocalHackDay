# -*- coding: utf-8 -*-

import time
from string import punctuation
import re
from bs4 import BeautifulSoup      
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys

userId = "**Your Twitter ID**"
userPw = "**Your Twitter Password"

driver = webdriver.Chrome("chromedriver.exe")

def login(userId = userId, userPw = userPw):

    # link to twitter
    twitterUrl = "https://twitter.com/"
    driver.get(twitterUrl)
    
    # log-in to twitter
    twitterId = driver.find_element_by_name('session[username_or_email]')
    twitterId.send_keys(userId)
    twitterPw = driver.find_element_by_name('session[password]')
    twitterPw.send_keys(userPw)
    twitterPw.send_keys(Keys.ENTER)
    time.sleep(1)
    print("finish login")
    
    
def scrapTrend():
    # scrap current "Trend"s from twitter
    element = driver.find_element_by_tag_name('html')
    html = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    trends = soup.find_all("span", {"class": "u-linkComplex-target trend-name"})
    temp = [re.findall("(?<=\\>)(.*)", str(trend))[0] for trend in trends]
    temp = [trend[:trend.find("<")] for trend in temp]
    print("finish scraping trends")
    return temp

def scrapNewsList(temp):
    newsList = {}
    
    newsUrl = "https://www.bing.com/news"
    driver.get(newsUrl)
    time.sleep(2)
    newsSearch.send_keys(Keys.ENTER)
    
    for trend in temp:
        # search for the news related to trend
        newsSearch = driver.find_element_by_name('q')
        newsSearch.clear()
        newsSearch.send_keys(trend)
        newsSearch.send_keys(Keys.ENTER)
        time.sleep(1)
        
        element = driver.find_element_by_tag_name('html')
        html = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        
        # scrap the list of urls of news
        body = soup.find_all("a", {"class": "title"})
        titles = [re.search("(?<=\\>)(.*)", str(title)).group() for title in body]
        titles = [title[:title.find("<")] for title in titles]
        urls = [url["href"] for url in body]
        newsList[trend] = [(title, url) for (title, url) in zip(titles, urls)]
        print(trend)
    return newsList
    
login()
newsList = scrapNewsList(scrapTrend())
#print([key2 for key2 in newsList.values()[0]])
    
