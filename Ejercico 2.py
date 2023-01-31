import pygame

# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejercicio 2")

# Crea el objeto pelota
ball = pygame.image.load("pelota_mundial_fubol.png")
ancho = 40
alto = 40
imagen_redimensionada = pygame.transform.scale(ball, (ancho, alto))
# Obtengo el rectángulo del objeto anterior
ballrect = imagen_redimensionada.get_rect()

# Inicializo los valores con los que se van a mover la pelota
speed = [4,4]

# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    # Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Muevo la pelota
    ballrect = ballrect.move(speed)

    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((252, 243, 207))

    # Dibujo la pelota
    ventana.blit(imagen_redimensionada, ballrect)

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()