import pygame

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((600, 600))

done = False

x = 25
y = 25


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            if x <575:
                x += 20
        if keys[pygame.K_LEFT]:
            if x > 25:
                x -= 20
        if keys[pygame.K_UP]:
            if y > 25:
                y -= 20
        if keys[pygame.K_DOWN]:
            if y < 575:
                y += 20
    display.fill((255, 255, 255))
    pygame.draw.circle(display, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
            
            
            