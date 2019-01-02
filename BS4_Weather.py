import requests,bs4

res = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.78862000000004&lon=-122.39508999999998#.XB_i91UzbIU")
res.raise_for_status()

SoupObject = bs4.BeautifulSoup(res.text,features="html.parser")
TagList = SoupObject.select(".myforecast-current-lrg")
for each in TagList:
    print(each.getText())
    print(each.attrs)