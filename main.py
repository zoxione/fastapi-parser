from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from lxml import html
from time import sleep
import os


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    shopUrl: str



@app.post("/aliexpress")
def get_gift_from_aliexpress(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(item.shopUrl)
        sleep(5)
        tree = html.fromstring(driver.page_source)
        driver.quit()

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



@app.post("/ozon")
def get_gift_from_ozon(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(item.shopUrl)
        sleep(5)
        tree = html.fromstring(driver.page_source)
        driver.quit()

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//span[@class="ns8"]/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@fetchpriority="high"]/@src')
        if imageUrl:
            imageUrl = imageUrl[0]

        result = {"title": title, "price": price, "imageUrl": imageUrl}
        print(result)
        return result
    except:
        return {"error": "Something went wrong"}
