import requests
import bs4
site = 'https://pvp.qq.com/web201605/'
req = requests.get(site + 'herolist.shtml')
req.encoding = ''
soup = bs4.BeautifulSoup(req.text, 'html.parser')
targets = soup.find_all(attrs={'class': 'herolist clearfix'})[0]
alist = targets.find_all('a')
index = 0
with open('heros.txt', 'w+', encoding='utf-8') as f:
    while index < len(alist):
        req = requests.get(site + alist[index]['href'])
        req.encoding = 'gbk'
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        target_hero = soup.find_all(attrs={'class': 'cover'})[0]
        hero_nick = str(target_hero.h3.string)
        hero_name = str(target_hero.h2.string)
        f.writelines([hero_nick, hero_name, '\n'])
        print(hero_name)
        target_skills = soup.find_all(attrs={'class':'skill-show'})
        for i in target_skills:
            infos = i.find_all('p')
            for j in infos:
                lst = list(j.strings)
                f.writelines(lst)
                f.write('\n')
        index += 1