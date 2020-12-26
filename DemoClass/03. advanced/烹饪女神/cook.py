from flask import Flask
from flask import render_template
import requests,bs4
import time
import random

app = Flask(__name__)
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


@app.route('/', methods=['GET', 'POST'])
def mainroot():
    return render_template('cook.html')

def searchContent(txt):
    keyword = txt
    site = 'http://www.xiachufang.com'
    condition = '/search/?keyword=' + keyword
    key = 1
    isContinue = True
    maxScan = -1
    maxScanUrl = ''
    dict = {}
    while isContinue == True:
        headers = {'user-agent': random.choice(my_headers)}
        req = requests.get(site + (condition if key == 1 else page['href']), headers = headers)
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        targets = soup.find_all(attrs={'class': 'recipe recipe-215-horizontal pure-g image-link display-block'})
        for i in targets:
            s = i.find_all(attrs={'class':'stats'})[0]
            num = float(s.span.text)
            if num > maxScan:
                maxScan = num
                maxScanUrl = i.a['href']
        try:
            page = soup.find_all(attrs={'class': 'next'})[0]
            page['href']
        except KeyError:
            isContinue = False
        except IndexError:
            isContinue = False
        key += 1
    dict['做过人数'] = maxScan
    print(site+maxScanUrl, maxScan)
    headers = {'user-agent': random.choice(my_headers)}
    req =  requests.get(site + maxScanUrl, headers = headers)
    content_soup = bs4.BeautifulSoup(req.text, 'html.parser')
    target = content_soup.find_all(attrs={'itemtype': 'http://schema.org/Recipe'})
    if len(target) > 0:
        target = target[0]
        dict['标题'] = target.h1.text
    else:
        dict['标题'] = txts
    detail = content_soup.find(attrs={'class':'block recipe-show'})
    dict['作者'] = detail.find(attrs={'itemtype':'http://schema.org/Person'}).a.span.text
    ings = detail.find(attrs={'class':'ings'})
    names = ings.find_all(attrs={'class':'name'})
    units = ings.find_all(attrs={'class':'unit'})
    ingLst = []
    for i in range(len(names)):
        ingLst.append(names[i].text + " " + units[i].text)
    dict['用料'] = ingLst
    steps = detail.find_all(attrs={'class':'steps'})[0]
    stepTextImg = steps.find_all(attrs={'class':'container'})
    texts = []
    imgUrls = []
    for i in range(len(stepTextImg)):
        texts.append(stepTextImg[i].p.text)
        try:
            imgUrls.append(stepTextImg[i].img['src'])
        except:
            pass

    dict['做法文字'] = texts
    dict['做法配图'] = imgUrls
    return dict


@app.route('/searh/<txt>')
def search(txt):
    print(txt)
    dict = searchContent(txt)
    return render_template('cook.html',
                           name=txt,
                           title=dict['标题'],
                           num=dict['做过人数'],
                           author=dict['作者'],
                           foodType=dict['用料'],
                           foodWay=dict['做法文字'])

def sc():
    txt = input('想吃啥菜：')
    global dict
    dict = searchContent(txt)


if __name__ == '__main__':
    app.run()