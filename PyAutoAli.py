### imports ###
import sys, time, codecs, re, logging, requests, csv, json
from bs4 import BeautifulSoup

### enable logging ###
#logging.basicConfig(level=logging.DEBUG)

class PyAutoAli(object):
    def __init__(self):
        self.variables: Dict = {"timesleep": ["time sleep", "timesleep"],
                                "maximages": ["max images", "maximages"],
                                "parser": ["parser"]}
        self.parsers: List[str] = ["lxml", "html.parser", "html5lib"]
        self.settings = self.getSettings()
        self.timesleep: int = self.settings['timesleep'] # the duration of the pause between links
        self.maximages: int = self.settings['maximages'] # max value of images
        self.parser: str = self.settings['parser'] # you can use "lxml"/"html.parser"/"html5lib"
        self.data: List[dict] = []
        self.openfilepath: str = ""

    def check_file(self, path: str) -> None:
        self.data: List[dict] = []
        self.openfilepath: str = path
        try:
            with open(path) as file:
                for url in file:
                    self.checkurl(url)
                    time.sleep(self.timesleep)
        except Exception as e:
            raise

    def save_file(self, path: str = "") -> None:
        if path == "":
            try:
                path = self.openfilepath[:-3]+".csv"
            except Exception as e:
                 raise
        if len(self.data)>0:
            try:
                with open(path, "w", newline='\n') as file:
                    writer = csv.writer(file, delimiter =';')
                    writer.writerow((
                        "url",
                        "name",
                        "price",
                        "discount",
                        "images"
                    ))
                    for item in self.data:
                        writer.writerow((item['url'],
                                         item['name'],
                                         item['price'],
                                         item['discount'],
                                         "\n".join(image for image in item['images'])))
                self.data: List[dict] = []
            except Exception as e:
                 raise

    def check_url(self, url: str) -> None:
        try:
            html = requests.get(url)
            url: string = html.url
            soup = BeautifulSoup(html.text, self.parser)
            name: str = soup.find("div", class_=re.compile("Product_Name__container")).next_element.text
            if(soup.find("span", class_=re.compile("Product_UniformBanner__uniformBannerBoxDiscounts")) != None):
                discond: bool = True
                price: str = soup.find("span", class_=re.compile("Product_UniformBanner__uniformBannerBoxDiscounts")).next_element.text
            else:
                discount: bool = False
                price: str = soup.find("div", class_=re.compile("Product_Price__container")).next_element.text
            images: List[str] = []
            for i, image in enumerate(soup.find_all("div", class_=re.compile("Product_GalleryBarItem__barItem"))):
                if i < self.maximages:
                    images.append(re.sub(r"_50x50.*", "", image.next_element['src']))
            self.data.append(
                {
                    "url": url,
                    "name": name,
                    "price": price,
                    "discount": discount,
                    "images": images
                }
            )
        except Exception as e:
            pass

    def get_settings(self):
        return json.load(open("config.json"))

    def set_settings(self,
                     variable,
                     value):
        if variable in self.variables.keys():
            if variable == "timesleep":
                try:
                    self.timesleep = int(value)
                except Exception as e:
                    raise
            elif variable == "maximages":
                try:
                    self.maximages = int(value)
                except Exception as e:
                    raise
            elif variable == "parser" and value in self.parsers:
                try:
                    self.parser = value
                except Exception as e:
                    raise
            vals = (val for val in [self.timesleep, self.maximages, self.parser])
            jsondict = {}
            for var in self.variables.keys():
                jsondict[var] = next(vals)
            with open('config.json', 'w') as file:
                json.dump(jsondict,
                file)
