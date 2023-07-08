import pygame
 
run = True #el programa se ejecutara mientras sea true
width = 400 #ancho de la ventana
height = 100 #altode la ventana
pygame.init() #inicializa el entorno pygame.
screen = pygame.display.set_mode((width, height)) #prepara la ventana de la aplicación y establece su tamaño
font = pygame.font.SysFont(None, 50) # crea un objeto que represente la fuente predeterminada 
text = font.render("python 2", True, (164, 129, 240))# crea un objeto que represente un texto dado, el texto será suavizado (True) y blanco (255,255,255).
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))# inserta el texto en el búfer de pantalla (actualmente invisible)
pygame.display.flip() # invierte los búferes de la pantalla para que el texto sea visible.
while run:
  for event in pygame.event.get(): #obtiene una lista de todos los eventos pendientes de pygame.
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False
 