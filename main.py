import urllib.request
import time
import os


from bs4 import BeautifulSoup


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
}


def download_image(soup, class_name):
    links = soup.find_all("img", attrs={"class":f"{class_name}"})

    for i in links:
        src = urllib.request.Request(url=i.attrs['src'], headers=header)
        filename = os.path.basename(src.full_url)
        data = urllib.request.urlopen(src).read()
        with open(filename, mode="wb") as f:
            f.write(data)
        time.sleep(0.5)


def parse_html(url, headers=header):
    html = get_html(url, headers=header)
    return BeautifulSoup(html, 'html.parser')


def get_html(url, headers=header):
    req = urllib.request.Request(url=url, headers=header)
    http_obj = urllib.request.urlopen(req)
    data = http_obj.read()
    return data.decode('utf-8')