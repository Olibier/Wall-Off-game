import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

rectList = []

def drawRar():
    for i in range(10):
        rect_y = 50 * i
        for j in range(10):
            rect_x = 50 * j + 250
            rect = pygame.Rect(rect_x, rect_y, 50, 50)
            rectList.append(rect)
drawRar()

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    for rect in rectList:
        pygame.draw.rect(screen, (180, 180, 180), rect, 1)

    
    pygame.display.flip()
    clock.tick()
