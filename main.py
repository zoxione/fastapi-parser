from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests as req
from selenium import webdriver
from lxml import html
from time import sleep
import os


app = FastAPI()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    shopUrl: str

# @app.post("/wildberries")
# def get_gift_from_ozon(item: Item):
#     try:
#         title = ""
#         price = ""
#         imageUrl = ""
#
#         resp = req.get(item.shopUrl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
#         print(resp.status_code)
#         #sleep(5)
#         soup = BeautifulSoup(resp.text, "html.parser")
#         title = soup.find('h1')
#         if title:
#             title = title.text
#         print(soup.find('h1'))
#         # price = soup.find('div', class_='snow-price_SnowPrice__secondPrice__18x8np').text
#         #imageUrl = soup.find('img', class_='gallery_Gallery__image__re6q0q')
#
#         result = {"title": title, "price": price, "imageUrl": imageUrl}
#         print(result)
#         return result
#     except:
#         return {"error": "Something went wrong"}

@app.post("/aliexpress")
def get_gift_from_aliexpress(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        driver.get(item.shopUrl)
        sleep(5)
        tree = html.fromstring(driver.page_source)

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//div[@class="snow-price_SnowPrice__secondPrice__18x8np"]/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@data-idx=0]/@src')
        if imageUrl:
            imageUrl = imageUrl[0]

        result = {"title": title, "price": price, "imageUrl": imageUrl}
        print(result)
        return result
    except:
        return {"error": "Something went wrong"}
