import requests as rq

from bs4 import BeautifulSoup as bs

import pandas as pd

r = rq.get("https://jnrengineers.com.au/about-us/teach-with-us/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

content = r.content

lizt = []

bcontent = bs(content, "html.parser").find_all("div",{"class": "wpb_text_column wpb_content_element"})

target = bcontent[0]

for pos in target.find_all("h3"):
    dic = {}
    dic["Position:"] = pos.text.replace(":", "")
    lizt.append(dic)
for des in target.find_all("p")[:-3]:
    dic = {}
    if ":" in des.text:
        continue
    else:
        dic["Description"] = des.text
        lizt.append(dic)
for req in target.find_all("li",{"class":""})[4:]:
    dic = {}
    dic["Requirement:"] = req.text
    lizt.append(dic)

df = pd.DataFrame(lizt)

df.to_csv("Res.csv")





