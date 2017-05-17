import pygame
import random
from random import shuffle
###################################end imports

pygame.init()

#############################konstante

width=1500
heigth=int(width*0.618033)

zacetna=[0,0]
koncna=[0,1]
##############################end konstante

class Cell:
	def __init__(self, s=10, v=10):
		super().__init__()  
		self.right=True
		self.down=True
		self.sirina=s
		self.visina=v
		self.obiskan=False
##########################################################################################################end cell

class Mreza(pygame.sprite.Sprite):
	
	def __init__(self,n=20,m=20):
		super().__init__()

		self.n=n
		self.m=m
		global koncna
		koncna=[random.randint(int(m/2),m-1),random.randint(int(n/2),n-1)]
		
		#Cell.sirina=width/self.n
		#Cell.visina=heigth/self.m

		self.polje=[[Cell(width/self.m, heigth/self.n) for i in range(n)]
							for j in range(m)]
#_________________________________________________________________________________________							
	def narisi_se(self):
		#Cell.sirina=width/self.n
		#Cell.visina=heigth/self.m
		
		pygame.draw.rect(okno,(155, 255,155),(zacetna[0]*width/self.m,zacetna[1]*heigth/self.n,width/self.m,heigth/self.n),0)
		pygame.draw.rect(okno,(255, 155,155),(koncna[0]*width/self.m,koncna[1]*heigth/self.n,width/self.m,heigth/self.n),0)

		for j in range(self.n):
			for i in range(self.m):
				c=self.polje[i][j]
					
				if c.right:
					#pygame.draw.line(okno,(255, 0, 0),(0,100),(100,100),5)
					pygame.draw.line(okno,(0, 0, 0),((i+1)*c.sirina,j*c.visina),((i+1)*c.sirina,(j+1)*c.visina),3)
				if c.down:
					pygame.draw.line(okno,(0, 0, 0),(i*c.sirina,(j+1)*c.visina),((i+1)*c.sirina,(j+1)*c.visina),3)
		
#_________________________________________________________________________________________	
	def dobi_sosede(self,x,y):
		sosedi=[]
		if y!=0 and  self.polje[x][y-1].obiskan==False:#1
			sosedi.append([x,y-1])
		if x!=self.m-1 and self.polje[x+1][y].obiskan==False :#2
			sosedi.append([x+1,y])	
		if y!=self.n-1 and self.polje[x][y+1].obiskan==False:#3
			sosedi.append([x,y+1])
		if x!=0 and  self.polje[x-1][y].obiskan==False:#4
			sosedi.append([x-1,y])
		return sosedi
#_________________________________________________________________________________________	
	def generiraj_labirint(self):

		pot=[zacetna]

		while len(pot)>0:
			jaz = pot[-1]
			#print(jaz)
			self.polje[jaz[0]][jaz[1]].obiskan=True
			sos= self.dobi_sosede(jaz[0],jaz[1])

			if len(sos)==0:
				pot.pop()
			else:
				shuffle(sos)
				naslednji=sos[0]
				pot.append(naslednji)
				if naslednji[1] > jaz[1]:
					self.polje[jaz[0]][jaz[1]].down = False

				elif naslednji[0] > jaz[0]:
					self.polje[jaz[0]][jaz[1]].right = False

				elif naslednji[1] < jaz[1]:
					self.polje[naslednji[0]][naslednji[1]].down = False

				elif naslednji[0] < jaz[0]:
					self.polje[naslednji[0]][naslednji[1]].right = False

#_________________________________________________________________________________________	
	def mozni_sosedje(self,x,y):
		sosedi=[]
		if y!=0 and  self.polje[x][y-1].obiskan==False and self.polje[x][y-1].down==False:#1 d
			sosedi.append([x,y-1])
		if x!=self.m-1 and self.polje[x+1][y].obiskan==False and  self.polje[x][y].right==False :#2
			sosedi.append([x+1,y])	
		if y!=self.n-1 and self.polje[x][y+1].obiskan==False and self.polje[x][y].down==False:#3
			sosedi.append([x,y+1])
		if x!=0 and  self.polje[x-1][y].obiskan==False and self.polje[x-1][y].right==False:#4 d
			sosedi.append([x-1,y])
		return sosedi

#_________________________________________________________________________________________			
	def resi_labirint(self):
		pot=[zacetna]

		for vrsta in self.polje:
			for cell in vrsta:
				cell.obiskan=False
			
		while True:
			jaz=pot[-1]
			if jaz==koncna:
				break

			
			self.polje[jaz[0]][jaz[1]].obiskan=True
			sos= self.mozni_sosedje(jaz[0],jaz[1])

			if len(sos)==0:
				pot.pop()
			else:
				shuffle(sos)
				naslednji=sos[0]
				pot.append(naslednji)
				if naslednji[1] > jaz[1]:
					self.polje[jaz[0]][jaz[1]].down = False

				elif naslednji[0] > jaz[0]:
					self.polje[jaz[0]][jaz[1]].right = False

				elif naslednji[1] < jaz[1]:
					self.polje[naslednji[0]][naslednji[1]].down = False

				elif naslednji[0] < jaz[0]:
					self.polje[naslednji[0]][naslednji[1]].right = False
		###narisi resitev
		w = self.polje[0][0].sirina
		h = self.polje[0][0].visina
		#print("REŠEN", w, h, pot)
		for i in range(len(pot)-1):
			t1=[w*pot[i][0]+w/2,h*pot[i][1]+h/2]
			t2=[w*pot[i+1][0]+w/2,h*pot[i+1][1]+h/2]
			pygame.draw.line(okno,(255, 0, 0),t1,t2,5)

		print(str(int(len(pot)/(self.n*self.m)*100)),"%")
#_________________________________________________________________________________________

##############################################################################################################end mreže

okno=pygame.display.set_mode([width+10, heigth+10])
ura=pygame.time.Clock()
mreza=Mreza(50,50)

mreza.generiraj_labirint()
game=True

while game:

	ura.tick(60)

	for dogodek in pygame.event.get():
		if dogodek.type == pygame.QUIT:
			# Ce uporabnik zapre okno nehajmo igrati
			game = False

	okno.fill((255, 255, 255))
	
	mreza.narisi_se()
	mreza.resi_labirint()
	pygame.display.flip()

pygame.quit()
