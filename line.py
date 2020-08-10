from point import Point
from tkinter import *

class Line(Point):
	"""Реализует рисование линии на основе двух точек"""
	def __init__(self,canvas,x0,y0,x1,y1,color,size):
		self.canvas = canvas
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1

		self.color = color 
		self.size = size

		self.coordinates = []
		
		self.add(self.x0,self.y0,self.coordinates)
		self.add(self.x1,self.y1,self.coordinates)
		
		self.draw_line(self.x0,self.y0,self.x1,self.y1)

	def draw_line(self,x0,y0,x1,y1):
		self.draw(self.coordinates)
		self.canvas.create_line(x0,y0,
								x1,y1,
								width=self.size*2,
								fill=self.color,
								capstyle=ROUND)
