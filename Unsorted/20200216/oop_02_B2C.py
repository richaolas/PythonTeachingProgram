class User(object):
    def __init__(self, username, address, payMode):
        self.username = username
        self.address = address
        self.payMode = payMode
        self.carts = {}  # [] key:cart

    def createCart(self, name):
        self.carts[name] = Cart(name)  # key:cart

    def buy(self, name, item):
        self.carts[name].push(item)

    def showAllCarts(self):
        for name, cart in self.carts.items():
            print('------------------------')
            print('In cart %s:' % name)
            for item in cart.items:
                print(item)
        print('------------------------')


class Item(object):
    def __init__(self, name, price, number = 1):
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return 'Item: %s, Price: %f, Count: %d' % (self.name, self.price, self.number)

class Cart(object):
    def __init__(self, name):
        self.name = name
        self.items = []

    def push(self, item):
        self.items.append(item)


user = User('lisi', 'beijing', 'zhifubao')
user.createCart('mycart')
user.buy('mycart', Item('iphonex', 8999.0, 2))
user.buy('mycart', Item('book', 99.0))

user.createCart('mymothercart')
user.buy('mymothercart', Item('shampoo', 89.0, 3))

user.showAllCarts()
#user.pay
