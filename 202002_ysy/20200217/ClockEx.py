# 封装就是将数据和行为整合到一起，并把一些内部元素做一定的私有化
class Clock(object):
    # 类属性数据，所有对象共享一份
    version = '1.0.1'

    # 构造函数
    def __init__(self, hour=0, minute=0, second=0):
        # 数据私有化
        # self.__hour = hour
        # self.setHour(hour)
        self.hour = hour
        # 对象(实例)属性数据, 每个对象单独拥有一份
        self.__minute = minute
        self.__second = second

    # def setHour(self, hour):
    #    if not isinstance(hour, int):
    #        raise ValueError('hour must int')
    #    if hour < 0 or hour > 23:
    #        raise ValueError('hour must less than 24 and larger than 0')
    #    self.__hour = hour

    # def getHour(self):
    #    return self.__hour

    # def show(self):
    #    print('%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second))

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if not isinstance(hour, int):
            raise ValueError('hour must int')
        if hour < 0 or hour > 23:
            raise ValueError('hour must less than 24 and larger than 0')
        self.__hour = hour

    def __str__(self):
        return '%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second)

    def __add__(self, sec):
        self.__second += sec
        if self.__second > 59:
            minute, second = divmod(self.__second, 60)
            self.__second = second
            self.__minute += minute
            if self.__minute > 59:
                hour, minute = divmod(self.__minute, 60)
                self.__minute = minute
                self.__hour += hour
                if self.__hour > 23:
                    self.__hour %= 24
        return self


class ClockEx(Clock):
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        # 以下三种方法都可以
        # Clock.__init__(self, hour, minute, second)           #1
        # super(ClockEx, self).__init__(hour, minute, second)  #2
        super().__init__(hour, minute, second)  # 3
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return '%04d-%02d-%02d' % (self.__year, self.__month, self.__day) + ' ' + (super().__str__())


if __name__ == '__main__':
    c1 = Clock()  # 用Clock创建对象，实例化的过程
    c2 = Clock(15, 20)
    c1.hour = 8
    c1 = c1 + (60 * 8 + 24)
    print(c1.hour, c1)
    # c1.setHour(15)
    # c1.show()
    # c2.show()
    cEx = ClockEx(2020, 2, 17, 8, 24, 0)
    print(cEx)
    print(Clock.__str__(cEx))
    print(super(ClockEx, cEx).__str__())
