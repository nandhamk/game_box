from turtle import *
from cl import Dots
class Logic:
	b=[]
	z=0
	count=0
	def i(self): 
		for i in range(0,8):
			a=[0]*8
			self.b.append(a)
							

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
		penup()


	def down(self):
		setheading(270)
		x,y=pos()
		self.wall1(x,y-40)	
		penup()

	def left(self):
		setheading(180)
		x,y=pos()
		self.wall1(x-40,y)		
		penup()

	def right(self):
		setheading(0)	    
		x,y=pos()
		self.wall1(x+40,y)
		penup()

	def enter(self):
		a,b=pos()
		self.dot(a,b)
		print(self.b)	    
		pendown()
		self.fill_box()

	def wall1(self,a,b):
		check=0
		if(a<(-147)):
			a=133
			check=1
			penup()
		if(a>133):
			check=2
			a=-147
			penup()
		if(b>148):
			b=-132
			check=3
			penup()
		if(b<(-132)):
			b=148
			check=4
			penup()
		goto(a,b)
		if(check==1):
			a=-147
			self.zero(a,b)
		elif(check==2):
			a=133
			self.zero(a,b)
		elif(check==3):
			b=148
			self.zero(a,b)
		elif(check==4):
			b=-132
			self.zero(a,b)
	def fill_box(self):
		draw=0
		a,b=pos()
		if(self.check_one(a,b)):
			backward(40)
			left(90)
			a,b=pos()
			if(self.check_one(a,b)):
				backward(40)
				left(90)
				a,b=pos()
				if(self.check_one(a,b)):
					backward(40)
					left(90)
					a,b=pos()
					if(self.check_one(a,b)):
						backward(40)
						left(90)
						draw=1
		if(draw==1):
			begin_fill()
			for i in range(0,4):
				backward(40)
				left(90)
			end_fill()
		

	def check_one(self,x,y):
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		c=self.b[o_y]
		if(c[o_x]==1):
			return True
		else:
			return False	
	def zero(self,x,y):
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		print(o_x,o_y)
		c=self.b[o_y]
		c[o_x]=0		
		
	def dot(self,x,y):
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		c=self.b[o_y]
		c[o_x]=1

	
logic=Logic()
dots=Dots()
dots.draw()
logic.i()
logic.listening()
done()