import pygame
import time
import random
pygame.init()

display_height = 600
display_width = 800


up_key = pygame.K_w
down_key = pygame.K_s
left_key = pygame.K_a
right_key = pygame.K_d 

black = (0,0,0)
white = (255,255,255)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hyper-Space RUSH')
clock = pygame.time.Clock()

#loads my flawless hand-drawn ship image
ship_img =pygame.image.load('purp-triangle.png') 

ship_height = 27
ship_width = 22


#TO BE ADDED 
#Collision only works on top left corner of ship, FIX
#Score 
#More Enemies for Higher Score
#Max 3 lives
#Extra Lives Object logic
#Extra Lives that spawn based on score
#Extra lives generate some score, double points if excess


class collision_object:

    #Sprite size reference
    #red ship W x H : 18 x 21
    #1 up W x H : 50 x 50
    #Asteroid W x H : 24 x 21

    def __init__(self, o_x, o_y, sprite, invert_x = False):
        self.x_position = o_x
        self.y_position = o_y
        if sprite == "red_ship":
            self.height = 21
            self.width = 18
            self.speed_x = 0
            self.speed_y = 7
            self.image = pygame.image.load('red_ship.png')
        elif sprite == "asteroid":
            self.width = 24
            self.height = 21
            self.randomize_speeds()
            self.image = pygame.image.load('asteroid_small.png')
            #invert x is True when the asteroid will be moving from the Right 
            #side of the screen 
            if invert_x == True:
                self.speed_x = self.speed_x * -1 
        elif sprite == "one_up":
            self.image = pygame.image.load('one_up.png')
            self.speed_x = 0
            self.speed_y = 3

    def randomize_speeds(self):
        self.speed_x = random.randrange(1, 10)
        self.speed_y = random.randrange(3, 10)

    def redraw(self):

        game_display.blit(self.image, (self.x_position, self.y_position))

    def update(self):
        self.x_position = self.x_position + self.speed_x
        self.y_position += self.speed_y

    def has_left_screen(self, window_x, window_y):
        if self.x_position > window_x:
            return True
        elif self.x_position < -1 * self.width:
            return True
        elif self.y_position > self.height + window_y:
            return True 
        else:
            return False


    def recreate(self):
        self.x_position = -1 * self.width
        self.y_position = -1 *self.height
        self.randomize_speeds()

    def check_collision(self, obj_xs, obj_ys, obj_invuln = False):
        in_x_range = False
        in_y_range = False 
        for x_value in obj_xs:
            if x_value >= self.x_position and x_value <= self.x_position + self.width:
                in_x_range = True
        for y_value in obj_ys:
            if y_value >= self.y_position and y_value <= self.y_position + self.height:
                in_y_range = True 

        if in_x_range and in_y_range: 
            return True

def crash():
   message_display("oh dear, you're dead")

def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def message_display(text):
    #creates a font + font size 
    large_text = pygame.font.Font('freesansbold.ttf', 80)
    text_surface, text_rectangle = text_objects(text, large_text)
    #creates a reference for the location of the center of Text rect
    text_rectangle.center = (display_width * 0.50, display_height *0.40)
    # prints a Text Surface and text rectangle to the screen
    game_display.blit(text_surface, text_rectangle)

    pygame.display.flip()

    time.sleep(2)

    game_loop()

def draw_ship(x):
    game_display.blit(ship_img, x)


def game_loop():

    key = pygame.key.get_pressed()

    moving_down = key[down_key]
    moving_up = key[up_key]
    moving_left = key[left_key]
    moving_right = key[right_key]

    #creates enemy object and adds it to Enemy list
    asteroid1 = collision_object(10, 10, "asteroid")
    enemy_list = []
    enemy_list.append(asteroid1)

    #Sets the default Coord of the ship. 
    ship_x = (display_width * 0.45)
    ship_y = (display_height * 0.8)

    #initializes the change variables used for movement 
    ship_x_change = 0
    ship_y_change = 0

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                #turn left
                if event.key == left_key:
                    print("ship move left")
                    #ship_x_change -= 5
                    moving_left = True

                if event.key == right_key:
                    print("ship move right")
                    #ship_x_change += 5
                    moving_right = True
                if event.key == down_key:
                    print("ship move down")
                    #ship_y_change += 5
                    moving_down = True
                if event.key == up_key:
                    print("ship move up")
                    #ship_y_change += -5
                    moving_up = True 
                

            if event.type == pygame.KEYUP:
                if event.key == left_key:
                    #ship_x_change = ship_x_change + 5
                    moving_left = False
                if event.key == right_key:
                    #ship_x_change = ship_x_change - 5
                    moving_right = False
                if event.key == up_key:
                    #ship_y_change += 5
                    moving_up = False
                if event.key == down_key:
                    #ship_y_change -= 5
                    moving_down = False


            
        ship_x_change = 0
        ship_y_change = 0 
        if moving_left and moving_right:
            ship_x_change += 0
        elif moving_left:
            ship_x_change += -5
        elif moving_right:
            ship_x_change += 5
        if moving_up and moving_down:
            ship_y_change += 0
        elif moving_down:
            ship_y_change += 5
        elif moving_up:
            ship_y_change += -5

        
        

        ship_x = ship_x_change + ship_x
        ship_y = ship_y_change + ship_y 

        if ship_x < ship_width * -1:
            ship_x = display_width - 5
        elif ship_x > display_width:
            ship_x = ship_width * -1 

        
        if ship_y > display_height: 
            ship_y_change = 0
            
            crash()
            #ship_y = ship_height * -1
        elif ship_y < ship_height * -1:
            ship_y = display_height

        game_display.fill(black)
        #draws all enemy objets, and checks for collisions. 
        ship_xs = (ship_x, ship_x + ship_width)
        ship_ys = (ship_y, ship_y + ship_height)
        for enemy in enemy_list:
            enemy.redraw()
            if enemy.check_collision(ship_xs, ship_ys):
                crash()
            if enemy.has_left_screen(display_width, display_height):
                #spawns a new enemy if current has left screen. 
                enemy.recreate()
            #this will update Enemy X Y postion based on Speed, or delete object if it has collided or left screen.
            if enemy.check_collision()
            enemy.update()
        draw_ship((ship_x, ship_y))

        pygame.display.flip()
        clock.tick(60)

game_loop()
  
pygame.quit()
quit()
