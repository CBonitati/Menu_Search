import sqlite3
import urllib.request
from bs4 import BeautifulSoup
import time
def getPageAsLinux(url):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    req = urllib.request.Request(url, headers=headers)
    data = urllib.request.urlopen(req).read()
    return data

def getUPCDataPage(upc):
    BASE_URL_2 = "https://upcitemdb.com/upc/"
    BASE_URL = "https://www.barcodelookup.com/"
    full_url = BASE_URL + upc
    data = getPageAsLinux(full_url)
    soup = BeautifulSoup( data, "html.parser")
    img_tag = soup.find("img", attrs={"id":"img_preview"})
    return img_tag["src"]


def savePair(upc, url):
    save_file = open("img_urls.txt", "a")
    save_file.writelines("%s, %s\n" % (upc, url))
    save_file.close()

def main():
    print(getUPCDataPage("024300041020"))
    conn = sqlite3.connect("food_db.db")
    cursor = conn.cursor()
    upc = None
    for row in cursor.execute("select gtin_upc from foods"):
        upc = row[0]
        if upc != None:
            try:
                img = getUPCDataPage( upc ) 
                print("Saving:", upc)
                savePair(upc, img)
                time.sleep(3)
            except:
                print( "Failed on:", upc )
            

def penis():
    data = getPageAsLinux("https://duckduckgo.com/?q=024300041020&ia=images&iax=images")
    print(data) 

if __name__ == "__main__":
    main()
