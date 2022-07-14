import pygame as pygame
import random
import time
# Init Pygame
pygame.init()

'''
Icon data
enemy_icon = <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
'''
# Setting Up Icons
background = pygame.image.load('bg.png')
game_icon = pygame.image.load('Game_icon.png')
enemy_icon = pygame.image.load('enemy.png')
player_icon = pygame.image.load('player.png')
scissors_icon = pygame.image.load('scissors.png')
paper_icon = pygame.image.load('paper.png')
rock_icon = pygame.image.load('rock.png')
# Set the Screen
screen = pygame.display.set_mode((1000,670))
pygame.display.set_caption('Rock Paper Scissors')
pygame.display.set_icon(game_icon)
# Make fonts
font = pygame.font.Font('freesansbold.ttf', 31)
font_counter = pygame.font.Font("freesansbold.ttf",38)
font_small = pygame.font.Font('freesansbold.ttf', 25)
# Make Labels
enemy_label = font.render('Enemy',True,(160,20,20))
player_label = font.render('You',True,(250,0,220))
def Onetwothree():
    global x
    if x > 0 and x != 11:
        screen.blit(Counter,(490,30))
        
def Get_result(rock,paper,scissors,enemy_choice):
    if ((enemy_choice == 'scissors' and scissors) or (enemy_choice == 'rock' and rock) or (enemy_choice == 'paper' and paper)):
        return 'Tie'
    elif ((enemy_choice == 'scissors' and (not(rock))) or (enemy_choice == 'paper' and (not(scissors))) or (enemy_choice == 'rock' and (not(paper)))):
        return 'Loss'
    else:
        return 'Win'
rock = False
paper = False
scissors = False
in_game = False
running = True
done_q = False
x = 11
result = False
def ShowChoices():
    screen.blit(font.render("R for ", True, (0,0,0)),(10,600))
    screen.blit(rock_icon,(85,575))
    screen.blit(font.render(", P for ", True, (0,0,0)), (150,600))
    screen.blit(paper_icon,(240,575))
    screen.blit(font.render(", S for ", True, (0,0,0)), (300,600))
    screen.blit(scissors_icon,(385,575))
def enemyreturn():
    x = random.randint(0,2)
    if x == 0:
        return 'scissors'
    elif x == 1:
        return 'paper'
    elif x == 2:
        return 'rock'
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,-300))
    screen.blit(enemy_label,(865,210))
    screen.blit(enemy_icon,(850,250))
    screen.blit(player_icon,(10,250))
    screen.blit(player_label,(50,210))
    if not(in_game):
        screen.blit(font_small.render("press Space to start", True, (0,0,0)),(10,10))
    ShowChoices()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                done_q = True
                in_game = True
            if event.key == pygame.K_s:
                if in_game:
                    scissors = True
            if event.key == pygame.K_p:
                if in_game:
                    paper = True
            if event.key == pygame.K_r:
                if in_game:
                    rock = True
                
    
    # Check For Counter + Display Counter If Check
    if done_q == True:
        if x > 0:
            x -= 1
            Counter = font_counter.render("{}".format(str(x)), True, (0,0,0))
            time.sleep(1)
        else:
            done_q = False
            in_game = False
            x = 11
    if done_q:
        try:
            Onetwothree()
        except Exception:
            pass
    if (rock or scissors or paper) and in_game:
        in_game = False
        done_q = False
        enemy_choice = enemyreturn()
        result = True
        get_result = Get_result(rock,paper,scissors,enemy_choice)
        x = 11
        paper = False
        rock = False
        scissors = False
    if not(in_game) and result :
        if get_result == 'Tie':
            if not(in_game):
                screen.blit(font_counter.render('TIE', True,(0,0,0)), (430,320))
                screen.blit(font_counter.render('Enemy has chosen {}'.format(enemy_choice), True,(0,0,0)),(280,400))
        if get_result == 'Loss':    
            if not(in_game):
                screen.blit(font_counter.render("You Loose", True, (0,0,0)),(430,320))
                screen.blit(font_counter.render('Enemy has chosen {}'.format(enemy_choice), True,(0,0,0)),(280,400))
        if get_result == 'Win':
            if not(in_game):
                screen.blit(font_counter.render("You Win", True, (0,0,0)),(430,320))
                screen.blit(font_counter.render('Enemy has chosen {}'.format(enemy_choice), True,(0,0,0)),(280,400))

                   
                   
    pygame.display.update()