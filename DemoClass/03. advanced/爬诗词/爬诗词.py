# /usr/local/bin/python3.7
import os
import requests
import bs4
url = "https://so.gushiwen.org/mingju/Default.aspx?p=1&c=山水&t=庐山"
response = requests.get(url)
po = bs4.SoupStrainer(style = " float:left;")
soup = bs4.BeautifulSoup(response.text, "html.parser", parse_only=po)
index = 0
for i in soup.strings:
    print(i, end = ("-------" if index % 2 == 0 else "\n"))
    index += 1

# lst = soup.find_all("a", target="_blank")#attrs={"target":"_blank"}
# for i in range(len(lst)):
#     s = str(lst[i])
#     print(s[s.find("\">") + 2: s.find("</")], end = ("-------" if i % 2 == 0 else "\n"))
#
# print(time.time()-start)

# content = input("content?:\n")
# path = "/Users/star_xlliu/Documents/lxl/test/"
# file = "诗词.txt"
# try:
#     fh = open(path + file, "w")
# except IOError:
#     os.mkdir(path)
#     fh = open(path + file, "w")
# finally:
#     url = "https://www.gushiwen.org/mingju/"
#     response = requests.get(url)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     lst = soup.find_all("a", {"target":"_blank"})
#     for i in range(len(lst) - 1):
#         s = str(lst[i + 1])
#         txt = s[s.find("\">") + 2 : s.find("</")] + ("---" if i % 2 == 0 else "\n")
#         fh.write(txt)
#     fh.close()
#     print("写入成功")


