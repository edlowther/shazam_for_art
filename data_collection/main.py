import requests
from lxml import html
import time
import urllib.request

url = "https://artuk.org/discover/artworks/view_as/grid/search/makers:joseph-mallord-william-turner-17751851/page/5"
response = requests.get(url)
grid_html = html.fromstring(response.text)
listing_grid = grid_html.cssselect(".listing-grid")[0]
painting_count = 1
for a in listing_grid.cssselect("a"):
    if a.get("href") and "/artworks/" in a.get("href"):# and not "/view_as/" in a.get("href"):
        print(a.get("href"))
        painting_response = requests.get(a.get("href"))
        painting_html = html.fromstring(painting_response.text)
        print(painting_html.cssselect(".artwork")[0].cssselect("img")[0].get("src"))
        time.sleep(1)
        artwork_url = painting_html.cssselect(".artwork")[0].cssselect("img")[0].get("src")
        print(artwork_url)
        time.sleep(1)
        save_to = "./images/turner_{}.jpg".format(painting_count)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(artwork_url, save_to)
        painting_count += 1
        time.sleep(1)
