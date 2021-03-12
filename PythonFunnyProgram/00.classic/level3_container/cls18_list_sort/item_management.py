items = []

while True:
    item_name = input('input item name: ')
    if item_name == '':
        break
    item_price = float(input('input item price: '))
    items.append([item_name, item_price])

while True:
    sortby = input('input sort by: ')
    if sortby == 'name':
        items.sort(key=lambda item: item[0])
    elif sortby == 'price':
        items.sort(key=lambda item: item[1])
    else:
        break
    print(items)
