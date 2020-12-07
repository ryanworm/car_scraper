from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # creating  path to the chrome driver
    executable_path = {"executable_path" : "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = True)

def scrape():
    browser = init_browser()
    listings = {}

    url = "https://www.autotrader.ca/cars/?rcp=0&rcs=0&prx=100&hprc=True&wcp=True&sts=New-Used&inMarket=basicSearch&loc=L8P2H3"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find("span").get_text()
    listings["price"] = soup.find("span", class="price-amount").get_text()

    return listings