import pygame
import datetime


pygame.init()


image_library = {}
def get_image(path):
        global image_library
        image = image_library.get(path)
        if image == None:
                image = pygame.image.load(path)
                image_library[path] = image
        return image
        

display = pygame.display.set_mode((850, 850))

done = False
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = datetime.datetime.now()
    seconds = current_time.second
    minutes = current_time.minute
    display.fill((255,255,255))
    display.blit(get_image('clock.jpeg'), (0,0))
    
    rotated_min = pygame.transform.rotate(pygame.transform.rotate(get_image('min.png'), 85), -minutes*6)
    display.blit(rotated_min, rotated_min.get_rect(center = display.get_rect().center))
    
    rotated = pygame.transform.rotate(pygame.transform.rotate(get_image('sec.png'), 90), -seconds*6)
    display.blit(rotated, rotated.get_rect(center = display.get_rect().center))
    
    pygame.display.update()
    clock.tick(60)
