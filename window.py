from tkinter import *
from point import Point
from line import Line
from triangle import Triangle

class Window():
	def __init__(self):
		#self.point = Point()
		self.width = 1200
		self.height = 700
		self.bg_color = "white"
		self.screen_resolution = str(self.width)+'x'+str(self.height) + "+300+300"

		#Создание окна
		self.root = Tk()
		self.root.geometry(self.screen_resolution)
		self.root.resizable(width=False, height=False)
		self.root.title("Paint")

		self.tool_bar = Frame(self.root,bg="#e0e0e0")
		
		self.btn_point1 = Button(self.tool_bar,text="POINT-1")
		self.btn_point1.grid(row=0,column=0,padx=4,pady=4)

		self.btn_point2 = Button(self.tool_bar,text="POINT-2")
		self.btn_point2.grid(row=1,column=0,padx=4,pady=4)

		self.btn_line1 = Button(self.tool_bar,text="LINE-1")
		self.btn_line1.grid(row=2,column=0,padx=4,pady=4)

		self.btn_triangle = Button(self.tool_bar,text="TRIANGLE")
		self.btn_triangle.grid(row=3,column=0,padx=4,pady=4)

		self.tool_bar.pack(side=RIGHT,fill=Y)

		#Создание Канвы 
		self.canvas = Canvas(self.root,width=self.width,height=self.height,bg=self.bg_color)
		self.canvas.pack(side=BOTTOM)

		self.btn_point1.bind("<Button-1>", func=lambda event: self.point1())
		self.btn_point2.bind("<Button-1>", func=lambda event: self.point2())
		self.btn_line1.bind("<Button-1>", func=lambda event: self.line1())
		self.btn_triangle.bind("<Button-1>", func=lambda event: self.triangle())

		self.root.mainloop()

	def point1(self):
		point_1 = Point(self.canvas,300,600,"blue",10)

	def point2(self):
		point_2 = Point(self.canvas,200,200,"red",20)

	def line1(self):
		line_1 = Line(self.canvas,500,400,300,300,"yellow",10)

	def triangle(self):
		triangle_1 = Triangle(self.canvas,600,200,100,300,900,650,"black",5)


mainclass = Window()