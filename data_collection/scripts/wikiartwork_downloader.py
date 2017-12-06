import requests
from lxml import html
import time
import urllib.request

class WikiartworkDownloader:
    def __init__(self, artist_name, html_string):
        self.artist_name = artist_name
        self.html_string = html_string

    def save_artworks(self):
        painting_count = 0
        print("Trying to find grid of links to artwork pages...")
        list_of_links = html.fromstring(self.html_string)
        print(list_of_links)
        for a in list_of_links.cssselect("a"):
            if "http" in a.get("href"):
                href = a.get("href")
            else:
                href = "https://www.wikiart.org" + a.get("href")
            print("Looking for artwork_url in", href)
            artwork_url = self.get_artwork_url(href)
            if artwork_url:
                print("Trying to save file from", artwork_url)
                self.save_file(artwork_url, painting_count)
            painting_count += 1


    def get_artwork_url(self, href):
        painting_response = requests.get(href)
        painting_html = html.fromstring(painting_response.text)
        time.sleep(1)
        artwork_url = False
        try:
            artwork_url = painting_html.cssselect("#image-link")[0].get("href")
        except:
            print("artwork_url not found")
        time.sleep(1)
        return artwork_url

    def save_file(self, artwork_url, painting_count):
        save_to = "./images/{}_{}.jpg".format(self.artist_name, painting_count)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(artwork_url, save_to)
        except:
            print("save file failed", artwork_url, save_to)
        time.sleep(1)
