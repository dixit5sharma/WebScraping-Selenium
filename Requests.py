import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()      # Automatically raises HTTPError exception if status is not 200 (Eg. 404)
except Exception as Exc:
    print("There was a problem: %s" %Exc)

print(type(res))    # Response Object
print(type(res.text))   # String
print(type(res.status_code))    # Integer
print(res.status_code)      # 200 is status OK

if res.status_code == requests.codes.ok:    # Not needed if res.raise_for_status() exists outside try except block
    if len(res.text)>0:
        print("Length of full response as text is " + str(len(res.text)))
        txt = res.text
        print("A part of the text is -->\n"+txt[:71])
        with open("Files\\RomeoJuliet.txt","wb") as f:
            # print(type(res.iter_content(50000)))    # Generator
            # print(list(res.iter_content(1000)))     # list of items each having 1000 characters string data
            for r in res.iter_content(50000):
                f.write(r)