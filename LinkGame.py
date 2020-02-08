import os, random
import tkinter as tk
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk

class Point(object):
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x
        self.y = y

class MainWindow(object):
    root = tkinter.Tk()
    gameTitle = "连连看游戏"
    windowWidth = 480
    windowHeight = 480

    icons = []
    gameComplexity = 10  # 每一种头像有多少个
    gameSize = 10
    iconKind = gameSize * gameSize / gameComplexity
    iconWidth = iconHeight = 40

################################################################################
    def __init__(self):
        self.root.title(self.gameTitle)
        self.root.minsize(self.windowWidth, self.windowHeight)
        self.centerWindow(self.windowWidth, self.windowHeight)

    def centerWindow(self, w, h):
        screenW = self.root.winfo_screenwidth()
        screenH = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (screenW - w) / 2, (screenH - h) / 2)
        self.root.geometry(size)

    def show(self):
        self.root.mainloop()

################################################################################
    def addComponets(self):
        self.menubar = tkinter.Menu(self.root)
        self.file_menu = tkinter.Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label="新游戏", command=self.file_new)
        self.menubar.add_cascade(label='游戏', menu=self.file_menu)

        self.root.configure(menu=self.menubar)

        self.canvas = tkinter.Canvas(self.root, bg='black', width=450, height=450)
        self.canvas.pack(side=tkinter.TOP, pady=5)

        self.extractSmallIconList()

    def file_new(self, event=None):
        self.initMap()
        self.drawMap()

    def extractSmallIconList(self):
        imageSouce = Image.open('images/NARUTO.png')
        for index in range(0, int(self.iconKind)):
            region = imageSouce.crop(
                (self.iconWidth * index, 0, self.iconWidth * index + self.iconWidth - 1, self.iconHeight - 1))
            self.icons.append(ImageTk.PhotoImage(region))

    def initMap(self):
        tmpRecords = []
        records = []
        # 0 0 0 1 1 1 ...
        for i in range(0, int(self.iconKind)):
            for j in range(0, self.gameComplexity):
                tmpRecords.append(i)

        total = self.gameSize * self.gameSize
        for x in range(0, total):
            index = random.randint(0, total - x - 1)  # [0, total - x - 1]
            records.append(tmpRecords[index])
            del tmpRecords[index]

        self.map = []
        # 一维数组转为二维，y为高维度
        for y in range(0, self.gameSize):
            for x in range(0, self.gameSize):
                if x == 0:
                    self.map.append([])
                self.map[y].append(records[x + y * self.gameSize])  # 加入第几个

    def getOuterLeftTopPoint(self, point):
        return Point(self.getX(point.x), self.getY(point.y))

    def getX(self, x):
        return x * self.iconWidth

    def getY(self, y):
        return y * self.iconHeight

    def drawMap(self):
        self.canvas.delete('all')
        for y in range(0, self.gameSize):
            for x in range(0, self.gameSize):
                point = self.getOuterLeftTopPoint(Point(x, y))
                #print(len(self.icons), self.map[y][x])
                #print(type
                #      (self.icons[self.map[y][x]]))
                im = self.canvas.create_image((point.x, point.y),
                                              image=self.icons[self.map[y][x]], anchor='nw', tags='im%d%d' % (x, y))
################################################################################


if __name__ == "__main__":
    # MainWindow.fun()
    m = MainWindow()
    m.centerWindow(800, 600)
    m.addComponets()

    m.show()
