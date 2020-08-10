
class Figure(object):
	def __init__(self,canvas):
		self.canvas = canvas

	def add(self,x,y,l): #Добавить координаты точки в список
		x_y = [x,y]
		l.append(x_y)

	def delete(self):
		pass
	def motion(self):
		pass
	def rotate(self):
		pass