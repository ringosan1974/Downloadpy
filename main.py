import urllib.request
import time
import os


from bs4 import BeautifulSoup


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
}


class Downloader():
    def __init__(self, url, header=header, dirname=""):
        self.url = url
        self.header = header
        self.dirname = dirname


    def download_image(self, attrs):
        soup = self._parse_html()
        links = soup.find_all("img", attrs=attrs)

        for i in links:
            src = urllib.request.Request(url=i.attrs['src'], headers=self.header)
            filename = os.path.basename(src.full_url)
            data = urllib.request.urlopen(src).read()
            if len(self.dirname) > 0:
                self.dirname += "\\"
            with open(f"{self.dirname}{filename}", mode="wb") as f:
                f.write(data)
            time.sleep(1)


    def _parse_html(self):
        html = self._get_html()
        return BeautifulSoup(html, 'html.parser')


    def _get_html(self):
        req = urllib.request.Request(url=self.url, headers=self.header)
        http_obj = urllib.request.urlopen(req)
        data = http_obj.read()
        return data.decode('utf-8')


if __name__ == "__main__":
    url = input("url :")
    head = input("head :")
    value = input("value :")
    attrs = {head:value}
    downloader = Downloader(url, dirname="D:\\images\\other\\")
    try:
        downloader.download_image(attrs)
    except ValueError as e:
        print("正しくURLを入力してください\n", e)
    except urllib.request.HTTPError as e:
        print("HTTPError:", e)