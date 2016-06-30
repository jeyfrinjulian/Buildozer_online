# simple control snake how kivy keyboard
# copyright Jsystems Technology

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock
from functools import partial
from kivy.core.window import Window
from kivy.app import App

from random import randrange

class Comida(Widget):
    def __init__(self, **k):
        super(Comida, self).__init__(**k)
        self.pos_comida=[10,10]
        self.draw()
    def draw(self):
        with self.canvas:
            Ellipse(size=(10,10), pos=self.pos_comida)

class Snake_kivy(Widget):   
    def __init__(self, **k):
        super(Snake_kivy, self).__init__(**k)
        self.x, self.y=10,200
        self.Snake=[(self.x+15,self.y) for i in range(5)]
        self.direcion=""
        self.start()
    def eventosKey(self,teclado,code,text,modf):     
        if text=="d":
            self.direcion=text
        if text=="w":
            self.direcion=text
        if text=="a":
            self.direcion=text
        if text=="s":
            self.direcion=text
        print self.x
    def animacion(self,*args):
        if self.direcion=="d":
            if self.x>=Window.width:
                self.x=0
            self.x+=15
            self.Snake.insert(0,(self.x,self.y))
            self.Snake.pop()
        if self.direcion=="w":
            if self.y>=Window.height:
                self.y=0
            self.y+=15
            self.Snake.insert(0,(self.x,self.y))
            self.Snake.pop()
        if self.direcion=="a":
            if self.x<0:
                self.x=Window.width
            self.x-=15
            self.Snake.insert(0,(self.x,self.y))
            self.Snake.pop()
        if self.direcion=="s":
            if self.y<0:
                self.y=Window.height
            self.y-=15
            self.Snake.insert(0,(self.x,self.y))
            self.Snake.pop()

    def draw(self, dt):
        self.canvas.clear()
        self.add_widget(Comida())
        for i in range(len(self.Snake)):
            with self.canvas:
                Rectangle(size=(10,10), pos=self.Snake[i])
    def start(self):
        teclado=Window.request_keyboard(self.eventosKey,self)
        teclado.bind(on_key_down=self.eventosKey)
        Clock.schedule_interval(self.animacion,0)
        Clock.schedule_interval(self.draw, 0)

class test(App):
    def build(self):
        self.w=Widget()              
        return Snake_kivy()

test().run()
