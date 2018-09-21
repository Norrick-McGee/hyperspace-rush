import pygame
pygame.init()

display_height = 600
display_width = 800

black = (0,0,0)
white = (255,255,255)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((display_width,display_width))
pygame.display.set_caption('Hyper-Space RUSH')
clock = pygame.time.Clock()

#loads my flawless hand-drawn ship image
ship_img =pygame.image.load('purp-triangle.png')  


def ship(x,y):
    game_display.blit(ship_img, (x,y))


def game_loop():

    #Sets the default Coord of the ship. 
    ship_x = (display_width * 0.45)
    ship_y = (display_height * 0.8)

    #initializes the change variables used for movement 
    ship_x_change = 0
    ship_y_change = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                #turn left
                if event.key == pygame.K_a:
                    print("ship move left")
                    ship_x_change -= 5

                if event.key == pygame.K_d:
                    print("ship move right")
                    ship_x_change += 5
                if event.key == pygame.K_s:
                    print("ship move down")
                    ship_y_change += 5
                if event.key == pygame.K_w:
                    print("ship move up")
                    ship_y_change += -5
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    ship_x_change = ship_x_change + 5
                if event.key == pygame.K_d:
                    ship_x_change = ship_x_change - 5
                if event.key == pygame.K_w:
                    ship_y_change += 5
                if event.key == pygame.K_s:
                    ship_y_change -= 5

            
            #print(event)

        ship_x = ship_x_change + ship_x
        ship_y = ship_y_change + ship_y 

        game_display.fill(white)
        ship(ship_x, ship_y)
        pygame.display.flip()
        clock.tick(60)

game_loop()  
pygame.quit()
quit()