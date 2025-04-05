import requests as req
import time as tm

while True:
    response = req.get("https://coinmarketcap.com/")
    list = response.text.split("<span>")

    for i in list:
        for a in i.split("</span>"):
            if a.startswith("$"):
                print(a)

    tm.sleep(1)
    print("\n\n")