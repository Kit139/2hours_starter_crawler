# import requests

# url = 'https://movie.douban.com/top250'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
#     'Cookie': '_vwo_uuid_v2=DF3BC37668EB9E0D898EF656883F8AC49|428bbf945ee750af7bfbbe49332d6458; bid=7CTQ6Kmi-pg; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22926; __gads=ID=a6183812fd6e7a86-22994bc86fcf00af:T=1639464898:RT=1639464898:S=ALNI_MZbHcWstraSiZzpyDyMmldmralvNA; ll="128496"; __yadk_uid=lF2MMZf02g84RCrFKQpre7fac93g74eG; __utmz=30149280.1642580411.14.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1288512643.1639464884.1642668260.1642683133.18; __utmc=30149280; dbcl2="229266949:wYmDhgQxvn0"; ck=6Zx6; __utmb=30149280.5.10.1642683133; __utma=223695111.1951251099.1637843614.1642668260.1642683203.8; __utmb=223695111.0.10.1642683203; __utmc=223695111; __utmz=223695111.1642683203.8.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642683203%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=c2b24a2232fc7d29.1637843613.8.1642683394.1642673455.',

# }

# res = requests.get(url, headers=headers)
# # print(res.text)

# from lxml import etree

# htmls = etree.HTML(res.text)
# score = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]/text()')
# title = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
# print(score, title)

# import pandas as pd

# # datas = [
# #     ['石河子大学','TOP1'],
# #     ['金融学', '牛B'],
# #     [100,'大学课程'],
# #         ]
# # df = pd.DataFrame(datas)

# # print(df)

# datas = {
#     'index': [1,2,3],
#     'name': ['小明', '小红', '小刚'],
#     'score': ['100', '99.9', '99.89']
# }
# df = pd.DataFrame(datas)
# print(df)

# import requests

# url = 'https://movie.douban.com/top250'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
#     'Cookie': '_vwo_uuid_v2=DF3BC37668EB9E0D898EF656883F8AC49|428bbf945ee750af7bfbbe49332d6458; bid=7CTQ6Kmi-pg; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22926; __gads=ID=a6183812fd6e7a86-22994bc86fcf00af:T=1639464898:RT=1639464898:S=ALNI_MZbHcWstraSiZzpyDyMmldmralvNA; ll="128496"; __yadk_uid=lF2MMZf02g84RCrFKQpre7fac93g74eG; __utmz=30149280.1642580411.14.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1288512643.1639464884.1642668260.1642683133.18; __utmc=30149280; dbcl2="229266949:wYmDhgQxvn0"; ck=6Zx6; __utmb=30149280.5.10.1642683133; __utma=223695111.1951251099.1637843614.1642668260.1642683203.8; __utmb=223695111.0.10.1642683203; __utmc=223695111; __utmz=223695111.1642683203.8.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642683203%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=c2b24a2232fc7d29.1637843613.8.1642683394.1642673455.',

# }
# res = requests.get(url=url, headers=headers)

# from lxml import etree

# htmls = etree.HTML(res.text)
# title = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
# scores = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
# comments = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')


# import pandas as pd

# datas = {
#     'title': title,
#     'scores': scores,
#     'comments': comments
# }
# df = pd.DataFrame(datas)
# df.to_csv('test2.csv', index=False)

# https://movie.douban.com/top250?start=0&filter=
# https://movie.douban.com/top250?start=25&filter=
# https://movie.douban.com/top250?start=50&filter=
# https://movie.douban.com/top250?start=75&filter=

# import requests


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
#     'Cookie': '_vwo_uuid_v2=DF3BC37668EB9E0D898EF656883F8AC49|428bbf945ee750af7bfbbe49332d6458; bid=7CTQ6Kmi-pg; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22926; __gads=ID=a6183812fd6e7a86-22994bc86fcf00af:T=1639464898:RT=1639464898:S=ALNI_MZbHcWstraSiZzpyDyMmldmralvNA; ll="128496"; __yadk_uid=lF2MMZf02g84RCrFKQpre7fac93g74eG; __utmz=30149280.1642580411.14.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1288512643.1639464884.1642668260.1642683133.18; __utmc=30149280; dbcl2="229266949:wYmDhgQxvn0"; ck=6Zx6; __utmb=30149280.5.10.1642683133; __utma=223695111.1951251099.1637843614.1642668260.1642683203.8; __utmb=223695111.0.10.1642683203; __utmc=223695111; __utmz=223695111.1642683203.8.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642683203%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=c2b24a2232fc7d29.1637843613.8.1642683394.1642673455.',

# }
# for page in range(2):
#     res = requests.get(url='https://movie.douban.com/top250?start={}&filter='.format(page*25), headers=headers)

#     from lxml import etree

#     htmls = etree.HTML(res.text)
#     title = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
#     scores = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
#     comments = htmls.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')


#     import pandas as pd

#     datas = {
#         'title': title,
#         'scores': scores,
#         'comments': comments
#     }
#     df = pd.DataFrame(datas)
#     df.to_csv('test_page{}.csv'.format(page+1), index=False)


import pandas as pd

df = pd.read_html('https://s.askci.com/stock/a/0-0?reportTime=2021-09-30&pageNum=2#QueryCondition')
df[-1]
