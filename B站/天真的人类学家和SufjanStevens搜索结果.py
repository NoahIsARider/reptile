#爬取B站视频评论
import requests
import datetime
import csv
from bs4 import BeautifulSoup
import requests
#
# cookies = {
#     'buvid3': '4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc',
#     'b_nut': '1715926152',
#     '_uuid': 'BEC672FB-1C57-B983-479A-38341052109310D44226infoc',
#     'enable_web_push': 'DISABLE',
#     'buvid_fp': 'f25cb8fb313f66295e06f88a14969022',
#     'buvid4': 'D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D',
#     'CURRENT_FNVAL': '4048',
#     'rpdid': "|(JJmulRY~YY0J'u~ulmkYJRY",
#     'header_theme_version': 'CLOSE',
#     'is-2022-channel': '1',
#     'DedeUserID': '603808299',
#     'DedeUserID__ckMd5': '4a8fed0a5ef54ebd',
#     'PVID': '3',
#     'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MTExNTIsImlhdCI6MTcxNjU1MTg5MiwicGx0IjotMX0.QD760-XXAC76S3duy7fNoOnppZZPaZm-GbE4VAOF7b4',
#     'bili_ticket_expires': '1716811092',
#     'SESSDATA': 'f0e2c349%2C1732103958%2C20d0c%2A52CjDivEkgfvCt9DIwgdSiSDa5boLIxM6buaDMekHpYu6W-eZKWG7pAt5eFpzwuh_jixMSVmFYMnJPWEhDM21QbmNiS3RQQ2xKVzduOWtMNDRfMUNsMDJleHZiWE1oZGM0bTRtanpWbnAyblhjT2JOOHVoYVBlOHZkUURJQU9KM25jYzNYWFVveURnIIEC',
#     'bili_jct': 'db9edeb2de9ae96d0fe3e16a55dcd976',
#     'home_feed_column': '5',
#     'browser_resolution': '1536-826',
#     'b_lsid': '810F814DA_18FB4F6F824',
#     'bsource': 'search_google',
# }
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'max-age=0',
#     # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid_fp=f25cb8fb313f66295e06f88a14969022; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MTExNTIsImlhdCI6MTcxNjU1MTg5MiwicGx0IjotMX0.QD760-XXAC76S3duy7fNoOnppZZPaZm-GbE4VAOF7b4; bili_ticket_expires=1716811092; SESSDATA=f0e2c349%2C1732103958%2C20d0c%2A52CjDivEkgfvCt9DIwgdSiSDa5boLIxM6buaDMekHpYu6W-eZKWG7pAt5eFpzwuh_jixMSVmFYMnJPWEhDM21QbmNiS3RQQ2xKVzduOWtMNDRfMUNsMDJleHZiWE1oZGM0bTRtanpWbnAyblhjT2JOOHVoYVBlOHZkUURJQU9KM25jYzNYWFVveURnIIEC; bili_jct=db9edeb2de9ae96d0fe3e16a55dcd976; home_feed_column=5; browser_resolution=1536-826; b_lsid=810F814DA_18FB4F6F824; bsource=search_google",
#     'priority': 'u=0, i',
#     'referer': 'https://www.bilibili.com/',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
# }
#
# params = {
#     'keyword': '天真的人类学家',
#     'from_source': 'webtop_search',
#     'spm_id_from': '333.1007',
#     'search_source': '3',
# }
#
# response = requests.get('https://search.bilibili.com/all', params=params, cookies=cookies, headers=headers)
# homePage=response.text
# # print(homePage)
# soup = BeautifulSoup(homePage,'html.parser')
# all_title1=soup.findAll("h3")
# # deleted=all_title1.pop(0)
# # for title1 in all_title1:
# #     print(title1["title"])

import requests
count=0
count2=0
cookies = {
    'buvid3': '4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc',
    'b_nut': '1715926152',
    '_uuid': 'BEC672FB-1C57-B983-479A-38341052109310D44226infoc',
    'enable_web_push': 'DISABLE',
    'buvid_fp': 'f25cb8fb313f66295e06f88a14969022',
    'buvid4': 'D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D',
    'CURRENT_FNVAL': '4048',
    'rpdid': "|(JJmulRY~YY0J'u~ulmkYJRY",
    'header_theme_version': 'CLOSE',
    'is-2022-channel': '1',
    'DedeUserID': '603808299',
    'DedeUserID__ckMd5': '4a8fed0a5ef54ebd',
    'PVID': '3',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MTExNTIsImlhdCI6MTcxNjU1MTg5MiwicGx0IjotMX0.QD760-XXAC76S3duy7fNoOnppZZPaZm-GbE4VAOF7b4',
    'bili_ticket_expires': '1716811092',
    'SESSDATA': 'f0e2c349%2C1732103958%2C20d0c%2A52CjDivEkgfvCt9DIwgdSiSDa5boLIxM6buaDMekHpYu6W-eZKWG7pAt5eFpzwuh_jixMSVmFYMnJPWEhDM21QbmNiS3RQQ2xKVzduOWtMNDRfMUNsMDJleHZiWE1oZGM0bTRtanpWbnAyblhjT2JOOHVoYVBlOHZkUURJQU9KM25jYzNYWFVveURnIIEC',
    'bili_jct': 'db9edeb2de9ae96d0fe3e16a55dcd976',
    'home_feed_column': '5',
    'browser_resolution': '1536-826',
    'b_lsid': 'E63C10F7F_18FB75D7A82',
    'bsource': 'search_google',
    'sid': '6nve0v6c',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid_fp=f25cb8fb313f66295e06f88a14969022; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MTExNTIsImlhdCI6MTcxNjU1MTg5MiwicGx0IjotMX0.QD760-XXAC76S3duy7fNoOnppZZPaZm-GbE4VAOF7b4; bili_ticket_expires=1716811092; SESSDATA=f0e2c349%2C1732103958%2C20d0c%2A52CjDivEkgfvCt9DIwgdSiSDa5boLIxM6buaDMekHpYu6W-eZKWG7pAt5eFpzwuh_jixMSVmFYMnJPWEhDM21QbmNiS3RQQ2xKVzduOWtMNDRfMUNsMDJleHZiWE1oZGM0bTRtanpWbnAyblhjT2JOOHVoYVBlOHZkUURJQU9KM25jYzNYWFVveURnIIEC; bili_jct=db9edeb2de9ae96d0fe3e16a55dcd976; home_feed_column=5; browser_resolution=1536-826; b_lsid=E63C10F7F_18FB75D7A82; bsource=search_google; sid=6nve0v6c",
    'priority': 'u=0, i',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
for page_index in range(1,20):
    params = {
        'keyword': 'Sufjan Stevens',
        'from_source': 'webtop_search',
        'spm_id_from': '333.1007',
        'search_source': '2',
        'page':str(page_index),
        'o': str(page_index*30-30),
    }

    response = requests.get('https://search.bilibili.com/all', params=params, cookies=cookies, headers=headers)
    homePage = response.text
    print(homePage)
    soup = BeautifulSoup(homePage, 'html.parser')
    all_title1 = soup.findAll("h3")
    all_playNum=soup.findAll("span",attrs="bili-video-card__stats--item")
    deleted=all_title1.pop(0)
    for title1 in all_title1:
        print(title1["title"])
        count=count+1
    for palyNum in all_playNum:
        # print(palyNum)
        # print(palyNum.find("span"))
        # print(palyNum.find("span").string)
        if(count2%2==0):
            # print(palyNum.find("span"))
            print(palyNum.find("span").string)
        count2=count2+1
    # print(count)
    # print(count2)
print(count)
print(count2/2)
# for page_index in range(2,20):
#     url="https://search.bilibili.com/all?keyword=Sufjan+Stevens&from_source=webtop_search&spm_id_from=333.1007&search_source=2&page="+str(page_index)+"&o="+str(page_index*30-30)
#     response = requests.get(url=url, params=params, cookies=cookies, headers=headers)
#     homePage=response.text
#     # print(homePage)
#     soup = BeautifulSoup(homePage,'html.parser')
#     all_title1=soup.findAll("h3")
#     # deleted=all_title1.pop(0)
#     for title1 in all_title1:
#         print(title1["title"])



