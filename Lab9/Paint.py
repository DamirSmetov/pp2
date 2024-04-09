import pygame

#initializing constants
SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
TRIANGLE = 'TRIANGLE'

dis_width = 640
dis_height = 480
main_screen_size = (dis_width, dis_height)
elements_to_draw = []

icon_top_bar_height = 50
icon_top_bar_width = 50
icon_rectangle_start_x = 0
icon_rectangle_end_x = 50
icon_circle_start_x = 50
icon_circle_end_x = 100
icon_square_start_x = 100
icon_square_end_x = 150
icon_rigth_triangle_start_x = 150
icon_rigth_triangle_end_x = 200
icon_equil_triangle_start_x = 200
icon_equil_triangle_end_x = 250
icon_rhombus_start_x = 250
icon_rhombus_end_x = 300
 


icon_red_color_start_y = 50
icon_red_color_end_y = 100
icon_blue_color_start_y = 100
icon_blue_color_end_y = 150
icon_color_shape_width = 40
icon_color_shape_height = 30



white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)

last_pos = (0, 0)


"""
def draw_all_shapes(screen):
  for element in elements_to_draw:
    if element['shape'] == SQUARE:
      pygame.draw.rect(screen, element['color'],
                       [element['x'], element['y'], 50, 50])
    elif element['shape'] == CIRCLE:
      pygame.draw.circle(screen, element['color'],
                         (element['x'], element['y']), element['radius'])
"""
#functions for drawing geometric figures
def add_element_square(screen,color, x, y):
  pygame.draw.rect(screen, color, (x,y, 50, 50))
  
def add_element_equil_triangle(screen, color, x, y):
  pygame.draw.polygon(screen, color, ((x, y), (x+50, y-40), (x+100, y)))
  
def add_element_rhombus(screen, color, x, y):
  pygame.draw.polygon(screen, color, ((x,y), (x+50, y-70), (x+100, y), (x+50, y+70)))

def add_element_rectangle(screen,color, x, y):
  pygame.draw.rect(screen, color, (x,y, 80, 50))

def add_element_circle(screen, color, x, y, radius):
  pygame.draw.circle(screen, color, (x,y), radius)

def add_element_right_triangle(screen, color, x, y):
  pygame.draw.polygon(screen, color, ((x, y), (x+50, y), (x+50, y+50)))
  pass

#drawing line
def drawline(screen, color, start, end, radius):
  Xaxis= end[0] - start[0]
  Yaxis = end[1] - start[1]
  dist = max(abs(Xaxis), abs(Yaxis))
  for i in range(dist):
    x = int(start[0]+float(i)/dist*Xaxis)
    y = int(start[1]+float(i)/dist*Yaxis)
    pygame.draw.circle(screen, color, (x, y), radius)
    print(x, y)

#interface
def draw_main_icons(screen):
  # tabs
  pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, 40))
  pygame.draw.rect(screen, right_tab_color,
                   (dis_width - 80, 0, 80, dis_height))
  #icons horizontal
  pygame.draw.rect(screen, white, (icon_rectangle_start_x + 5, 5, 40, 30))
  pygame.draw.rect(screen, black, (icon_rectangle_start_x + 10, 10, 30, 20))

  pygame.draw.rect(screen, white, (icon_circle_start_x + 5, 5, 40, 30))  
  pygame.draw.circle(screen, black, (icon_circle_start_x + 25, 20), 10)
  
  pygame.draw.rect(screen, white, (icon_square_start_x + 5, 5, 40, 30))
  pygame.draw.rect(screen, black, (icon_square_start_x + 15, 10, 20, 20))
  
  pygame.draw.rect(screen, white, (icon_rigth_triangle_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, black, ((icon_rigth_triangle_start_x + 15, 10,), (icon_rigth_triangle_start_x + 35, 10,), (icon_rigth_triangle_start_x + 35, 30,)))
  
  pygame.draw.rect(screen, white, (icon_equil_triangle_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, black, ((icon_equil_triangle_start_x + 35, 30,), (icon_equil_triangle_start_x + 25, 10,), (icon_equil_triangle_start_x + 15, 30,)))
  
  pygame.draw.rect(screen, white, (icon_rhombus_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, black, ((icon_rhombus_start_x + 15, 20,), (icon_rhombus_start_x + 25, 10,), (icon_rhombus_start_x + 35, 20,), (icon_rhombus_start_x + 25, 30,)))
  

  # colors
  pygame.draw.rect(screen, red,
                   (dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
  pygame.draw.rect(screen, blue,
                   (dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))
  erasor = pygame.transform.scale(pygame.image.load("eraser-icon.png"), (icon_color_shape_width, icon_color_shape_height))
  screen.blit(erasor, (dis_width-70, 150))
  
  

#main function
def main():
  pygame.init()
  screen = pygame.display.set_mode(main_screen_size)
  clock = pygame.time.Clock()
  screen.fill((255, 255, 255))


  x = 0
  y = 0
  mode = 'blue'
  points = []
  is_rectangle_drawer = False
  is_circle_drawer = False
  is_square_drawer = False
  is_rigth_triangle_drawer = False
  is_equil_triangle_drawer = False
  is_rhombus_drawer = False
  is_eraser = False
  draw_on = False
  color = black
  radius = 1
  last_pos = (0, 0)



  while True:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and ctrl_held:
          return
        if event.key == pygame.K_F4 and alt_held:
          return
        if event.key == pygame.K_ESCAPE:
          return
      #checking what colour and shape are chosen
      if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()
        if event.button == 1:
          if position[0] <= icon_rectangle_end_x and position[
            0] > 0 and position[1] < icon_top_bar_height:
            is_rectangle_drawer = not is_rectangle_drawer
            is_circle_drawer = False
            is_equil_triangle_drawer = False
            is_square_drawer = False
            is_rigth_triangle_drawer = False
            is_rhombus_drawer = False
            print('is_rectangle_drawer = True')
          elif position[0] <= icon_circle_end_x and position[
            0] > icon_circle_start_x and position[1] < icon_top_bar_height:
            is_circle_drawer = not is_circle_drawer
            is_rectangle_drawer = False
            is_square_drawer = False
            is_rigth_triangle_drawer = False
            is_rhombus_drawer = False 
            is_equil_triangle_drawer = False
            print('is_circle_drawer = True')
          elif position[0] <= icon_square_end_x and position[
            0] > icon_square_start_x and position[1] < icon_top_bar_height:
            is_square_drawer = not is_square_drawer
            is_rigth_triangle_drawer = False
            is_rhombus_drawer = False
            is_rectangle_drawer = False
            is_circle_drawer = False
            is_equil_triangle_drawer = False
          elif position[0] <= icon_rigth_triangle_end_x and position[
            0] > icon_rigth_triangle_start_x and position[1] < icon_top_bar_height:
            is_rigth_triangle_drawer = not is_rigth_triangle_drawer
            is_rhombus_drawer = False
            is_square_drawer = False
            is_circle_drawer = False
            is_equil_triangle_drawer = False
            is_rectangle_drawer = False
          elif position[0] <= icon_equil_triangle_end_x and position[
            0] > icon_equil_triangle_start_x and position[1] < icon_top_bar_height:
            is_equil_triangle_drawer = not is_equil_triangle_drawer
            is_rhombus_drawer = False
            is_rectangle_drawer = False
            is_circle_drawer = False
            is_rectangle_drawer = False
            is_rigth_triangle_drawer = False
          elif position[0] <= icon_rhombus_end_x and position[
            0] > icon_rhombus_start_x and position[1] < icon_top_bar_height:
            is_rhombus_drawer = not is_rhombus_drawer
            is_rectangle_drawer = False
            is_circle_drawer = False
            is_rectangle_drawer = False
            is_rigth_triangle_drawer = False
            is_equil_triangle_drawer = False
            
          elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_red_color_start_y and position[1] < icon_red_color_end_y:
            color = red
          elif position[0] >= dis_width -70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_blue_color_start_y and position[1] < icon_blue_color_end_y:
            color = blue
          elif position[0] >= dis_width - 70 and position[0] < dis_width-70 + icon_color_shape_width and position[1] > 110 and position[1] < 250:
            is_eraser = not is_eraser
            is_circle_drawer = False
            is_rectangle_drawer = False
            is_rigth_triangle_drawer = False
            is_equil_triangle_drawer = False
            is_rhombus_drawer = False
            
          elif is_rectangle_drawer:
            add_element_rectangle(screen, color, position[0], position[1])
          elif is_circle_drawer:
            add_element_circle(screen, color, position[0], position[1], 20)
          elif is_square_drawer:
            add_element_square(screen, color, position[0], position[1])
          elif is_rigth_triangle_drawer:
            add_element_right_triangle(screen, color, position[0], position[1])
          elif is_equil_triangle_drawer:
            add_element_equil_triangle(screen, color, position[0], position[1])
          elif is_rhombus_drawer:
            add_element_rhombus(screen, color, position[0], position[1])
          draw_on = True
          

      if event.type == pygame.MOUSEBUTTONUP:
        draw_on = False
      #conditions fot line drawing 
      if event.type == pygame.MOUSEMOTION: 
        position = pygame.mouse.get_pos()
        if draw_on and position[0] < dis_width-80 and position[1] > 40:
          if is_eraser:
            pygame.draw.circle(screen, white, event.pos, 20) 
            drawline(screen, white, event.pos, last_pos, 20)
          else:
            pygame.draw.circle(screen, color, event.pos, radius) 
            drawline(screen, color, event.pos, last_pos, radius)
        last_pos = event.pos
          
    draw_main_icons(screen)
    pygame.display.update()
    clock.tick(60)

main()
