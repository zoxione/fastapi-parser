from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from lxml import html
from time import sleep
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def parsing(shopUrl):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get(shopUrl)
    sleep(5)

    tree = html.fromstring(driver.page_source)
    driver.quit()

    return tree


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

        tree = parsing(item.shopUrl)

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


@app.post("/regard")
def get_gift_from_regard(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        tree = parsing(item.shopUrl)

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//span[@class="PriceBlock_price__3hwFe"]/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@class="BigSlider_slide__image__1DrhA"]/@src')
        if imageUrl:
            imageUrl = imageUrl[0]

        result = {"title": title, "price": price, "imageUrl": imageUrl}
        print(result)
        return result
    except:
        return {"error": "Something went wrong"}


@app.post("/yandexmarket")
def get_gift_from_yandexmarket(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        tree = parsing(item.shopUrl)

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//span[@class="_1Hw8N"]/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@class="_1Gngb"]/@src')
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

        tree = parsing(item.shopUrl)

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


@app.post("/dns")
def get_gift_from_dns(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        tree = parsing(item.shopUrl)

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//span[@class="product-buy__prev"]/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@class="product-images-slider__main-img loaded"]/@src')
        if imageUrl:
            imageUrl = imageUrl[0]

        result = {"title": title, "price": price, "imageUrl": imageUrl}
        print(result)
        return result
    except:
        return {"error": "Something went wrong"}


@app.post("/wildberries")
def get_gift_from_wildberries(item: Item):
    try:
        title = ""
        price = ""
        imageUrl = ""

        tree = parsing(item.shopUrl)

        title = tree.xpath('//h1/text()')
        if title:
            title = title[0]
        price = tree.xpath('//ins/text()')
        if price:
            price = price[0]
        imageUrl = tree.xpath('//img[@height="1200"]/@src')
        if imageUrl:
            imageUrl = imageUrl[0]

        result = {"title": title, "price": price, "imageUrl": imageUrl}
        print(result)
        return result
    except:
        return {"error": "Something went wrong"}
