# import abc

class Shape(object):
    def __init__(self):
        super().__init__()

    def getArea(self):
        raise NotImplementedError('method getArea not implement')

    @staticmethod
    def getAllArea(shapes):
        ret = 0.0
        for s in shapes:
            ret += s.getArea()
        return ret


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        p = (self.a + self.b + self.c) * 0.5
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Rectangle(Shape):
    def __init__(self, w, h):
        super(Rectangle, self).__init__()
        self.w = w
        self.h = h

    def getArea(self):
        return self.w * self.h


if __name__ == '__main__':
    shapes = []
    shapes.append(Triangle(3, 4, 5))
    shapes.append(Triangle(7, 8, 9))
    shapes.append(Rectangle(5, 6))
    shapes.append(Rectangle(6, 9))
    area = Shape.getAllArea(shapes)
    print(area)

# 继承重点内容
# 1. 把子类看作两部分组成(父类部分，扩展部分）
# 2. 如何调用父类方法 三种
# 3. 静态方法的含义 (@staticmethod)