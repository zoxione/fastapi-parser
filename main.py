from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from lxml import html
from time import sleep

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    shopUrl: str

@app.post("/aliexpress")
def get_gift_from_aliexpress(item: Item):
    driver = webdriver.Chrome()
    driver.get(item.shopUrl)
    sleep(1)

    tree = html.fromstring(driver.page_source)
    title = tree.xpath('//h1/text()')[0]
    price = tree.xpath('//div[@class="snow-price_SnowPrice__secondPrice__18x8np"]/text()')[0]
    imageUrl = tree.xpath('//img[@data-idx=0]/@src')[0]

    result = { "title": title, "price": price, "imageUrl": imageUrl }
    print(result)
    return result