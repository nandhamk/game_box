from turtle import *
from cl import Dots
class Logic:
	b=[]
	z=0
	count=0
	point=[]
	box_blue=0
	box_red=0
	box_green=0
	box_yellow=0
	color=("blue",'red',"green","yellow")
	co=0
	player=0
	names=[]
	boxes=[]
	c=0
	box_count=0
	def __init__(self,p,name,count):
		self.player=p
		self.names=name
		self.box_count=count
	def i(self):
		for i in range(0,8):
			c=[]
			for j in range(0,8):
				d=[]
				c.append(d)
			self.b.append(c)
		for i in range(0,7):
			a=[0]*7
			self.boxes.append(a)

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
			self.position()
			self.dot()
			self.z=0
			self.fill_box_up()
			self.color_change()
		penup()


	def down(self):
		setheading(270)
		x,y=pos()
		self.wall1(x,y-40)
		if(self.z==1):
			self.position()
			self.dot()
			self.z=0
			self.fill_box_down()
			self.color_change()	
		penup()

	def left(self):
		setheading(180)
		x,y=pos()
		self.wall1(x-40,y)
		if(self.z==1):
			self.position()
			self.dot()
			self.z=0
			self.fill_box_left()
			self.color_change()		
		penup()

	def right(self):
		setheading(0)	    
		x,y=pos()
		self.wall1(x+40,y)
		if(self.z==1):
			self.position()
			self.dot()
			self.z=0
			self.fill_box_right()
			self.color_change()
		penup()

	def enter(self):
		a,b=pos()
		self.point=[a,b]
		self.z=1
		print(self.b)
		pendown()

	def z_zero(self):
		if(self.z):
			self.z=0

	def wall1(self,a,b):
		if(a<(-147)):
			self.z_zero()
			a=133
			penup()
		if(a>133):
			self.z_zero()
			a=-147
			penup()
		if(b>148):
			self.z_zero()
			b=-132
			penup()
		if(b<(-132)):
			self.z_zero()
			b=148
			penup()
		goto(a,b)

	def fill_box_up(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		double_box=0
		self.c=0
		if((o_y,o_x-1) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y][o_x-1]):
			if((o_y+1,o_x-1) in self.b[o_y][o_x-1] or (o_y,o_x-1) in self.b[o_y+1][o_x-1]):
				if((o_y+1,o_x) in self.b[o_y+1][o_x-1] or (o_y+1,o_x-1) in self.b[o_y+1][o_x]):
					if((o_y,o_x) in self.b[o_y+1][o_x]):
						#self.draw_box(270)
						#double_box+=1
						x=min(o_y,o_y+1)
						y=min(o_x,o_x-1)
						if(not self.boxes[y][x]):
							self.draw_box(270)
							double_box+=1
							self.boxes[y][x]=1
							print(self.boxes)
							self.box_count+=1

		#error
		try:
			if((o_y,o_x+1) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y][o_x+1]):
				if((o_y+1,o_x+1) in self.b[o_y][o_x+1] or (o_y,o_x+1) in self.b[o_y+1][o_x+1]):
					if((o_y+1,o_x) in self.b[o_y+1][o_x+1] or (o_y+1,o_x+1) in self.b[o_y+1][o_x]):
						if((o_y,o_x) in self.b[o_y+1][o_x]):
							#self.draw_box(0)
							#double_box+=1
							x=min(o_y,o_y+1)
							y=min(o_x,o_x+1)
							if(not self.boxes[y][x]):
								self.draw_box(0)
								double_box+=1
								self.boxes[y][x]=1
								print(self.boxes)
								self.box_count+=1
							
		except IndexError:
			print("small error up")
			pass

		if(double_box==2):
			self.co+=1

	def fill_box_down(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		double_box=0

		if((o_y,o_x-1) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y][o_x-1]):
			if((o_y-1,o_x-1)in self.b[o_y][o_x-1] or (o_y,o_x-1) in self.b[o_y-1][o_x-1]):
				if((o_y-1,o_x) in self.b[o_y-1][o_x-1] or (o_y-1,o_x-1) in self.b[o_y-1][o_x]):
					if((o_y,o_x) in self.b[o_y-1][o_x]):
						#self.draw_box(180)
						#double_box+=1
						x=min(o_y,o_y-1)
						y=min(o_x,o_x-1)
						if(not self.boxes[y][x]):
							self.boxes[y][x]=1
							self.draw_box(180)
							double_box+=1
							print("dowm sucess2")
							print(self.boxes)
							self.box_count+=1
		#error
		try:
			if((o_y,o_x+1) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y][o_x+1]):
				if((o_y-1,o_x+1) in self.b[o_y][o_x+1] or (o_y,o_x+1) in self.b[o_y-1][o_x+1]):
					if((o_y-1,o_x) in self.b[o_y-1][o_x+1] or (o_y-1,o_x+1) in self.b[o_y-1][o_x]):
						if((o_y,o_x) in self.b[o_y-1][o_x]):
							#self.draw_box(90)
							#double_box+=1
							x=min(o_y,o_y-1)
							y=min(o_x,o_x+1)
							if(not self.boxes[y][x]):
								self.draw_box(90)
								double_box+=1
								self.boxes[y][x]=1
								print("down sucess1")
								print(self.boxes)
								self.box_count+=1
		except IndexError:
			print("small error down")
			pass
		if(double_box==2):
			self.co+=1

	def fill_box_left(self):
		x,y=pos()
		print('left')
		print('y,x',y,x)
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		print('o_y,o_x',o_y,o_x)
		double_box=0
		try:
			if((o_y+1,o_x) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y+1][o_x]):
				if((o_y+1,o_x+1) in self.b[o_y+1][o_x] or (o_y+1,o_x) in self.b[o_y+1][o_x+1]):
					if((o_y,o_x+1) in self.b[o_y+1][o_x+1] or (o_y+1,o_x+1) in self.b[o_y][o_x+1]):
						if((o_y,o_x) in self.b[o_y][o_x+1]):
							#double_box+=1
							#self.draw_box(0)
							x=min(o_y,o_y+1)
							y=min(o_x,o_x+1)
							if(not self.boxes[y][x]):
								self.boxes[y][x]=1
								self.draw_box(0)
								double_box+=1
								print("left sucess1")
								print(self.boxes)
								self.box_count+=1
		except IndexError:
			print("small error left")
			pass

				
		if((o_y-1,o_x) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y-1][o_x]):
			if((o_y-1,o_x+1) in self.b[o_y-1][o_x] or (o_y-1,o_x) in self.b[o_y-1][o_x+1]):
				if((o_y,o_x+1) in self.b[o_y-1][o_x+1] or (o_y-1,o_x+1) in self.b[o_y][o_x+1]):
					if((o_y,o_x) in self.b[o_y][o_x+1]):
						#self.draw_box(90)
						#double_box+=1
						x=min(o_y,o_y-1)
						y=min(o_x,o_x+1)
						if(not self.boxes[y][x]):
							self.boxes[y][x]=1
							self.draw_box(90)
							double_box+=1						
							print("left sucess 2")
							print(self.boxes)
							self.box_count+=1

		if(double_box==2):
			self.co+=1

	def fill_box_right(self):
		x,y=pos()
		print('right')
		print('y,x',y,x)
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		print('o_y,o_x',o_y,o_x)
		double_box=0		
		#top right
		try:
			if((o_y+1,o_x) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y+1][o_x]):
				if((o_y+1,o_x-1) in self.b[o_y+1][o_x] or (o_y+1,o_x) in self.b[o_y+1][o_x-1]):
					if((o_y,o_x-1) in self.b[o_y+1][o_x-1] or (o_y+1,o_x-1) in self.b[o_y][o_x-1]):
						if((o_y,o_x) in self.b[o_y][o_x-1]):
							#double_box+=1
							#self.draw_box(270)
							x=min(o_y,o_y+1)
							y=min(o_x,o_x-1)
							if(not self.boxes[y][x]):
								self.boxes[y][x]=1
								self.draw_box(270)
								double_box+=1
								print(self.boxes)
								self.box_count+=1
		except IndexError:
			print("small error right")
			pass

		#down right
		if((o_y-1,o_x) in self.b[o_y][o_x] or (o_y,o_x) in self.b[o_y-1][o_x]):
			if((o_y-1,o_x-1) in self.b[o_y-1][o_x] or (o_y-1,o_x) in self.b[o_y-1][o_x-1]):
				if((o_y,o_x-1) in self.b[o_y-1][o_x-1] or (o_y-1,o_x-1) in self.b[o_y][o_x-1]):
					if((o_y,o_x) in self.b[o_y][o_x-1]):
						#self.draw_box(180)
						#double_box+=1
						x=min(o_y,o_y-1)
						y=min(o_x,o_x-1)
						if(not self.boxes[y][x]):
							self.draw_box(180)
							double_box+=1
							self.boxes[y][x]=1
							print(self.boxes)
							self.box_count+=1

		if(double_box==2):
			self.co+=1
		



	def draw_box(self,dir):
		setheading(dir)					
		begin_fill()
		for i in range(0,4):
			forward(40)
			right(90)
		end_fill()
		c=color()
		print("box-count",self.box_count)
		if(c[1]=="blue"):
			self.box_blue+=1
		elif(c[1]=="red"):
			self.box_red+=1
		elif(c[1]=="green"):
			self.box_green+=1
		elif(c[1]=="yellow"):
			self.box_yellow+=1
		if(self.box_count==49):
			self.game_over()
		else:
			self.score()
	def game_over(self):
		winner=''
		if(self.box_blue > max(self.box_red,self.box_yellow,self.box_green)):
			winner=self.names[0]
		elif(self.box_red > max(self.box_blue,self.box_yellow,self.box_green)):
			winner=self.names[1]
		elif(self.box_green > max(self.box_red,self.box_blue,self.box_yellow)):
			winner=self.names[2]
		elif(self.box_yellow > max(self.box_red,self.box_blue,self.box_green)):
			winner=self.names[3]
		gameover="The winner is "+winner
		penup()
		goto(-148,0)
		pendown()
		write(gameover,font=("Bauhaus 93",40,"italic"))
		hideturtle()
		penup()

	def score(self):
		x,y=pos()
		penup()
		hideturtle()
		cor=color()
		if(cor[1]=="blue"):
			goto(-450,300)
			box=self.box_blue
		elif(cor[1]=="red"):
			goto(610,300)
			box=self.box_red
		elif(cor[1]=="green"):
			goto(-450,-300)
			box=self.box_green
		elif(cor[1]=="yellow"):
			goto(610,-300)
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
	def position(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		print(o_x,o_y)
	def dot(self):
		x,y=pos()
		o_x=int(abs(-147-x)/40)
		o_y=int((148-y)/40)
		#print('o_y,o_x',o_y,o_x)
		a,b=self.point
		a=int(abs(-147-a)/40)
		b=int((148-b)/40)
		#print('b,a',b,a)
		p=(o_y,o_x)
		if(p not in self.b[b][a]):
			self.b[b][a].append(p)
		else:
			self.co-=1
		

	def color_change(self):
		self.co+=1
		length=self.player
		value=self.co%length
		fillcolor(self.color[value])
player=0
names=['','','','']
i=0
mode=[1,2]
select=0
while(player<2 or player>=5):
	player=int(input("enter the no of players(2 to 4) : "))
while(i<player):
	print("Enter the name of the player "+str(i+1)+" : ")
	name=input()
	if(len(name)<=6):
		names[i]=name
		i+=1
	else:
		print("Renter the name with only 5 letters")
print("\t\tmode\n\t1.Classic\n\t2.Arcade ")
while(select not in mode):
	select=int(input("enter the mode no:"))
val=0
if(select==1):			
	val=1
else:
	val=49
logic=Logic(player,names,val)
dots=Dots(player,names,val)
dots.draw()
logic.i()
logic.listening()
del logic
done()
