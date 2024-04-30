import pygame 
import random
import time
import psycopg2
conn = psycopg2.connect(host = "localhost", dbname = "postgres", user="postgres", password = "damir2005d", port = "5432")
conn.autocommit = True
cur = conn.cursor()
#Create table

#cur.execute("""CREATE TABLE IF NOT EXISTS Users_Snake(
    #id serial PRIMARY KEY,
    #Nickname VARCHAR(255),
    #Score INT,
    #Level INT
#);
#""")


#insert data



#cur.execute("""INSERT INTO Users_Snake (Nickname, Score, Level) VALUES
#('Jake', 7, 2),
#('Kate', 3, 1)
#""")

pygame.init()
#initializing constants
window_x = 720
window_y = 480

GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = pygame.Color('dodgerblue2')
font = pygame.font.SysFont("times new roman", 25)
font2 = pygame.font.SysFont("times new roman", 50)
font3 = pygame.font.SysFont("times new roman", 25)
font4 = pygame.font.SysFont("times new roman", 50)
font5 = pygame.font.SysFont("times new roman", 10)
color_active  = False
border_x = window_x
border_y = window_y



FOOD_TIMER = 5

level_increase = 3

food_time_start = time.time()

FPS = 60

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
#parametrs of snake
snake_position = [300, 200]
snake_body = [[300, 200], [310, 200], [320, 200]]
speed = 15
#parametrs of fruit
fruit_position = [350, 230]
fruit_spawn = True
spawn = True
fruit_position1 = []

direction = "DOWN"
change_to = direction

score = 0
level = 1
speed = 15

def show_results(score):
    global level
    level = match[3]
    text = font2.render("Your level: " + str(level), True, WHITE)   
    screen.fill(BLACK)
    screen.blit(text, (220, 120))
    pygame.display.update()
    time.sleep(3)
    
    

def score_collect():
    global score, level
    text = font.render("Score:"+str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
def game_over():
    global score
    cur.execute(f"UPDATE Users_Snake SET Score = '{score}', Level = '{level}' WHERE nickname = '{input_text}' ")
    text = font2.render("Your final score:" + str(score), True, (255, 255, 255))   
    screen.fill(RED)
    screen.blit(text, (160, 100))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    
done = True
show = True
input_text = ""
need_input = False
match = ()
#menu
while show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if event.button == 1:
                if position[0] <= 400 and position[
            0] > 300 and position[1] < 230 and position[1] > 200:
                    need_input = not need_input 
                    color_active = not color_active
                    print(need_input)  
                else:
                    need_input = False
                    color_active = False
        #logic of typing the text and checking the existense of user nickname
        if need_input and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(input_text) <= 10:
                cur.execute(f"SELECT * FROM Users_Snake WHERE nickname = '{input_text}';")
                match = cur.fetchone()
                if match == None:
                    cur.execute(f"INSERT INTO Users_Snake(nickname, score, level) VALUES ('{input_text}', 0, 1);")
                else:
                    score = match[2]
                    show_results(score)
                    level_increase = score + 3
                    speed = 15 + (level - 1)*5
                    border_x = border_x - (level-1)*10
                    border_y = border_y - (level-1)*10
                print(match)
                done = False
                show = not True
                print(show)
                break
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
            
                
    keys = pygame.key.get_pressed()
    

    screen.fill(BLACK)
    text4 = font4.render("Enter username", True, WHITE)
    pygame.draw.rect(screen, WHITE, pygame.Rect(300, 200, 100, 30))
    #Draw input box
    if color_active:
        pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(300, 200, 100, 30), 2)
    screen.blit(text4, (200, 100))
    text5 = font5.render(input_text, True, BLACK)
    screen.blit(text5, (310, 210))
    pygame.display.update()
    
    

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
        score += 1
        fruit_spawn = False
        if score >= level_increase:
            speed += 5
            level += 1
            border_x = border_x - 10
            border_y = border_y - 10
            level_increase += 3
    else:
        snake_body.pop()
    #checking if the time exceds or not
    if time.time() - food_time_start > FOOD_TIMER or not fruit_spawn:
        fruit_position = [round(random.randrange(0+(level-1)*10, border_x - 10) / 10.0) * 10.0, round(random.randrange(0+(level-1)*10, border_y - 10) / 10.0) * 10.0 ]
        food_time_start = time.time()
        
    fruit_spawn = True
    screen.fill(BLACK)
    
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
            
    pygame.draw.rect(screen, BLUE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))                                                                                                                                                                                                                      

    if level > 1:
        pygame.draw.rect(screen, RED, pygame.Rect(0, 0, 0 + (level-1)*10, 480 ))
        pygame.draw.rect(screen, RED, pygame.Rect(0, 480-(level-1)*10, 720, 0 + (level-1)*10))
        pygame.draw.rect(screen, RED, pygame.Rect(0, 0, 720, 0 + (level-1)*10))
        pygame.draw.rect(screen, RED, pygame.Rect(720-(level-1)*10, 0, (level-1)*10, 480))
        
    
    score_collect()

    text = font3.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(text,(600, 10))
    #conditions of "game_over"
    if snake_position[0] < 0 + (level-1)*10 or snake_position[0] > border_x-10:
        game_over()
    if snake_position[1] < 0 + (level-1)*10 or snake_position[1] > border_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    
    pygame.display.update()
    clock.tick(speed)
        
    