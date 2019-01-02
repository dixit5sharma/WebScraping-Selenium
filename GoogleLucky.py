import bs4,requests,sys,pyperclip,webbrowser

print('Googling...')
if len(sys.argv) > 1:
    search = " ".join(sys.argv[1:])
else:
    search = pyperclip.paste()

res = requests.get("https://www.google.com/search?q=" + search)
res.raise_for_status()

SoupObject = bs4.BeautifulSoup(res.text,features="html.parser")
TopResults = SoupObject.select(".r a")

N_Tabs = min(5,len(TopResults))
for i in range(N_Tabs):
    # print(TopResults[i].get("href"))
    webbrowser.open('http://google.com' + TopResults[i].get("href"))