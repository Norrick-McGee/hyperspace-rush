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
#Score display 
#More Enemies for Higher Score
#Max 3 lives
#Extra Lives Object logic
#Extra Lives that spawn based on score
#Extra lives generate some score, double points if excess


class collision_object:

    #Sprite size reference
    #red ship W x H : 18 x 21
    #red ship large : 77 x 66
    #1 up W x H : 50 x 50
    #Asteroid_small W x H : 50 x 50

    def __init__(self, o_x = 0, o_y = 0, sprite = "random", invert_x = False):
        self.x_position = o_x
        self.y_position = o_y
        if sprite == "red_ship":
            self.height = 66
            self.width = 77
            self.speed_x = 0
            self.speed_y = 7
            self.image = pygame.image.load('red_ship_large.png')
        elif sprite == "asteroid":
            self.width = 50
            self.height = 50
            if invert_x:
                self.randomize_speeds(False)
            else:
                self.randomize_speeds()
            self.image = pygame.image.load('asteroid_small.png')
            #invert x is True when the asteroid will be moving from the Right 
            #side of the screen 
            #if invert_x == True:
                #self.speed_x = self.speed_x * -1 
        elif sprite == "one_up":
            self.image = pygame.image.load('one_up.png')
            self.speed_x = 0
            self.speed_y = 3

        elif sprite =="random":
            self.random_enemy()

    def random_enemy(self):
        #list of enemy classes
        enemy_type = random.choice(["red_ship", "asteroid"])
        if enemy_type == "asteroid":
            
            
            if random.choice([True, False])
                self.__init__(display_width + 50, -50, enemy_type ,invert_x = True)
            else:
                self.__init__(-50, -50, enemy_type)

        elif enemy_type == "red_ship":
            delay_height = random.randrange(-200, -60)
            position = random.randrange(0, display_width)
            self.__init__(position, delay_height, enemy_type)
        

    def width_height(self):
        self.xs = (self.x_position, self.x_position + self.width)
        self.ys = (self.y_position, self.y_position + self.height)

    def randomize_speeds(self, left = True):
        if left:
            self.speed_x = random.randrange(1, 10)
            
        else:
            self.speed_x = random.randrange(-9, 0)
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

    def recreate_invertedX(self, screen_width):
        self.x_position = screen_width
        self.y_position = -1 *self.height
        self.randomize_speeds()
        self.speed_x = self.speed_x * -1

    def check_collision(self, objx, objy, objw, objh): 
        myL = self.x_position
        myR = self.x_position + self.width
        yourL = objx 
        yourR = objx + objw 
        myTop = self.y_position
        myBottom = self.y_position + self.height
        yourTop = objy 
        yourBottom = objy + objh
        x_collision = True 
        y_collision = True 

        if myL > yourL and myR > yourR and myL > yourR and myR > yourL:
            x_collision = False
        elif myL < yourL and myR < yourR and myL < yourR and myR < yourL:
            x_collision = False 
        if myTop > yourTop and myBottom > yourBottom and myTop > yourBottom and myBottom > yourTop:
            y_collision = False 
        elif myTop < yourTop and myBottom < yourBottom and myTop < yourBottom and myBottom < yourTop:
            y_collision =  False
        return x_collision and y_collision

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

def score_display(score):
    score_text = pygame.font.Font('freesansbold.ttf', 10)
    text_surface, text_rectangle = text_objects("SCORE : " +str(score), score_text)
    text_rectangle.center = (30, 20)
    game_display.blit(text_surface, text_rectangle)


def game_loop():

    score = 0.0 

    key = pygame.key.get_pressed()

    moving_down = key[down_key]
    moving_up = key[up_key]
    moving_left = key[left_key]
    moving_right = key[right_key]

    #creates enemy object and adds it to Enemy list
    number_of_enemies = 2      
    
    asteroid1 = collision_object()
    asteroid2 = collision_object()
    enemy_list = []
    enemy_list.append(asteroid1)
    enemy_list.append(asteroid2)

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






        if score > 500:
            number_of_enemies = 9
        elif score > 450:
            number_of_enemies = 8
        elif score > 400:
            number_of_enemies = 7
        elif score > 325:
            number_of_enemies = 6
        elif score > 250:
            number_of_enemies = 5
        elif score > 200: 
            number_of_enemies = 4
        elif score > 100: 
            number_of_enemies = 3

        if number_of_enemies > len(enemy_list):
            enemy_list.append(collision_object())
        

        game_display.fill(black)
        #draws all enemy objets, and checks for collisions. 
        for enemy in enemy_list:
            enemy.redraw()
            if enemy.check_collision(ship_x, ship_y, ship_width, ship_height):
                crash()
            if enemy.has_left_screen(display_width, display_height):
                #spawns a new enemy if current has left screen. 
                enemy.random_enemy()
            #this will update Enemy X Y postion based on Speed, or delete object if it has collided or left screen.
            for enemy2 in enemy_list:
                if enemy is not enemy2:
                    if enemy.check_collision(enemy2.x_position, enemy2.y_position, enemy2.width, enemy2.height):
                        #destroy both enemies and recreate them
                        print("Enemy collisions")
                        enemy.random_enemy()
                        enemy2.random_enemy()

            enemy.update()
        draw_ship((ship_x, ship_y))
        score += 0.1 
        print(int(score))
        score_display(int(score))
        pygame.display.flip()
        clock.tick(60)

game_loop()
  
pygame.quit()
quit()
