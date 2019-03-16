from turtle import *
from cl import Dots
class Logic:
	b=[]
	z=0
	count=0
	h_line=[]
	v_line=[]
	box_blue=0
	box_red=0
	box_green=0
	box_yellow=0
	color=["blue",'red',"green","yellow"]
	co=0
	def i(self):
		for i in range(0,8):
			a=[0]*8
			self.b.append(a)
			c=[0]*8
			self.h_line.append(c)
		for i in range(0,8):
			c=[0]*8
			self.v_line.append(c)

	def listening(self):
		listen()
		onkey(self.up, 'Up')
		onkey(self.down, 'Down')
		onkey(self.left, 'Left')
		onkey(self.right, 'Right')
		onkey(self.enter,'space')
	def up(self):
		setheading(90)
		x,y=pos()
		self.wall1(x,y+40)
		if(self.z==1):
			self.dot_v_line(x,y,y+40)
			self.z=0
			self.fill_box_up()
			self.color_change()
		penup()


	def down(self):
		setheading(270)
		x,y=pos()
		self.wall1(x,y-40)
		if(self.z==1):
			self.dot_v_line(x,y,y-40)
			self.z=0
			self.fill_box_down()
			self.color_change()	
		penup()

	def left(self):
		setheading(180)
		x,y=pos()
		self.wall1(x-40,y)
		if(self.z==1):
			self.dot_h_line(x,x-40,y)
			self.z=0
			self.fill_box_left()
			self.color_change()		
		penup()

	def right(self):
		setheading(0)	    
		x,y=pos()
		self.wall1(x+40,y)
		if(self.z==1):
			self.dot_h_line(x,x+40,y)
			self.z=0
			self.fill_box_right()
			self.color_change()
		penup()

	def enter(self):
		a,b=pos()
		self.dot(a,b)
		print(self.b)
		self.z=1	    
		pendown()

	def wall1(self,a,b):
		if(a<(-147)):
			a=133
			penup()
		if(a>133):
			a=-147
			penup()
		if(b>148):
			b=-132
			penup()
		if(b<(-132)):
			b=148
			penup()
		goto(a,b)

	def fill_box_up(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		if(self.h_line[o_y][o_x]):
			if(self.v_line[o_y][o_x+1]):
				if(self.h_line[o_y+1][o_x]):
					if(self.v_line[o_y][o_x]):
						self.draw_box(0)

		if(self.h_line[o_y][o_x-1]):
			if(self.v_line[o_y][o_x-1]):
				if(self.h_line[o_y+1][o_x-1]):
					if(self.v_line[o_y][o_x]):
						self.draw_box(270)

	def fill_box_down(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		if(self.h_line[o_y][o_x]):
			print(o_y,o_x)
			if(self.v_line[o_y-1][o_x+1]):
				print(o_y-1,o_x+1)
				if(self.h_line[o_y-1][o_x]):
					print(o_y-1,o_x)
					if(self.v_line[o_y-1][o_x]):
						print(o_y-1,o_x)
						self.draw_box(90)
						print("down sucess1")

		if(self.h_line[o_y][o_x-1]):
			print(o_y,o_x-1)
			if(self.v_line[o_y-1][o_x-1]):
				print(o_y-1,o_x-1)
				if(self.h_line[o_y-1][o_x-1]):
					print(o_y-1,o_x-1)
					if(self.v_line[o_y-1][o_x]):
						print(o_y-1,o_x)
						self.draw_box(180)
						print("dowm sucess2")

	def fill_box_left(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		if(self.v_line[o_y][o_x]):
			print(o_y,o_x)
			if(self.h_line[o_y+1][o_x]):
				print(o_y+1,o_x)
				if(self.v_line[o_y][o_x+1]):
					print(o_y,o_x+1)
					if(self.h_line[o_y][o_x]):
						print(o_y,o_x)
						self.draw_box(0)
						print("left sucess1")

		if(self.v_line[o_y-1][o_x]):
			print(o_y-1,o_x)
			if(self.h_line[o_y-1][o_x]):
				print(o_y-1,o_x)
				if(self.v_line[o_y-1][o_x+1]):
					print(o_y-1,o_x+1)
					if(self.h_line[o_y][o_x]):
						print(o_y,o_x)
						self.draw_box(90)
						print("left sucess 2")

	def fill_box_right(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		#top right
		if(self.v_line[o_y][o_x]==1):
			print(o_y,o_x)
			if(self.h_line[o_y+1][o_x-1]==1):
				print(o_y+1,o_x-1)
				if(self.v_line[o_y][o_x-1]==1):
					print(o_y,o_x-1)
					if(self.h_line[o_y][o_x-1]==1):
						print(o_y,o_x-1)
						self.draw_box(270)
		#down right
		if(self.v_line[o_y-1][o_x]==1):
			print(o_y-1,o_x)
			if(self.h_line[o_y-1][o_x-1]==1):
				print(o_y-1,o_x-1)
				if(self.v_line[o_y-1][o_x-1]==1):
					print(o_y-1,o_x-1)
					if(self.h_line[o_y][o_x-1]==1):
						print(o_y,o_x-1)
						self.draw_box(180)
		

	def draw_box(self,dir):
		setheading(dir)					
		begin_fill()
		for i in range(0,4):
			forward(40)
			right(90)
		end_fill()
		c=color()
		if(c[1]=="blue"):
			self.box_blue+=1
		elif(c[1]=="red"):
			self.box_red+=1
		elif(c[1]=="green"):
			self.box_green+=1
		elif(c[1]=="yellow"):
			self.box_yellow+=1
		self.score()

	def score(self):
		x,y=pos()
		penup()
		hideturtle()
		cor=color()
		if(cor[1]=="blue"):
			goto(-450,300)
			box=self.box_blue
		elif(cor[1]=="red"):
			goto(600,300)
			box=self.box_red
		elif(cor[1]=="green"):
			goto(-450,-300)
			box=self.box_green
		elif(cor[1]=="yellow"):
			goto(600,-300)
			box=self.box_yellow
		pendown()
		pencolor("white")
		fillcolor("white")
		begin_fill()
		setheading(0)
		for i in range(0,4):
			forward(70)
			left(90)
		end_fill()
		pencolor("black")
		write(box,font=("Bauhaus 93",40,"italic"))
		penup()
		fillcolor(cor[1])
		goto(x,y)
		showturtle()
		self.co-=1	
		
	def dot(self,x,y):
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		c=self.b[o_y]
		c[o_x]=1
		print(o_y,o_x)
	def dot_h_line(self,x1,x2,y):
		o_x1=int(abs(-147-x1)/40)
		o_x2=int(abs(-147-x2)/40)
		o_y=int((148-y)/40)
		o_x=min(o_x1,o_x2)
		print(o_y,o_x1,o_x2)
		self.h_line[o_y][o_x]=1
		print("h_line :",self.h_line)

	def dot_v_line(self,x,y1,y2):
		o_x=int(abs(-147-x)/40)
		o_y1=int((148-y1)/40)
		o_y2=int((148-y2)/40)
		o_y=min(o_y1,o_y2)
		print(o_y1,o_y2,o_x)
		self.v_line[o_y][o_x]=1
		print("v_line : ",self.v_line)

	def color_change(self):
		self.co+=1
		length=len(self.color)
		value=self.co%length
		fillcolor(self.color[value])
	
logic=Logic()
dots=Dots()
dots.draw()
logic.i()
logic.listening()
done()