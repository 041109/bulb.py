import pygame
import time
pygame.init()

HEIGHT = 800
WIDTH = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
img = pygame.image.load("BulbSimulator/Bulboff.jpg")
img3 = pygame.transform.scale(img, (250,250))
pygame.display.update()
 
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        img1 = pygame.image.load("BulbSimulator/Bulbon.jpg")
        img2 = pygame.transform.scale(img1, (300,300))
        screen.blit(img2,(250,250))
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        img = pygame.image.load("BulbSimulator/Bulboff.jpg")
        img3 = pygame.transform.scale(img, (300,300))
        screen.blit(img3,(250,250))
        pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

