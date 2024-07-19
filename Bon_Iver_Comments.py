import requests

import csv

if __name__ == '__main__':
    #创建保存文件以及相关配置
    f = open('data.csv',mode='a',encoding='utf-8',newline='')
    csv_writer = csv.DictWriter(f,fieldnames=[
            '昵称',
            '性别',
            '签名',
            '内容',
            '归属地',
    ])
    csv_writer.writeheader()
    import requests

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
        'bp_t_offset_603808299': '936187228560818226',
        'home_feed_column': '5',
        'browser_resolution': '1536-826',
        'b_lsid': 'DED2713B_18FCDF149AE',
        'bsource': 'search_google',
        'SESSDATA': 'c245bf45%2C1732699112%2Cb141e%2A52CjAvQaWmgbpGV8jNtKruTQ_iNzkyKDx1vjzzjVreqGns8j_153u5CHC92NPyg2uxrigSVm9JZ05LMVRHOTFmOTlGTDltdGNnZzN6UlhHTUJ6dkdQbWoyTG1zWUdNMDZ1dFNYR2FXcUtsWXVheDVqRzRoMnNYb1AyQWJydk5WRlQwRWs1YnI2SzlnIIEC',
        'bili_jct': '783b81e1c6cdedfa8f9bc15c105d713f',
        'sid': '5vfqz1bf',
        'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc0MDYzMjgsImlhdCI6MTcxNzE0NzA2OCwicGx0IjotMX0.J8emIWv-mO6iSigbRWAoM5eYcj2224jZTmeaBltQTh4',
        'bili_ticket_expires': '1717406268',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid_fp=f25cb8fb313f66295e06f88a14969022; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bp_t_offset_603808299=936187228560818226; home_feed_column=5; browser_resolution=1536-826; b_lsid=DED2713B_18FCDF149AE; bsource=search_google; SESSDATA=c245bf45%2C1732699112%2Cb141e%2A52CjAvQaWmgbpGV8jNtKruTQ_iNzkyKDx1vjzzjVreqGns8j_153u5CHC92NPyg2uxrigSVm9JZ05LMVRHOTFmOTlGTDltdGNnZzN6UlhHTUJ6dkdQbWoyTG1zWUdNMDZ1dFNYR2FXcUtsWXVheDVqRzRoMnNYb1AyQWJydk5WRlQwRWs1YnI2SzlnIIEC; bili_jct=783b81e1c6cdedfa8f9bc15c105d713f; sid=5vfqz1bf; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc0MDYzMjgsImlhdCI6MTcxNzE0NzA2OCwicGx0IjotMX0.J8emIWv-mO6iSigbRWAoM5eYcj2224jZTmeaBltQTh4; bili_ticket_expires=1717406268",
        'origin': 'https://www.bilibili.com',
        'priority': 'u=1, i',
        'referer': 'https://www.bilibili.com/video/BV1M44y1m7q8/?spm_id_from=333.337.search-card.all.click&vd_source=e35574fb766b5b6d49ca33f42c08e914',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://api.bilibili.com/x/v2/reply/wbi/main?oid=974296910&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=671bc42474b10ac6cd60f19f5102fe7c&wts=1717147142',
        cookies=cookies,
        headers=headers,
    )

    json_data = response.json()
    print(json_data)
    for index in json_data['data']['replies']:
        try:
            print(index['content']['message'])
        except:
            pass

# from bs4 import BeautifulSoup
# import requests
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
#     'bp_t_offset_603808299': '936187228560818226',
#     'home_feed_column': '5',
#     'browser_resolution': '1536-826',
#     'b_lsid': 'DED2713B_18FCDF149AE',
#     'bsource': 'search_google',
#     'SESSDATA': 'c245bf45%2C1732699112%2Cb141e%2A52CjAvQaWmgbpGV8jNtKruTQ_iNzkyKDx1vjzzjVreqGns8j_153u5CHC92NPyg2uxrigSVm9JZ05LMVRHOTFmOTlGTDltdGNnZzN6UlhHTUJ6dkdQbWoyTG1zWUdNMDZ1dFNYR2FXcUtsWXVheDVqRzRoMnNYb1AyQWJydk5WRlQwRWs1YnI2SzlnIIEC',
#     'bili_jct': '783b81e1c6cdedfa8f9bc15c105d713f',
#     'sid': '5vfqz1bf',
#     'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc0MDYzMjgsImlhdCI6MTcxNzE0NzA2OCwicGx0IjotMX0.J8emIWv-mO6iSigbRWAoM5eYcj2224jZTmeaBltQTh4',
#     'bili_ticket_expires': '1717406268',
# }
#
# headers = {
#     'accept': '*/*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid_fp=f25cb8fb313f66295e06f88a14969022; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bp_t_offset_603808299=936187228560818226; home_feed_column=5; browser_resolution=1536-826; b_lsid=DED2713B_18FCDF149AE; bsource=search_google; SESSDATA=c245bf45%2C1732699112%2Cb141e%2A52CjAvQaWmgbpGV8jNtKruTQ_iNzkyKDx1vjzzjVreqGns8j_153u5CHC92NPyg2uxrigSVm9JZ05LMVRHOTFmOTlGTDltdGNnZzN6UlhHTUJ6dkdQbWoyTG1zWUdNMDZ1dFNYR2FXcUtsWXVheDVqRzRoMnNYb1AyQWJydk5WRlQwRWs1YnI2SzlnIIEC; bili_jct=783b81e1c6cdedfa8f9bc15c105d713f; sid=5vfqz1bf; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc0MDYzMjgsImlhdCI6MTcxNzE0NzA2OCwicGx0IjotMX0.J8emIWv-mO6iSigbRWAoM5eYcj2224jZTmeaBltQTh4; bili_ticket_expires=1717406268",
#     'origin': 'https://www.bilibili.com',
#     'priority': 'u=1, i',
#     'referer': 'https://www.bilibili.com/video/BV1SK4y1A7Ex/?spm_id_from=pageDriver&vd_source=e35574fb766b5b6d49ca33f42c08e914',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
# }
#
# response = requests.get(
#     'https://api.bilibili.com/x/v2/reply/wbi/main?oid=888084478&type=1&mode=3&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:1,%5C%22direction%5C%22:1,%5C%22data%5C%22:%7B%5C%22pn%5C%22:7%7D%7D%22%7D&plat=1&web_location=1315875&w_rid=60bbccb89c46fdf4d3dc1fc65f45a58b&wts=1717147894',
#     cookies=cookies,
#     headers=headers,
# )
# homePage = response.text
# print(homePage)
# soup = BeautifulSoup(homePage, 'html.parser')
# all_title1 = soup.findAll("code")
# # deleted = all_title1.pop(0)
# for title1 in all_title1:
#     print(title1.string)
# json_data = response.json()
# # print(json_data)
# for index in json_data['data']['replies']:
#     try:
#         print(index['content']['message'])
#     except:
#         pass



