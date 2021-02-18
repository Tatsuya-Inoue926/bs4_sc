from bs4 import BeautifulSoup
import requests
import urllib

url = "https://www.asahi.com/politics/list/"
r = requests.get(url)
soup = BeautifulSoup( r.content, "html.parser" )

data = soup.find_all("ul", class_ = "List")

maindata = data[0].find_all("a")

filename = "poli.txt"
with open( filename, "w", encoding="utf-8")as f:
    for d in maindata:
        title = d.text
        urls = d.get("href")
        link_url = urllib.parse.urljoin( url, urls )
        f.write("タイトル:" + title + "\n")
        f.write("URL:" + link_url + "\n")
        f.write("\n")