# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:54:30 2019

@author: ric_r
"""
import sys
import pygame
import time
import re


class TextGeneratorFromFile():
    '''
    从文本产生单词
    '''
    def __init__(self, path, numWords):
        self.path = path
        self.pos = 0
        self.numWords = numWords
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = re.findall(r'\w+', f.read())

    def getText(self):
        if self.pos + self.numWords >= len(self.text):
            self.pos = 0
        text = " ".join(self.text[self.pos: self.pos+self.numWords])
        self.pos += self.numWords
        return text

class BLock():
    '''
    字符对(源字符和输入字符)块
    '''
    def __init__(self, content, loc):
        self.text = content
        self.input = ''
        self.loc = loc
        self.cHeight = pygame.font.Font(None, 36).get_height() 
        self.cWidth = pygame.font.Font(None, 36).size('W')[0] # for simple, just use W represent max height of char
        
    def update(self, surface):  
        textClr = (0,0,0)
        if len(self.input) > 0:
            if self.input == self.text:
                textClr = (0,0,255)
            else:
                textClr = (255,255,255)
            
        charSurface = pygame.font.Font(None, 36).render(self.text, 1, textClr)
        charW = charSurface.get_size()[0]
        surface.blit(charSurface, (self.loc[0] + (self.cWidth - charW)/2, self.loc[1]))
            
        if len(self.input) > 0:
            inputCharSurface = pygame.font.Font(None, 36).render(self.input, 1, (0,0,0))
            charW = inputCharSurface.get_size()[0]
            surface.blit(inputCharSurface, (self.loc[0] + (self.cWidth - charW)/2, self.loc[1] + self.cHeight))
            
class InfoArea(pygame.sprite.Sprite):
    '''
    游戏信息显示区
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = "Speed: %.1f/min, correct words: %s/%s, time: %d s" % (0, 0, 0, 0)
        self.update()

    def update(self):
        self.image = pygame.font.Font(None, 26).render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

    def setText(self, speed, correct, total, passTime):
        self.text = "Speed: %.1f/min, correct words: %s/%s, time: %d s" % (
            speed, correct, total, passTime)    
   
class Button():
    '''
    按钮
    '''
    def __init__(self, loc, size, text):
        self.loc = loc
        self.size = size
        self.text = text
    
    def isPressd(self, loc):
        return self.inRect(loc, (self.loc[0],self.loc[1], self.size[0], self.size[1]))    
    
    def inRect(self, pos, rect):
        x,y = pos
        rx,ry,rw,rh = rect
        if (rx <= x <=rx+rw)and(ry <= y <= ry +rh):
            return True
        return False   
    
    def update(self, surface):
        pygame.draw.rect(surface, (255,255,255), (self.loc[0],self.loc[1], self.size[0], self.size[1]))
        charSurface = pygame.font.Font(None, 36).render(self.text, 1, (0,0,0))
        w, h = charSurface.get_size()
        surface.blit(charSurface, (self.loc[0] + (self.size[0]-w)/2, self.loc[1] + (self.size[1] - h)/2))
        
class TextArea():

    def __init__(self, words):
        self.resetWords(words)
        
    def resetWords(self, words):
        self.surface = pygame.display.get_surface()        
        width, height = self.surface.get_size()
        self.hMargin = 20
        self.vMargin = 80
        self.max_width = width - self.hMargin * 2
        self.maxrow = 5
        self.cHeight = pygame.font.Font(None, 36).get_height() 
        self.cWidth = pygame.font.Font(None, 36).size('W')[0] # for simple, just use W represent max height of char

        self.input = ''
        self.words = []
        self.blocks = []
        
        x = self.hMargin #(width - self.max_width) // 2
        y = self.vMargin
        row = 0
        for word in words:
            w = (len(word) + 1) * self.cWidth
            if (x + w <= self.max_width):
                self.words.append(word)
                for c in word + ' ':
                    block = BLock(c, (x,y))
                    self.blocks.append(block)
                    x += self.cWidth
            else:
                x = self.hMargin
                y += self.cHeight * 3
                row += 1
                if (row >= self.maxrow):
                    break
        
        if len(self.words) > 0:
            self.wordsLine = ' '.join(self.words) + ' '
        else:
            self.wordsLine = ''
        print(self.wordsLine)
   
    def keydown(self, char):
        if char == '\n' or char == '\r' or char == '\t':
            char = ' '
        if char == '\b':
            self.input = self.input[:-1]
            self.blocks[len(self.input)].input = ''
        else:
            if (len(self.input) == len(self.blocks)):
                return False
            self.input += char
            idx = len(self.input)
            self.blocks[idx-1].input = char 
        return True
            
    def check(self):
        beg = -1
        idx = 0
        count = 0
        while True:
            beg = self.wordsLine.find(' ', beg + 1)
            if beg < 0 or beg > len(self.input):
                break
            if (self.wordsLine[beg-len(self.words[idx]):beg] == self.input[beg-len(self.words[idx]):beg]):
                count += 1
            idx += 1         
        return count, idx
   
    def update(self):
        for b in self.blocks:
            b.update(self.surface)
        
        nextIdx = len(self.input) 
        if (nextIdx >= len(self.blocks)): #到最后一个光标就停在最后一个
            nextIdx = len(self.blocks) - 1
        if len(self.blocks) > 0: #显示光标
            pygame.draw.line(self.surface, (0,0,0), (self.blocks[nextIdx].loc[0], self.blocks[nextIdx].loc[1] + self.cHeight * 2), (self.blocks[nextIdx].loc[0] + self.cWidth, self.blocks[nextIdx].loc[1] +  + self.cHeight * 2), 3)    


class TypingGame():
    '''
    图形用户界面
    '''
    def __init__(self, textSource):
        self.clock = pygame.time.Clock()
        self.screenRect = pygame.Rect(0, 0, 640, 480)
        self.screen = pygame.display.set_mode(self.screenRect.size)
        self.elements = pygame.sprite.RenderUpdates()
        self.infoArea = InfoArea()
        self.elements.add(self.infoArea)
        self.startBtn = Button((550,10), (80, 40), 'start')
        self.timeout = Button((50,200),(540, 80), 'Time Out')
    
        self.maxSpeed = 60  * 5
        self.totolTime = 60
        self.beginTime = 0
        self.speed = 0
        self.correctCnt = 0
        self.totalInput = 0
        self.isStop = True
        self.isTimeOut = False
        self.keycnt = 0

        self.textGenerator = TextGeneratorFromFile('text.txt', 50)
        self.ta = TextArea([])
        
        pygame.display.set_caption('Typing')
        pygame.display.update()
          
    def start(self):
        self.beginTime = time.time()
        self.speed = 0
        self.correctCnt = 0
        self.totalInput = 0
        self.ta.resetWords(self.textGenerator.getText().split(' '))
        self.isStop = False
        self.isTimeOut = False
        self.keycnt = 0
    
    def stop(self):
        self.beginTime = 0
        self.speed = 0
        self.correctCnt = 0
        self.totalInput = 0
        self.ta.resetWords([])
        self.isStop = True
        self.isTimeOut = False
        self.keycnt = 0
    
    def end(self):
        self.isStop = True
        self.isTimeOut = True

    def gameloop(self):
        while True:
            for event in pygame.event.get(): #事件处理
                if event.type == pygame.QUIT:
                    pygame.quit()  # 停止运行Pygame
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()  # 停止运行Pygame
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.startBtn.isPressd(event.pos):
                        if self.isStop: 
                            self.startBtn.text = 'stop'
                            self.start()
                        else:
                            self.startBtn.text = 'start'
                            self.stop()
                    
                if not self.isStop: 
                    if event.type == pygame.KEYDOWN:
                        if len(event.unicode) > 0:
                            self.keycnt += 1
                            reset = self.ta.keydown(event.unicode)
                            if not reset:
                                correct, total = self.ta.check()
                                self.correctCnt += correct
                                self.totalInput += total
                                self.ta.resetWords(self.textGenerator.getText().split(' '))                               
                                  
            if not self.isStop:         
                self.speed = self.keycnt / (time.time() - self.beginTime + 1e-6) * 60   
                correct, total = self.ta.check()
            
                self.infoArea.setText(self.speed, self.correctCnt + correct, self.totalInput + total, time.time() - self.beginTime)
            
                if self.speed > self.maxSpeed:
                    self.speed = self.maxSpeed
                
                if (time.time() - self.beginTime >= self.totolTime):
                    self.end()
                    self.startBtn.text = 'start'
            
            self.screen.fill((255-255*self.speed/self.maxSpeed,255*self.speed/self.maxSpeed,0))
            self.startBtn.update(self.screen)
            self.infoArea.update()
            self.ta.update()
            self.elements.update()
            self.elements.draw(self.screen)
            if self.isTimeOut:
                self.timeout.update(self.screen)
            pygame.display.update()
            self.clock.tick(20)

def main():
    pygame.init()
    game = TypingGame(0)
    game.gameloop()

if __name__ == '__main__':
    main()    
