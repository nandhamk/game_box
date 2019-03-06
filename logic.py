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
	
	def boxing(self):
		backward(40)
		if(self.check_box()):
			a,b=pos()
			penup()
			goto(a,b)
			pendown()
			bengin_fill()
			for i in range(0,4):
				right(90)
				forward(40)
			end_fill()
				
		
	def dot(self,x,y):
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		c=self.b[o_y]
		c[o_x]=1

	def check_box(self):
		a,b=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/4)
		c=self.b[o_y]
 		if((c[o_x]==1) and (self.count<5)):
			left(90)
			backward(40)
			self.count+=1
			self.check_box()
		else:
			return True
	
logic=Logic()
dots=Dots()
dots.draw()
logic.i()
logic.listening()
done()