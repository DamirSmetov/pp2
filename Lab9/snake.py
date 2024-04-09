import pygame 
import random
import time

pygame.init()
#initializing constants
window_x = 720
window_y = 480

GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("times new roman", 25)
font2 = pygame.font.SysFont("times new roman", 50)
font3 = pygame.font.SysFont("times new roman", 25)

FOOD_TIMER = 5

food_time_start = time.time()

FPS = 60

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
#parametrs of snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
speed = 15
#parametrs of frut
fruit_position = [random.randint(1, (window_x//10))*10, random.randint(1, (window_y//10))*10]
fruit_spawn = True

direction = "DOWN"
change_to = direction

score = 0
level = 1

def score_collect():
    global score, level
    text = font.render("Score:"+str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
def game_over():
    global score
    text = font2.render("Your final score:" + str(score), True, (255, 255, 255))   
    screen.fill(RED)
    screen.blit(text, (window_x/4, window_y/2))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
                
    #restrictios for movement
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
	    direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
	    direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
	    direction = 'RIGHT'

	# Moving the snake
    if direction == 'UP':
	    snake_position[1] -= 10
    if direction == 'DOWN':
	    snake_position[1] += 10
    if direction == 'LEFT':
	    snake_position[0] -= 10
    if direction == 'RIGHT':
	    snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    #Checking if the snake has colided with fruit
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += random.randint(1, 4)
        fruit_spawn = False
        if score%3==0:
            speed += 5
            level += 1
    else:
        snake_body.pop()
    #checking if the time exceds or not
    if time.time() - food_time_start > FOOD_TIMER or not fruit_spawn:
        fruit_position = [random.randint(10, (window_x//10))*10, random.randint(10, (window_y//10))*10]
        food_time_start = time.time()
        
    fruit_spawn = True
    screen.fill(BLACK)
    
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, BLUE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    score_collect()
    text = font3.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(text,(600, 10))
    #conditions of "game_over"
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    
    pygame.display.update()
    clock.tick(speed)
        
    
    
        

        