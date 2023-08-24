import pgzrun

WIDTH = 1000
HEIGHT = 700
TITLE = "football_game"

sun = Actor("sun" , (-120 , 350))
star = Actor("star" , (-120 , 350))
moon = Actor("moon" , (-120 , 350))

speedStars = 10

def update():
    global speedStars  
    sun.x += speedStars
    if sun.x >= WIDTH:
        star.x += speedStars
    if star.x >= WIDTH:
        moon.x += speedStars
    
    if moon.x >= WIDTH:
        sun.x = -120
        star.x = -120
        moon.x = -120
        speedStars += 10
    print(speedStars)    

    

    
def draw():
    
    screen.fill("#ffd505")

    if sun.x >= WIDTH:
        screen.fill("#030303")


    if star.x <= WIDTH and sun.x >= WIDTH:
        screen.fill("#696969")


    sun.draw()
    star.draw()
    moon.draw()

pgzrun.go()