# import requests
import bs4

# res = requests.get('https://www.google.co.in/')
# res.raise_for_status()

with open("Files\\example.html") as exampleFile:
    SoupObject = bs4.BeautifulSoup(exampleFile,features="html.parser")
    print(type(SoupObject))
    # SoupObject.select("div")    # All div elements
    # SoupObject.select("#author")    # Element with id attribute of author
    # SoupObject.select(".notice")    # All Elements with class attribute of notice
    # SoupObject.select("div span")   # All Elements with span inside div element
    # SoupObject.select("div > span")     # All elements with span directly within div with no other element
    # SoupObject.select("input[name]")    # All input element with name attribute defined with any value
    # SoupObject.select("input[type='button']")   # All button input elements
    # SoupObject.select("p .myforecast-current-lrg")
    TagElement = SoupObject.select("#author")
    print(type(TagElement))
    print(TagElement[0].getText())
    print(TagElement[0].attrs)
    print(str(TagElement[0]))

    print("------------- p Soup Element starts here -------------")
    pElement = SoupObject.select("p")
    for each in pElement:
        print(str(each))
        print(each.getText())
        # print(each.attrs)
        # print(len(each.attrs))
        if len(each.attrs)>0:
            # for Keyattr,Valattr in each.attrs.items():
            #     print(Keyattr,"=",Valattr)
            print(each.attrs.get("class"))  # If not there, None will be returned

    SpanElement = SoupObject.select("span")[0]      # Can define first element here as well. Now, no [] needed
    print(str(SpanElement))
    print(SpanElement.get("id"))
    print(SpanElement.attrs)