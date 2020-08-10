from tkinter import *
from figure import Figure

class Point(Figure):
	"""Реализует рисование точки,наследуемое от абстрактного класса Фигура"""
	def __init__(self,canvas,x,y,color,size):
		self.canvas = canvas
		self.x = x
		self.y = y
		self.color = color
		self.size = size
		self.coordinates = []
		self.add(self.x, self.y,self.coordinates)
		self.draw(self.coordinates)

	def draw(self,l): #Отрисовать точку по координатам из списка
		n = 0
		for i in l:
			self.canvas.create_oval(l[n][0]-self.size, l[n][1]-self.size,
									l[n][0]+self.size, l[n][1]+self.size,
									outline=self.color,
									fill=self.color)
			n += 1
