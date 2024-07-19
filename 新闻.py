import requests


import re
from bs4 import BeautifulSoup

response = requests.get('http://society.people.com.cn/')
homePage=response.text
# print(homePage)
soup = BeautifulSoup(homePage,'html.parser')
all_title1=soup.findAll("a")
for title1 in all_title1:
        print(title1.get("href"))


# for i in range(50):
#     title=json_data['list'][i]['title']
#     # for source
#     print(title)

# for i in range(50):
#     url=json_data['list'][i]['source']['url']
#     # for source
#     print(url)

    # response = requests.get(
    # url=url
    # )
    # soup=BeautifulSoup(response.text,'html.parser')
    # # print(soup)
    # all_title1 = soup.findAll('span')
    # for title1 in all_title1:
    #     if(title1.string!=None):
    #         print(title1.string.strip())


















