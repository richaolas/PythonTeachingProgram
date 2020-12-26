import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['fangsong']
url = 'https://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579582238&enterid=1579582238&from=timeline&isappinstalled=0'
res = requests.get(url)
res.encoding = 'utf-8'
pat0 = re.compile('window.getAreaStat = ([\s\S]*?)</script>')
data_list = pat0.findall(res.text)
data = data_list[0].replace('}catch(e){}','')
data = eval(data)
provinceShortNames = []
confirmedCounts = []
curedCounts = []
deadCounts = []

for i in data:
    provinceShortNames.append(i['provinceShortName'])
    confirmedCounts.append(i['confirmedCount'])
    curedCounts.append(i['curedCount'])
    deadCounts.append(i['deadCount'])
df = pd.DataFrame(index = provinceShortNames)
df['省份'] = provinceShortNames
df['确诊'] = confirmedCounts
df['治愈'] = curedCounts
df['死亡'] = deadCounts
import time
date = time.strftime('%Y%m%d')
# 保存成Excel表格
df.plot(figsize=(16,10))
df.to_excel(date+'疫情数据.xlsx')
index = [i for i in range(len(provinceShortNames))]
plt.xticks(index, provinceShortNames)
plt.show()
