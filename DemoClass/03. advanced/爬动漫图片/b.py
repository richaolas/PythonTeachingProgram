import requests
import bs4

keyword = '花子'
site = 'https://www.zcool.com.cn'
condition = '/search/content?type=0&field=0&other=0&sort=5&word=' + keyword + '&recommend=0&time=0&requestId=requestId_1582351397803&p=1#tab_anchor'
key = 1
totalPage = 3
while key < totalPage:
    req = requests.get(site + (condition if key == 1 else page[0]['href']))
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    targets = soup.find_all(attrs={'class': 'card-img-hover'})
    index = 0
    for i in targets:
        img_req =  requests.get(i['href'])
        img_soup = bs4.BeautifulSoup(img_req.text, 'html.parser')
        img_targets = img_soup.find_all(attrs={'class': 'reveal-work-wrap text-center'})
        for j in img_targets:
            index += 1
            img = requests.get(url=j.img['src'])
            with open('image/' + keyword + '{0}_{1}.jpg'.format(key,index), 'ab+') as f:
                for chunk in img.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                print('第{0}页，第{1}张'.format(key, index))
    page = soup.find_all(attrs={'class': 'laypage_next'})
    key += 1
