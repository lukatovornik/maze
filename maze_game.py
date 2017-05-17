import pygame
import random
from random import shuffle
###################################end imports

pygame.init()

#############################konstante

width=1500
heigth=int(width*0.618033)

zacetna=[0,0]
koncna=[20,10]
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
	
	def __init__(self,n=100,m=50):
		super().__init__()

		self.n=n
		self.m=m
		#Cell.sirina=width/self.n
		#Cell.visina=heigth/self.m

		self.polje=[[Cell(width/self.n, heigth/self.m) for i in range(n)]
							for j in range(m)]
#_________________________________________________________________________________________							
	def narisi_se(self):
		#Cell.sirina=width/self.n
		#Cell.visina=heigth/self.m

		pygame.draw.rect(okno,(155, 255,155),(zacetna[0]*width/self.n,zacetna[1]*heigth/self.m,width/self.n,heigth/self.m),0)
		pygame.draw.rect(okno,(255, 155,155),(koncna[0]*width/self.n,koncna[1]*heigth/self.m,width/self.n,heigth/self.m),0)

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
		if y!=0 and  self.polje[x][y-1].obiskan==False:
			sosedi.append([x,y-1])
		if x!=self.n-1 and self.polje[x+1][y].obiskan==False :
			sosedi.append([x+1,y])	
		if y!=self.m-1 and self.polje[x][y+1].obiskan==False:
			sosedi.append([x,y+1])
		if x!=0 and  self.polje[x-1][y].obiskan==False:
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
	def reši_labirint(self):
		pot=[zacetna]

		while trenutna==koncna:
			pass
#_________________________________________________________________________________________

##############################################################################################################end mreže

okno=pygame.display.set_mode([width, heigth])
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
	pygame.display.flip()

pygame.quit()
