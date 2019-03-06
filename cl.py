from turtle import *
class Dots:
	def title(self):
		penup()
		goto(-127,300)
		pendown()
		write("Dot-Box",font=("Bauhaus 93",40,"italic"))
		penup()
	def box1(self):
		fillcolor("red")
		speed(1000)
		penup()
		goto(-187,188)
		length=40*9
		pendown()
		for i in range(0,4):
			forward(length)
			right(90)
	def draw(self):
		self.title()
		self.box1()
		penup()
		x=-150.0
		y=140.0
		setpos(x,y)
		hideturtle()
		self.box(x,y)
	def box(self,x,y):
		xo=x
		yo=y
		for j in range(0,8):
			for i in range(0,8):
				pendown()
				write(".",font=("Arial",20,"normal"))	
				penup()
				forward(40)
			y-=40.0	
			goto(x,y)
		goto(xo+3.0,yo+8.0)
		showturtle()
		 

