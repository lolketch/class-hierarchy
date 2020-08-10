from tkinter import *
from line import Line

class Triangle(Line):
	"""Реализует рисование треугольника на основе трех линий"""
	def __init__(self,canvas,x0,y0,x1,y1,x2,y2,color,size):
		self.canvas = canvas
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = color
		self.size = size

		self.coordinates = []

		self.add(self.x0,self.y0,self.coordinates)
		self.add(self.x1,self.y1,self.coordinates)
		self.add(self.x2,self.y2,self.coordinates)

		self.draw_triangle(self.x0,self.y0,self.x1,self.y1,self.x2,self.y2)


	def draw_triangle(self,x0,y0,x1,y1,x2,y2):
		self.draw_line(x0,y0,x1,y1)
		self.draw_line(x1,y1,x2,y2)
		self.draw_line(x2,y2,x0,y0)