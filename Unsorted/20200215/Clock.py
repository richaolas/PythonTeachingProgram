#封装就是将数据和行为整合到一起，并把一些内部元素做一定的私有化
class Clock(object):
    # 类属性数据，所有对象共享一份
    version = '1.0.1'

    # 构造函数
    def __init__(self, hour=0, minute=0, second=0):
        # 数据私有化
        # self.__hour = hour
        self.setHour(hour)
        # 对象(实例)属性数据, 每个对象单独拥有一份
        self.__minute = minute
        self.__second = second

    def setHour(self, hour):
        if not isinstance(hour, int):
            raise ValueError('hour must int')
        if hour < 0 or hour > 23:
            raise ValueError('hour must less than 24 and larger than 0')
        self.__hour = hour

    def getHour(self):
        return self.__hour

    def show(self):
        print('%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second))


if __name__ == '__main__':
    c1 = Clock()      #用Clock创建对象，实例化的过程
    c2 = Clock(15, 20)
    c1.setHour(15)
    c1.show()
    c2.show()
