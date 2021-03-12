products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("--------- 商品列表 --------")

products.sort(key=lambda item:item[1], reverse=True)

for index,i in enumerate(products):
    print("%s  %s    %s"%(index,i[0],i[1]))