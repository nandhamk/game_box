from turtle import *
class Dots:
	def __init__(self,player):
		self.player=player
	def title(self):
		penup()
		goto(-127,300)
		pendown()
		write("Dot-Box",font=("Bauhaus 93",40,"italic"))
		penup()
	def score(self):
		if(self.player==2):
			penup()
			goto(-650,300)
			pendown()
			pencolor("blue")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			print(pos())
			penup()
			goto(400,300)
			pendown()
			pencolor("red")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
		elif(self.player==3):
			penup()
			goto(-650,300)
			pendown()
			pencolor("blue")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			print(pos())
			penup()
			goto(400,300)
			pendown()
			pencolor("red")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
			goto(-650,-300)
			pendown()
			pencolor("green")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
		elif(self.player==4):
			penup()
			goto(-650,300)
			pendown()
			pencolor("blue")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			print(pos())
			penup()
			goto(400,300)
			pendown()
			pencolor("red")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
			goto(-650,-300)
			pendown()
			pencolor("green")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
			goto(400,-300)
			pendown()
			pencolor("yellow")
			write("Score : ",font=("Bauhaus 93",40,"italic"))
			penup()
		pencolor("black")
		
	def box1(self):
		fillcolor("blue")
		speed(1000)
		penup()
		goto(-187,188)
		length=40*9
		pendown()
		for i in range(0,4):
			forward(length)
			right(90)
	def draw(self):
		title("dot-box")
		self.title()
		self.box1()
		self.score()
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
		 

