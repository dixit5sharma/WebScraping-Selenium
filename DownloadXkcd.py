import  bs4,requests,os

url = 'http://xkcd.com'
os.makedirs('Files\\xkcd', exist_ok=True)   # exist_ok=True is used if it exists, does not give an error.

while not url.endswith('#'):
    print('Downloading page %s...' %url)
    res = requests.get(url)
    SoupObject = bs4.BeautifulSoup(res.text, features="html.parser")

    """ This portion below is to avoid a bug in the actual site with Comic url 2067 """
    if url.__contains__("2067"):
        Prev = SoupObject.select("a[rel='prev']")[0]
        url = "http://xkcd.com" + Prev.get("href")
        continue
    """ This portion above is to avoid a bug in the actual site with Comic url 2067 """

    Image = SoupObject.select("#comic img")

    if len(Image)>0:
        ComicUrl = "http:" + Image[0].get("src")
        print('Downloading image %s...' %ComicUrl )
        res = requests.get(ComicUrl)
        res.raise_for_status()
        with open(os.path.join("Files\\xkcd", os.path.basename(ComicUrl)), "wb") as File:
            for data in res.iter_content(100000):
                File.write(data)
    else:
        print("Could not find comic image.")

    # Prev = SoupObject.select(".comicNav li a")[1]
    Prev = SoupObject.select("a[rel='prev']")[0]
    url = "http://xkcd.com" + Prev.get("href")
print("Done")