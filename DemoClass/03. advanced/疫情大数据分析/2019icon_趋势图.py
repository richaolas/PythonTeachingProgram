# -*- coding: utf-8 -*-
from datetime import datetime
import time,json,requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


import urllib, sys
import ssl

# import urllib.request
# resp=urllib.request.urlopen('http://www.baidu.com')
# html=resp.read()
# print(html)
#
# sys.exit()

host = 'https://ncovdata.market.alicloudapi.com'
path = '/ncov/cityDiseaseInfoWithTrend'
method = 'GET'
appcode = 'f9cc3fa2ef32419f845d5234bf0f888b'
querys = ''
bodys = {}
url = host + path

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    #print(content)
    provinceArray = json.loads(content)['provinceArray']
    hubei = [s for s in provinceArray if s['childStatistic'] == '湖北省']
    hubei_citys = hubei[0]['cityArray']
    print(hubei_citys)
sys.exit()

plt.rcParams[ 'font.sans-serif'] = [ 'FangSong'] # 设置默认字体
plt.rcParams[ 'axes.unicode_minus'] = False# 解决保存图像时'-'显示为方块的问题

#腾讯冠状病毒地址：https://news.qq.com/zt2020/page/feiyan.htm#/

def catch_daily():
    """抓取每日确诊和死亡数据"""
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()* 1000)
    data = json.loads(requests.get(url).json()['data'])
    data.sort(key=lambda x: x["date"])
    date_list = list()  # 日期
    confirm_list = list()  # 确诊
    suspect_list = list()  # 疑似
    dead_list = list()  # 死亡
    heal_list = list()  # 治愈
    for item in data:
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s' %(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    return date_list, confirm_list, suspect_list, dead_list, heal_list

def catch_all():
    """抓取所有数据"""
    data = dict() #存储数据
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d" % int(time.time() * 1000)
    response = json.loads(requests.get(url=url).json()['data'])
    print("确认：", response)
    china = response.get("areaTree")[0]
    print(china.get("children")[0])#湖北数据
    for provs in china.get("children"):
        # print(provs)
        if provs["name"] not in data:
            data.update({provs["name"]+"省":0})
            data[provs["name"]+"省"] += int(provs["total"]["confirm"])
        # if item['area'] not in data:
        #     data.update({item['area']: 0})
        #     data[item['area']] += int(item['confirm'])
    print(data)
    return data

# print(catch_all())

def catch_distribution():
    """抓取行政区域确诊分布数据"""
    data = dict() #存储数据
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d"%int(time.time()*1000)
    print(url)
    for item in json.loads(requests.get(url=url).json()['data']):
        if item['area'] not in data:
            data.update({item['area']: 0})
            data[item['area']] += int(item['confirm'])
    return data



def draw_plot_daily():
    """绘制每日确诊和死亡数据"""
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() # 获取数据
    print(date_list)
    print(confirm_list)
    print(suspect_list)
    print(date_list)
    plt.figure( '2020-nCoV疫情统计图表', facecolor= '#f0f0f0', figsize=( 10, 8))
    plt.title( '2020-nCoV疫情曲线', fontsize= 45)
    plt.plot(date_list, confirm_list, label= '确诊')
    plt.plot(date_list, suspect_list, label= '疑似')
    plt.plot(date_list, dead_list, label= '死亡')
    plt.plot(date_list, heal_list, label= '治愈')
    #matplotlib 调用 gca() 函数以及 gcf() 函数来获取当前的坐标轴和图像
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  #格式化时间轴标注
    plt.gcf().autofmt_xdate() # 优化标注（自动倾斜）
    plt.grid(linestyle= '--') # 显示网格,supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    plt.legend(loc= 'best',edgecolor='blue',facecolor='grey') # 设置图例位置loc  设置图例字体fontsize  设置图例边框及背景   设置图例标题
    plt.savefig( '2020-nCoV疫情曲线.png') # 保存为文件
    plt.show()

if __name__ == '__main__':
    draw_plot_daily()
    #catch_all()