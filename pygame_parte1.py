#importamos libreria pygame  y sys
import pygame
import sys
#ventana
pygame.init()
alto_ventana=600
ancho_ventana=600
#definimos colores en RGB
blanco=(250,250,250)
#creamos una nueva ventana
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana))
game_over = False
#importamos reloj para limitar los loops
reloj=pygame.time.Clock()
#################################
#creamos un nueva superficie
#s1=pygame.Surface((50,50))
#damos color a la superficie s1 en RGB
#s1.fill((200,20,50))
##############################
##pos
movx=ancho_ventana
movy=0
#para introducir texto
puntaje=0
vueltx=0
fuente = pygame.font.SysFont("ARIAL BLACK",30)
fuente2 = pygame.font.SysFont("consolas",16)
txt=fuente.render("HOLA MUNDO",True,blanco)

while not game_over:
	# eventos dentro de la ventana LOOOOOP PRINCIPAL
	for event in pygame.event.get():
		print(event)
		#si el evento es = QUIT termina el proceso
		if event.type == pygame.QUIT:
			sys.exit()

	#definimos el numero de frame a 20
	reloj.tick(20)
	#introduciomos la superficie creada s1 a ventana, con las cordenadas
	#ventana.blit(s1,[50,10])
	#introducimos el rectangulo con draw: (superficie,color,tamaño)
	
	ventana.fill((0,0,0))
	txt_punto = fuente2.render("PUNTOS : "+ str(puntaje),True,blanco)
	txt_vuelta = fuente2.render("VUELTA : "+ str(vueltx),True,blanco)
	ventana.blit(txt_vuelta,(490,0))
	ventana.blit(txt_punto,(6,0))
	ventana.blit(txt,(200,0))
	pygame.draw.rect(ventana,blanco,(movx,movy,20,20))
	#movimiento de rectangulo
	movx -= 10
	movy += 10
	if movx <= 0:
		movx=ancho_ventana+19
		puntaje+=10
	if movy>alto_ventana:
		movy=-19
		vueltx+=1
	
	#actualizacion de la ventana
	pygame.display.update()
	pygame.time.delay(10)
