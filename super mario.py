#-------------------------------------------------------------------------------
# Name:        supermario
# Author:      senfl
# Created:     01-09-2020
# Copyright:   (c) senfl 2020
#-------------------------------------------------------------------------------
from graphics import *
from winsound import PlaySound
from time import sleep


class Button:

    def __init__(self,win,center,width,height,label):
        """ creates a rectangular button, eg:
            qb = Button(myWin,centerPoint,width,height,'Quit')"""
        w,h = width/2.0, height/2.0
        x,y = center.getX(),center.getY()
        self.xmax, self.xmin, = x + w, x - w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('grey')
        self.rect.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self,p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def remove(self):
        "Attempts to remove the button"
        self.rect.undraw()
        self.label.undraw()

class super():

    def __init__(self):
        #window maker
        winde = GraphWin("Graphics window",600,600)
        self.click(winde)

    def click(self,winde):#window,center,width,height,label
    #before they click one of two buttons on the screen.
        mid = Button(winde,Point(300,300),100,100,'click my boy here')
        exitb = Button(winde,Point(500,500),50,50,'Exit')
        exitb.activate()
        mid.activate()

        bclick = False
        while bclick is False:
            clik = winde.getMouse()
            if mid.clicked(clik) == True:
                mid.deactivate()
                sleep(.25)
                mid.remove()
                exitb.remove()
                bclick = True
                self.postclick(winde)
            elif exitb.clicked(clik) == True:
                exitb.deactivate()
                sleep(.25)
                exitb.remove()
                mid.remove()
                bclick = True
                winde.close()

    def postclick(self,winde):
    #after they click the button, bruh
        stop = Button(winde,Point(300,300),80,80,'Stop!')
        exitb = Button(winde,Point(500,500),50,50,'Exit')
        stop.activate()
        exitb.activate()
        joe = 1
        bop = 'bopped.wav'
        while joe == 1:
            p = winde.checkMouse()
            if p!= None:
                xval = p.getX()
                yval = p.getY()
                #this is for stop button
                if xval >=260 and xval <=340:
                    if yval >=260 and yval <=340:
                        stop.deactivate()
                        sleep(.2)
                        joe=2
                        self.click(winde)
                #this is for exit button
                elif xval >=475 and xval <=525:
                    if yval >=475 and yval <=525:
                        exitb.deactivate()
                        sleep(.2)
                        joe =2
                        winde.close()
                elif p == None:
                    PlaySound(bop,1)
                    sleep(.25)
                    joe = 1

super()