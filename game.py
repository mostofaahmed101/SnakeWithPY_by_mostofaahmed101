#  Requirement: python , pygame module , all image-audio-document source
'''
                    cheat Code :
        key x --> Help menu
        key 2 --> increase score 2
        
'''

        # Module import
import pygame as pg
import random


        # initialize program
pg.mixer.init()
pg.init()


            # Colors RGB
white = (255,255,255)
red = (255,0,0)
black = (0, 0, 0)


            # Set Display 
display_width = 900
display_height = 600
display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('SnakeWithPy By MoStOfA  AhMeD')             # <-- Title of this game


            # load the Back-Ground Image
bg = pg.image.load('assets/BG.jpg')
bg = pg.transform.scale(bg, (display_width, display_height)).convert_alpha()

clock = pg.time.Clock()                                             # <-- for set FPS to get better Performence


            # creating screen_text function for put text in screen/window
def screen_text(text, color, x,y, fontSize):
    font = pg.font.SysFont(None, fontSize)                          # <-- set font
    sText = font.render(text, True, color)
    display.blit(sText, [x,y])


            # creating plot_snake_length function for increase the length
def plot_snake_length(display, color, snake_length_list, snake_size):
    for x,y in snake_length_list:
        pg.draw.rect(display, color, [x, y, snake_size, snake_size])


            # creating c_code function for help or make easy to play this game
def c_code():
    game_exit = False
    fps = 60
    while not game_exit:
        display.fill(white)
        screen_text('q --> Back to the Home page', black, 20, 50, 30)
        screen_text('r --> Reset HighScore [Home]', black, 20, 80, 30)

        for event in pg.event.get():                                    # <-- for get all key and mouse log
            if event.type == pg.QUIT:
                print('Exit Game')
                game_exit = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    welcome()
                if event.key == pg.K_r:
                    with open('assets/highscore.txt', 'w') as f:
                        f.write('0')
                        
        pg.display.update()
        clock.tick(fps)



            # creating welcome function for open this game and show a home section
def welcome():
    pg.mixer.music.load('assets/BGS.mp3')                                      # <-- Load the Back-Ground Music
    pg.mixer.music.play()

    game_exit = False
    fps = 60
    while not game_exit:
        display.fill(white)
        display.blit(bg, (0,0))                                         # <-- Set the BackGround Image

        screen_text('Snake With Py', white, 310, 250, 50)               # <-- Game Name
        screen_text('By MoStOfA AhMeD', white, 355, 290, 35)            # <-- Creator Name
        screen_text('Press Space tab for Play -->', white, 300, 570, 25)

        for event in pg.event.get():                                    # <-- for get all key and mouse log
            if event.type == pg.QUIT:
                print('Exit Game')
                game_exit = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    with open('assets/highscore.txt', 'w') as f:
                        f.write('0')
                if event.key == pg.K_x:
                    c_code()
                if event.key == pg.K_SPACE:
                    Gameloop()
                
        pg.display.update()
        clock.tick(fps)
    


            # creating Gameloop function for start this game
def Gameloop():

                # Game Veriables
    game_exit = False
    game_over = False
    snake_size = 10
    snake_x = 445
    snake_y = 295
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3
    food_x = random.randint(20, display_width / 2)
    food_y = random.randint(50, display_height / 2)
    food_size = 8
    score = 0
    fps = 60
    snake_length = 1
    increase_snake_length = 3
    snake_length_list = []

    with open('assets/highscore.txt', 'r') as f:                           # <-- Load the HighScore file
        highscore = f.read()


            # Game loop start
    while not game_exit:
        display.fill(white)

                                # Game_Over Sction
        if game_over:
            with open('assets/highscore.txt', 'w') as f:
                f.write(str(highscore))
            screen_text('GAME OVER!:)--> Press Enter for continue', red, 150, display_height / 2.1, 40)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print('Your Total Score :', score)
                    print('Exit Game')
                    game_exit = True
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        welcome()

        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:                       # <-- Game Quit
                    with open('assets/highscore.txt', 'w') as f:
                        f.write(str(highscore))                 # <-- Re-Write the HighScore file
                    game_exit = True
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pg.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pg.K_UP:
                        velocity_x = 0
                        velocity_y = - init_velocity

                    if event.key == pg.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

                    if event.key == pg.K_2:                 # <-- cheat key 
                        score +=2
                        if score > int(highscore):
                            highscore = score


                        # increase the velocity for move snake
            snake_x += velocity_x
            snake_y += velocity_y


                        # colide section for snake and food colide
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 1
                food_x = random.randint(20, display_width / 2)
                food_y = random.randint(50, display_height / 2)
                snake_length += increase_snake_length
                
                if score > int(highscore):                          # <-- for Equale the score and highscore when both are same
                    highscore = score


            screen_text(('Score : '+ str(score) + '  --  HighScore : ' + str(highscore)), red, 10, 10, 35)   # <-- Score Display
            pg.draw.rect(display, red, [food_x, food_y, food_size, food_size])                               # <-- food draw


                        # Snake_length Section
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_length_list.append(head)

            if len(snake_length_list)>snake_length:                                                     # <-- Adjustment the snake length
                del snake_length_list[0]

            plot_snake_length(display, black, snake_length_list, snake_size)                            # <-- snake Draw


                        # Game Over Sction
            if head in snake_length_list[:-1]:
                game_over = True
                pg.mixer.music.load('game_over.wav')                                                    # <-- Load the Game-Over Music
                pg.mixer.music.play()

            if snake_x < 0 or snake_x > display_width or snake_y < 0 or snake_y > display_height:
                game_over = True
                pg.mixer.music.load('assets/game_over.wav')                                                    # <-- Load the Game-Over Music
                pg.mixer.music.play()

        pg.display.update()                                                                             
        clock.tick(fps)                                                                                 # <-- set FPS

    pg.quit()                                               # <-- Quit program
    quit()





welcome()     # <-- Start this software program
