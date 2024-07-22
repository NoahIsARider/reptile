import requests
from bs4 import BeautifulSoup
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
    'b_lsid': 'AA75DA29_18FB420DE36',
    'bsource': 'search_google',
    'bmg_af_switch': '1',
    'bmg_src_def_domain': 'i0.hdslb.com',
    'sid': '65642lr3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid_fp=f25cb8fb313f66295e06f88a14969022; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MTExNTIsImlhdCI6MTcxNjU1MTg5MiwicGx0IjotMX0.QD760-XXAC76S3duy7fNoOnppZZPaZm-GbE4VAOF7b4; bili_ticket_expires=1716811092; SESSDATA=f0e2c349%2C1732103958%2C20d0c%2A52CjDivEkgfvCt9DIwgdSiSDa5boLIxM6buaDMekHpYu6W-eZKWG7pAt5eFpzwuh_jixMSVmFYMnJPWEhDM21QbmNiS3RQQ2xKVzduOWtMNDRfMUNsMDJleHZiWE1oZGM0bTRtanpWbnAyblhjT2JOOHVoYVBlOHZkUURJQU9KM25jYzNYWFVveURnIIEC; bili_jct=db9edeb2de9ae96d0fe3e16a55dcd976; home_feed_column=5; browser_resolution=1536-826; b_lsid=AA75DA29_18FB420DE36; bsource=search_google; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; sid=65642lr3",
    'priority': 'u=0, i',
    'referer': 'https://search.bilibili.com/all?keyword=hyperpop&from_source=webtop_search&spm_id_from=333.1007&search_source=5',
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

params = {
    'spm_id_from': '333.337.search-card.all.click',
    'vd_source': 'e35574fb766b5b6d49ca33f42c08e914',
}

response = requests.get('https://www.bilibili.com/video/BV1rL4y1N7pV/', params=params, cookies=cookies, headers=headers)
homePage=response.text
print(homePage)
soup = BeautifulSoup(homePage,'html.parser')
all_title1=soup.findAll("p",attrs={"class":"title"})
deleted=all_title1.pop(0)
for title1 in all_title1:
    print(title1.string)
# json_data = response.json()
# for index in json_data['data']['related']:
#     try:
#         print(index['title'])
#     except:
#         pass
