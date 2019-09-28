# Putting everything in a single file for now
from bs4 import BeautifulSoup
import urllib.request




def dlURL(url):
    """
    Returns the data gathered from a url
    Data will be retrieved using headers masking as a computer
    @url <string>: The url the data will be retrieved from
    """
    request = urllib.request.Request(url)
    f = urllib.request.urlopen(request)
    data = f.read()
    return data

def soupify(url):
    return BeautifulSoup(dlURL(url), "html.parser")

def main():
    categories = MCD_getAllCategories()
    products = MCD_getProductsFromCategory(categories[1])
    print(products)

#McDonalds menu link retrieval code
MCD_BASE = "http://www.mcdonalds.com"
def MCD_getAllCategories():
    url = "http://www.mcdonalds.com/us/en-us/full-menu.html"
    cat_tag_name = "mcd-category-page__link-item"
    soup = soupify(url)
    soups = soup.find_all("li", {"class":cat_tag_name})
    category_links = [soup.a["href"] for soup in soups]
    return category_links

def MCD_getProductsFromCategory(cat_link):
    full_url = MCD_BASE + cat_link
    print("DEBUG: url=", full_url)
    soup = soupify(full_url)
    item_link_tags = soup.find_all("a", {"class":"categories-item-link"})
    print("DEBUG:", len(item_link_tags))
    item_links = [soup["href"] for soup in item_link_tags]
    return item_links

#Gets ingredients from products
def MCD_getIngsFromProduct(prod_link):
    full_url = MCD_BASE + prod_link
    print("DEBUG: url=", full_url)
    soup = soupify(full_url)


if __name__ == "__main__":
    main()




