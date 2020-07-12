import pygame
import random
pygame.init()


# screen dimensions
screen_width = 800
screen_height = 600



# colors
black = (0 ,0,0)
white = (255 , 255 , 255)
red =   (255 ,0 , 0)


# Game window
game_window = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("SNAKE")
pygame.display.update()

# game specifics


# food
food_x = random.randint(20 , screen_width)
food_y = random.randint(20 , screen_height)
food_size = 10



with open("high_score.txt" , "r") as f:
    highscore = f.read()







clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 55)

def text_score(text , color , x , y):     # function for displaying the text on screen
    screen_text = font.render(text , True , color)
    game_window.blit(screen_text , [x , y])




def plot_snake (game_window , color , snake_list, snake_size): # plotting of the snake

    for x ,y in snake_list:
        pygame.draw.rect(game_window , color , [x , y ,snake_size , snake_size])



def welcome():
    global clock
    exit_game = False
    while not exit_game:
        game_window.fill((233 , 220 , 229))
        text_score("Welcome to SNAKE game" , black , 160 , 240)
        text_score("Press SPACEBAR to PLAY" , black , 150 , 310)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()



        pygame.display.update()
        clock.tick(60)



# main Loop

def game_loop ():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 8
    snk_list = []
    snake_length = 1
    score = 0
    food_x = random.randint(20, screen_width)
    food_y = random.randint(20, screen_height)
    food_size = 10
    global highscore

    while not exit_game:
        if game_over :

            with open("high_score.txt" , "w") as f:
                f.write(str(highscore))



            game_window.fill(white)
            text_score(f"Game Over ! Press Enter to Play Again" , red , 60 , 260)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

                    


        else:

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0


                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0


            snake_x += velocity_x  # incrementing of the position of the snake
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:  # food eating system and new food generation
                score += 10
                food_x = random.randint(80, screen_width // 2)
                food_y = random.randint(80, screen_height // 2)
                snake_length += 2
                if score > int(highscore):
                    highscore = score


            game_window.fill(black)
            text_score(f"Score : {score}   High Score : {highscore}", (255, 255, 0), 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list) > snake_length:
                del snk_list[0]


            if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height :
                game_over = True
                # print(game_over)


            if head in snk_list[:-1]:
                game_over = True


            plot_snake(game_window , white ,snk_list , snake_size )



        # pygame.draw.rect(game_window , white , snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



if __name__ == '__main__':
    welcome()
    # game_loop()
    pygame.quit()
    quit()
