import time
from turtle import Screen
from turtle import Turtle
from PIL import Image
from time import sleep
from shooter import Shooter
from bullet import Bullet
from alien import Alien
from score import Score
from obstruct import Obstruct
import random

#
# with Image.open('alien.gif') as img:
#     img = img.resize((15, 15))
#     img.save('alien_small_1.gif')

# All lists created
aliens_to_remove = []
bullets_to_remove = []
block_to_remove = []
bullets = []  # Create a shoot bullet function to store all bullets inside a list
alien_bullets = []

# set up screen size
screen_width = 1000
screen_height = 600

# Speed of refresh
speed = 0.05

# speed of aliens
direction = 1  # Start moving right
step = 10

# Alien move down time
down_time = 4

# Distance between alien and shooter before losing
dis_btw = 10

# Location of shooter
shooter_xcor = 0
shooter_ycor = -250

# Set up screen
screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor('black')
screen.tracer(0)
screen.colormode(255)
screen.addshape('alien_small_1.gif', None)

# Create alien usable area
usable_screen_width = int(screen_width / 2 - 40)
usable_screen_height = int(screen_height / 2 - 40)




# Create all aliens
def create_aliens():
    all_aliens = []
    y = usable_screen_height
    for column in range(1, 5):
        x = -usable_screen_width
        for row in range(1, 20):
            alien = Alien(x=x, y=y)
            all_aliens.append(alien)
            x += 30
        y -= 30
    return all_aliens


aliens_mass = create_aliens()


# Move aliens
def move_aliens(aliens, direct, stp):
    if not aliens:  # Check if the list is empty
        return direct  # Return the current direction without any changes
    for ali in aliens:
        new_x = ali.xcor() + direct * stp
        # Update alien position
        ali.setx(new_x)

    # Check boundary conditions to change direction
    if direction == 1 and aliens[-1].xcor() > screen_width / 2 - 40:
        return -1  # Change direction to left
    elif direction == -1 and aliens[0].xcor() < -screen_width / 2 + 40:
        return 1  # Change direction to right
    return direction  # Continue in the same direction


def obstructions():
    objects = []
    y = -100
    for column in range(1, 5):
        x = -200
        for row in range(1, 30):
            obstructs = Obstruct(x=x, y=y)
            objects.append(obstructs)
            x += 15
        y -= 15
    return objects


all_obstruct = obstructions()

# Create shooter object
shooter = Shooter(x=shooter_xcor, y=shooter_ycor, screen_width=screen_width)


def alien_shoot_bullet():
    if aliens_mass:
        random_alien = aliens_mass[random.randint(0, len(aliens_mass) - 1)]
        x = random_alien.xcor()
        y = random_alien.ycor()
        alien_bullets.append(Bullet(x=x, y=y, head=270))


def shoot_bullet():
    bullets.append(Bullet(x=shooter.xcor(), y=shooter.ycor(), head=90))


# Assigning functions to keys
screen.listen()
screen.onkey(fun=shooter.move_left, key="a")
screen.onkey(fun=shooter.move_right, key="d")
screen.onkey(fun=shoot_bullet, key="space")


# Set up score board
score = Score(xcor=int(screen_width / 2 - 50), ycor=int(screen_height / 2 - 20), alien=aliens_mass)

game = True
start_time = time.time()
while game:
    sleep(speed)
    direction = move_aliens(aliens_mass, direction, step)

    if random.random() < 0.2 and aliens_mass:  # Adjust probability as needed
        alien_shoot_bullet()

    for alien_bul in alien_bullets[:]:
        alien_bul.shoot()
        if alien_bul.ycor() < -(screen_height / 2):
            alien_bul.hideturtle()
            alien_bullets.remove(alien_bul)

    for bullet in bullets[:]:
        bullet.shoot()
        if bullet.ycor() > screen_height / 2:
            bullet.hideturtle()
            bullets.remove(bullet)
        for alien_bul in alien_bullets:
            if bullet.distance(alien_bul) < 8:
                bullets_to_remove.append(bullet)
                bullets_to_remove.append(alien_bul)

    for alien in aliens_mass:
        for bullet in bullets:
            if bullet.distance(alien) < 12:
                aliens_to_remove.append(alien)
                bullets_to_remove.append(bullet)
        for blocks in all_obstruct:
            if blocks.distance(alien) < 12:
                block_to_remove.append(blocks)

        if alien.distance(shooter) < dis_btw or alien.ycor() < shooter_ycor + 30:
            score.lose(xcor=int(screen_width / 2 - 50), ycor=int(screen_height / 2 - 40), )
            game = False
            break

        if score.score == score.total_alien or len(aliens_mass) == 0:
            score.win(xcor=int(screen_width / 2 - 50), ycor=int(screen_height / 2 - 40), )
            screen.update()  # Ensure the screen updates
            game = False
            break

    for block in all_obstruct:
        for bullet in bullets:
            if block.distance(bullet) < 10:
                block_to_remove.append(block)
                bullets_to_remove.append(bullet)
        for ali_bul in alien_bullets:
            if block.distance(ali_bul) < 10:
                block_to_remove.append(block)
                bullets_to_remove.append(ali_bul)

    for ali_bul in alien_bullets:
        if shooter.distance(ali_bul) < 20:
            score.lose(xcor=int(screen_width / 2 - 50), ycor=int(screen_height / 2 - 40), )
            game = False
            break

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullet.hideturtle()
            bullets.remove(bullet)
        if bullet in alien_bullets:
            bullet.hideturtle()
            alien_bullets.remove(bullet)

    for block in block_to_remove:
        if block in all_obstruct:
            block.hideturtle()
            all_obstruct.remove(block)

    for ali in aliens_to_remove:
        if ali in aliens_mass:
            ali.hideturtle()
            aliens_mass.remove(ali)
            score.add_score()

    if time.time() - start_time > down_time:
        for ali in aliens_mass:
            ali.sety(ali.ycor() - 10)
        start_time = time.time()

    screen.update()
screen.exitonclick()
