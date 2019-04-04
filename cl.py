from turtle import *
class Dots:
	def __init__(self,player,names,val):
		self.player=player
		self.names=names
		self.opt=val
	def title(self):
		penup()
		goto(-127,300)
		pendown()
		write("Dot->Box",font=("Bauhaus 93",40,"italic"))
		penup()
	def score_title(self,color,x,y,player_name):
		penup()
		goto(x,y)
		pendown()
		pencolor(color)
		name=self.names[player_name]+" "*(6-len(self.names[player_name]))
		if(self.opt==1):
			name+=":" 
		write(name,font=("Bauhaus 93",40,"italic"))
	def instruction(self):
		penup()
		goto(-650,-50)
		pendown()
		write("\tInstruction: \n1.Press Space to draw line.\n2.Use arrow keys to move \n   the pointer.",font=("Bauhaus 93",20,"italic"))
		penup()
	def score(self):
		if(self.player==2):
			self.score_title("blue",-650,300,0)
			self.score_title("red",390,300,1)
		elif(self.player==3):
			self.score_title("blue",-650,300,0)
			self.score_title("red",390,300,1)
			self.score_title("green",-650,-300,2)
			
		elif(self.player==4):
			self.score_title("blue",-650,300,0)
			self.score_title("red",390,300,1)
			self.score_title("green",-650,-300,2)
			self.score_title("yellow",400,-300,3)
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
		setup(1360,710)
		title("dot->box")
		self.title()
		self.box1()
		self.instruction()
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
		 

