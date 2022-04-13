### imports ###
import sys, time, codecs, re, logging, requests, csv
from bs4 import BeautifulSoup

### enable logging ###
#logging.basicConfig(level=logging.DEBUG)

class PyAutoAli(object):
    def __init__(self):
        self.timesleep: int = 5 # the duration of the pause between links
        self.maximages: int = 3 # max value of images
        self.parser: str = "html.parser" # you can use "lxml"/"html.parser"/"html5lib"
        self.data: List[dict] = []
        self.openfilepath: str = ""

    def checkfile(self, path: str) -> None:
        self.data: List[dict] = []
        self.openfilepath: str = path
        try:
            with open(path) as file:
                for url in file:
                    self.checkurl(url)
                    time.sleep(self.timesleep)
        except Exception as e:
            raise

    def savefile(self, path: str = "") -> None:
        if path == "":
            try:
                path = self.openfilepath[:-3]+".csv"
            except Exception as e:
                 raise
        print(path)
        print(self.data)
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
            print('add')
        except Exception as e:
            pass

if __name__ == '__main__':
    pyAuto = PyAutoAli()
    while True:
        print("""Welcome to the PyAutoAli Open Source project
To start, select the operating mode and proceed according to the instructions:
0: exit
1: manual input
2: file input""")
        mode = int(input(""))
        if mode==0:
            break
        elif mode==1:
            print("In this mode you have to enter by one link")
            while True:
                try:
                    print("Enter url or 0 to exit")
                    url = input()
                    if url == "0": break
                    pyAuto.checkurl(url)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.savefile(path)
                except Exception as e:
                    raise
        elif mode==2:
            print("In this mode, you must enter the path to the file")
            while True:
                try:
                    print("Enter path or 0 to exit")
                    path=input()
                    if path == "0": break
                    pyAuto.checkfile(path)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.savefile(path)
                except Exception as e:
                    raise
        else:
            print("Invalid value entered!")
            input()
