### imports ###
import sys, time, codecs, re, logging, requests, csv
from bs4 import BeautifulSoup

### enable logging ###
#logging.basicConfig(level=logging.DEBUG)

class PyAutoAli(object):
    def __init__(self):
        self.timesleep: int = 5 # the duration of the pause between links
        self.maximages: int = 3 # max value of images
        self.parser: str ="lxml" # you can use "lxml"/"html.parse"/"html5lib"
        self.data: List[dict] = []
        self.openfilepath: str = ""

    def checkfile(self, path: str) -> None:
        self.data: List[dict] = []
        self.openfilepath: str = path
        try:
            with open(path) as file:
                for url in file:
                    self.checkurl(url)
                    time.sleep(timesleep)
        except Exception as e:
            raise

    def savefile(self, path: str) -> None:
        pass

    def checkurl(self, url: str) -> None:
        try:
            html = requests.get(url)
            url: string = html.url
            soup = BeautifulSoup(html.text, self.parser)
            name: str = soup.find("div", class_=re.compile("Product_Name__container")).next_element.text
            if(soup.find("span", class_=re.compile("Product_UniformBanner__uniformBannerBoxDiscounts")) != None):
                discond: bool = True
                price: str = soup.find("span", class_=re.compile("Product_UniformBanner__uniformBannerBoxDiscounts")).next_element.text
            else:
                discond: bool = False
                price: str = soup.find("div", class_=re.compile("Product_Price__container")).next_element.text
            images: List[str] = []
            for i, image in enumerate(soup.find_all("div", class_=re.compile("Product_GalleryBarItem__barItem"))):
                if i < self.maximages-1:
                    images.append(image.next_element['src'].replace("_50x50", ""))
            self.data.append(
                {
                    "url": url,
                    "name": name,
                    "price": price,
                    "discond": discond,
                    "images": images
                }
            )
        except Exception as e:
            raise

if __name__ == '__main__':
    pyAuto = PyAutoAli()