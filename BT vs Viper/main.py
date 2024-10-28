import pgzrun
import random

HEIGHT = 720
WIDTH = 1080

TITLE = "viper vs bt"

viper = Actor("viper.webp")
viper.pos = (WIDTH//2,HEIGHT//2)
bt = Actor("bt.webp")
bt.pos = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
score = 0
is_game_over = False

def move_bt():
    bt.pos =(random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))

def draw():
    screen.fill(color = "green")
    screen.blit("backround",(0,0))
    viper.draw()
    bt.draw()


    screen.draw.text("score = {}".format(score),color = "black",topleft = (540,50),fontsize = 35)
    if is_game_over:
        screen.fill(color = "red")
        screen.draw.text("Game over score - {}".format(score),color = "black",midtop = (540,0),fontsize = 50)


def update():
    global score
    if keyboard.left:
        viper.x -= 2
    if keyboard.right:
        viper.x += 2
    if keyboard.up:
        viper.y -= 2
    if keyboard.down:
        viper.y += 2
    if viper.colliderect(bt):
        score += 10
        move_bt()

def game_over():
    global is_game_over
    is_game_over = True

clock.schedule(game_over,60.0)
pgzrun.go()