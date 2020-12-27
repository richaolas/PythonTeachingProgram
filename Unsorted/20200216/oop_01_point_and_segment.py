class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x=%f,y=%f' % (self.x, self.y)

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


p = Point(1, 1)
print(p)
print(p.distance(Point(3, 3)))


class Segment(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)

    def slope(self):
        if abs(self.p1.x - self.p2.x) < 1e-9:
            return None
        else:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)


s = Segment(Point(1, 5), Point(1, 3))
print(s.slope())
