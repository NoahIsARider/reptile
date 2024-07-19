import requests
import re
from bs4 import BeautifulSoup
import json
response=requests.get("https://a24films.com/films")
homePage=response.text
#print(homePage)
soup = BeautifulSoup(homePage,'html.parser')
all_title1=soup.findAll("h3")
all_time1=soup.findAll("h6",attrs={"class":"date"})
for title1 in all_title1:
    print(title1.string)
#tag_list=[tag.extract() for tag in soup.select("time")]
#tag_list2=[tag.extract() for tag in soup.select("sup")]
all_title2=soup.findAll("h2",attrs={"class":"title"})
all_time=soup.findAll("time")
for title2 in all_title2:
    print(title2.contents[0].strip())
# for time1 in all_time1:
#     print(time1.string)
# for time2 in all_time:
#     print(time2.string)
# all_title3=soup.findAll("h2")
# for title3 in all_title3:
#     if title3.string!=None :
#      print(title3.string)
