import pgzrun

WIDTH = 700
HEIGHT = 700
TITLE = "car game"

tank = Actor("tank" , (-50 , 350))
motor = Actor("motor" , (350 , 575))
game_over = Actor("game_over" , (350 , 350))

speed_motor = 0
score = 0
gameOver = False

def update():
    global gameOver , score , speed_motor
    
    if gameOver == False:
        tank.x += 5
    if tank.x >= 750:
        tank.x = -50

    motor.y -= speed_motor
    if motor.y <= -50:
        motor.y = 750
        score += 1

    if motor.colliderect(tank):
        speed_motor = 0
        gameOver = True

def draw():
    screen.fill("#8ed13c")
    tank.draw()
    motor.draw()
    screen.draw.text(f"score : {score}" , color = "black" , topleft = (50 , 50) , fontsize = 25)

    if gameOver == True:
        screen.fill("red")
        game_over.draw()
        screen.draw.text(f"{score}" , color = "black" , topleft = (350 , 500) , fontsize = 100)

def on_mouse_down(pos,button):
    global speed_motor 

    if gameOver == False:
        if motor.collidepoint(pos) and button == mouse.LEFT:
            speed_motor += 1

        elif motor.collidepoint(pos) and button == mouse.RIGHT and speed_motor > 0:
            speed_motor -= 1

pgzrun.go()
