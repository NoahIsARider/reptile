import requests
from bs4 import BeautifulSoup
import re
cookies = {
    'buvid3': 'B19C71B3-3FDB-D7E3-750B-D3088FD2976672197infoc',
    'i-wanna-go-back': '-1',
    'b_ut': '7',
    '_uuid': 'D3499BFC-7673-F56F-8A55-FE19E1E27331070783infoc',
    'FEED_LIVE_VERSION': 'V8',
    'buvid_fp': '569ffbd86897913d8caeac22df9bcbed',
    'b_nut': '1690374971',
    'DedeUserID': '603808299',
    'DedeUserID__ckMd5': '4a8fed0a5ef54ebd',
    'header_theme_version': 'CLOSE',
    'buvid4': '4644F9BE-7926-0DF6-2E20-3488CFE6A2E973429-023072620-FZtXSQfpnQPKfr5OxQ04NA%3D%3D',
    'CURRENT_FNVAL': '4048',
    'rpdid': "|(u~mJkJu)RY0J'uYm|lul)|k",
    'enable_web_push': 'DISABLE',
    'PVID': '1',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5Mzg1MzQsImlhdCI6MTcxNzY3OTI3NCwicGx0IjotMX0.NFbe9sJ_tr2Ci5N-77WsfUCJOwizvS_ftV2nq0JPn78',
    'bili_ticket_expires': '1717938474',
    'SESSDATA': 'c5138048%2C1733231335%2C4b61a%2A62CjDMdRYcUdxNuGp-V8Za03jRZ4Og97Ba1uVWTRDj1y9w43TpshiWlMRxTDu4Reh5t0ASVnJhR1dJOThqcXZwVk9KdnRFbmJsaU1ZelAtaGR1R3pkbk9RM29lVXhuV3F5cWhjZTRxNW5SYzd6VVRLazVPTUd2cm1GQkkzcUNnUjVlRlMtNWlGMjJnIIEC',
    'bili_jct': '217c26ab8583b0b0ca35710518e644b8',
    'sid': '7fa2cpgi',
    'b_lsid': 'C4831381_18FF1A933BB',
    'home_feed_column': '5',
    'browser_resolution': '1482-842',
}

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': "buvid3=B19C71B3-3FDB-D7E3-750B-D3088FD2976672197infoc; i-wanna-go-back=-1; b_ut=7; _uuid=D3499BFC-7673-F56F-8A55-FE19E1E27331070783infoc; FEED_LIVE_VERSION=V8; buvid_fp=569ffbd86897913d8caeac22df9bcbed; b_nut=1690374971; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; header_theme_version=CLOSE; buvid4=4644F9BE-7926-0DF6-2E20-3488CFE6A2E973429-023072620-FZtXSQfpnQPKfr5OxQ04NA%3D%3D; CURRENT_FNVAL=4048; rpdid=|(u~mJkJu)RY0J'uYm|lul)|k; enable_web_push=DISABLE; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5Mzg1MzQsImlhdCI6MTcxNzY3OTI3NCwicGx0IjotMX0.NFbe9sJ_tr2Ci5N-77WsfUCJOwizvS_ftV2nq0JPn78; bili_ticket_expires=1717938474; SESSDATA=c5138048%2C1733231335%2C4b61a%2A62CjDMdRYcUdxNuGp-V8Za03jRZ4Og97Ba1uVWTRDj1y9w43TpshiWlMRxTDu4Reh5t0ASVnJhR1dJOThqcXZwVk9KdnRFbmJsaU1ZelAtaGR1R3pkbk9RM29lVXhuV3F5cWhjZTRxNW5SYzd6VVRLazVPTUd2cm1GQkkzcUNnUjVlRlMtNWlGMjJnIIEC; bili_jct=217c26ab8583b0b0ca35710518e644b8; sid=7fa2cpgi; b_lsid=C4831381_18FF1A933BB; home_feed_column=5; browser_resolution=1482-842",
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV19F411K7Q8/?spm_id_from=333.337.search-card.all.click&vd_source=e35574fb766b5b6d49ca33f42c08e914',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
}

params = {
    'type': '1',
    'oid': '778880508',
    'date': '2024-06-03',
}
content=[]
status=False
response = requests.get('https://api.bilibili.com/x/v2/dm/web/history/seg.so', params=params, cookies=cookies, headers=headers)
all_barrage=response.text.split('\n')
all_barrage=re.findall('[\u4e00-\u9fa5_a-zA-Z\s]+' ,response.text)
#'[\u4e00-\u9fa5]+'代表汉字
for barrage in all_barrage:
    # match=<string>re.search(':(.*?)@',barrage)
    # print(match)
    if len(barrage)>1:
        for _char in barrage:
            if '\u4e00' <= _char <= '\u9fa5':
                status=True
        if status==True:
            print(barrage.strip())
        if status==False:
            if len(barrage) > 5:
                print(barrage.strip())
    status=False

# import requests
#
# cookies = {
#     'buvid3': '4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc',
#     'b_nut': '1715926152',
#     '_uuid': 'BEC672FB-1C57-B983-479A-38341052109310D44226infoc',
#     'enable_web_push': 'DISABLE',
#     'buvid4': 'D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D',
#     'CURRENT_FNVAL': '4048',
#     'rpdid': "|(JJmulRY~YY0J'u~ulmkYJRY",
#     'header_theme_version': 'CLOSE',
#     'is-2022-channel': '1',
#     'DedeUserID': '603808299',
#     'DedeUserID__ckMd5': '4a8fed0a5ef54ebd',
#     'PVID': '3',
#     'bp_t_offset_603808299': '936187228560818226',
#     'SESSDATA': '3d215e10%2C1733227255%2Caae2d%2A62CjA3kGeJUEuK2SpQD1Q47vO4YaX55f6RscDX_sLeToPXU8nFsh1YX2N2row2dY8E7-sSVlppcUFFSDExN01VZXBJUDY0aFFUSXRrS3lFQUVuWTlYMHpsaDZySnBlVzdLY1JHUjRUbzdPblc0anRTTFRyWEY3SWFoSXN6NVItOGY0S0pZeWlZcWNnIIEC',
#     'bili_jct': 'dbced96de4ece043e746a7c59cad2690',
#     'home_feed_column': '5',
#     'browser_resolution': '1536-826',
#     'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5MzQ0ODksImlhdCI6MTcxNzY3NTIyOSwicGx0IjotMX0.3fP4YZDxnDlS4zhZBAZXZcWaTCGm-das84rncGMZunI',
#     'bili_ticket_expires': '1717934429',
#     'fingerprint': 'f25cb8fb313f66295e06f88a14969022',
#     'buvid_fp_plain': 'undefined',
#     'buvid_fp': 'f25cb8fb313f66295e06f88a14969022',
#     'b_lsid': 'FD49109F2_18FF5494A4F',
#     'bsource': 'search_google',
#     'sid': '6pys94hc',
# }
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     # 'cookie': "buvid3=4F7A0781-B5CC-F96C-2AC7-E38548D7175952841infoc; b_nut=1715926152; _uuid=BEC672FB-1C57-B983-479A-38341052109310D44226infoc; enable_web_push=DISABLE; buvid4=D38CB9CF-6663-40F6-A147-C9583B26D67653626-024051706-xDpFedVBgIU9SCh0aIXW9w%3D%3D; CURRENT_FNVAL=4048; rpdid=|(JJmulRY~YY0J'u~ulmkYJRY; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=603808299; DedeUserID__ckMd5=4a8fed0a5ef54ebd; PVID=3; bp_t_offset_603808299=936187228560818226; SESSDATA=3d215e10%2C1733227255%2Caae2d%2A62CjA3kGeJUEuK2SpQD1Q47vO4YaX55f6RscDX_sLeToPXU8nFsh1YX2N2row2dY8E7-sSVlppcUFFSDExN01VZXBJUDY0aFFUSXRrS3lFQUVuWTlYMHpsaDZySnBlVzdLY1JHUjRUbzdPblc0anRTTFRyWEY3SWFoSXN6NVItOGY0S0pZeWlZcWNnIIEC; bili_jct=dbced96de4ece043e746a7c59cad2690; home_feed_column=5; browser_resolution=1536-826; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5MzQ0ODksImlhdCI6MTcxNzY3NTIyOSwicGx0IjotMX0.3fP4YZDxnDlS4zhZBAZXZcWaTCGm-das84rncGMZunI; bili_ticket_expires=1717934429; fingerprint=f25cb8fb313f66295e06f88a14969022; buvid_fp_plain=undefined; buvid_fp=f25cb8fb313f66295e06f88a14969022; b_lsid=FD49109F2_18FF5494A4F; bsource=search_google; sid=6pys94hc",
#     'origin': 'https://www.bilibili.com',
#     'priority': 'u=1, i',
#     'referer': 'https://www.bilibili.com/video/BV19F411K7Q8/?spm_id_from=333.337.search-card.all.click&vd_source=e35574fb766b5b6d49ca33f42c08e914',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
# }
#
# params = {
#     'type': '1',
#     'oid': '778880508',
#     'date': '2024-06-03',
# }
# real_barrage=""
# status=False
# response = requests.get('https://api.bilibili.com/x/v2/dm/web/history/seg.so', params=params, cookies=cookies, headers=headers)
# # print(response.text)
# # all_barrage=response.text
# # for barrage in all_barrage:
# #     for char in barrage:
# #         if(status==True):
# #             real_barrage += char
# #             print(real_barrage)
# #         else:
# #             if (char==':'):
# #                 status=True
# #             else:
# #                 if(char=='@'):
# #                     status=False
# #                     break
# #     # print(real_barrage)
# # real_barrage = ""
#
# print(response.text)
# status=False
# # all_barrage=re.findall('[\u4e00-\u9fa5_a-zA-Z\s]+' ,response.text)
# all_barrage=response.text
# print(all_barrage)
# match = re.search(':(.*?)@', all_barrage)
# print(match)
# for ans in match:
#     print(ans)
#
# #         if '\u4e00' <= _char <= '\u9fa5':
# #             status=True
# #         if status==True:
# #             if(len(barrage)>1 and barrage!=""):
# #                 print(barrage.strip())
# #             break
# #     status=False













































