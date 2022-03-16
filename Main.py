import pygame
import random

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

ballVel = 3
starting_dir_list = [-ballVel, ballVel]

class PongEntity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getRect(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))

    def moveY(self, yvel):
        self.y += yvel

    def moveX(self, xvel):
        self.x += xvel

    def move(self, xvel, yvel):
        self.x += xvel
        self.y += yvel

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosY(self, ypos):
        self.y = ypos

    def setPosX(self, xpos):
        self.x = xpos

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))

class Ball (PongEntity):
    pass

class Paddle (PongEntity):
    def getPaddleTop(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height/2))

    def getPaddleBottom(self):
        return pygame.Rect((self.x, self.y + self.height/2), (self.width, self.height/2))

class Divider:
    def __init__(self, x, width, height):
        self.block_positions = []
        self.x = x
        self.width = width
        self.height = height
        self.rect_dist = 5

        for i in range(int(HEIGHT / (self.height + self.rect_dist))):
            self.y = i * (self.rect_dist + self.height)
            self.block_positions.append(self.y) 
       

    def draw(self):
        for y in self.block_positions:
          pygame.draw.rect(WIN, WHITE, (self.x, y, self.width, self.height))
    

P1_SIZE_X, P1_SIZE_Y = 8, 110
B_SIZE = 10
D_SIZE_X = 4
D_SIZE_Y = 80

# Paddles

p1 = Paddle(P1_SIZE_X, HEIGHT/2 - P1_SIZE_Y/2, P1_SIZE_X, P1_SIZE_Y)
p2 = Paddle((WIDTH - P1_SIZE_X) - P1_SIZE_X, HEIGHT/2 - P1_SIZE_Y/2, P1_SIZE_X, P1_SIZE_Y)

DIVIDER_WIDTH, DIVIDER_HEIGHT = 4, 20

# BALL
ball_reset_posX = WIDTH/2 - B_SIZE/2
ball_reset_posY = HEIGHT/2 - B_SIZE/2
b = Ball(WIDTH/2 - B_SIZE/2, HEIGHT/2 - B_SIZE/2, B_SIZE, B_SIZE)
divider = Divider(WIDTH/2 - DIVIDER_WIDTH/2, DIVIDER_WIDTH, DIVIDER_HEIGHT)



def draw_window():
    p1.draw()
    p2.draw()
    b.draw()
    divider.draw()
    pygame.display.update()

def setBoundries(p1, p2):
    if p1.y + p1.getHeight() > HEIGHT:
        p1.setPosY(HEIGHT - p1.getHeight())
    elif p1.y < 0:
        p1.setPosY(0)
    if p2.y + p2.getHeight() > HEIGHT:
        p2.setPosY(HEIGHT - p2.getHeight())
    elif p2.y < 0:
        p2.setPosY(0)

def reset_ball(b):
    b.setPosX(ball_reset_posX)
    b.setPosY(ball_reset_posY)
    

def main():
    run = True
    paddle_vel = 8
    clock = pygame.time.Clock()
    dirX = starting_dir_list[random.randrange(0, len(starting_dir_list))] # randomizing whoever gets the ball first
    dirY = starting_dir_list[random.randrange(0, len(starting_dir_list))] # randomizing whoever gets the ball first

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        # PADDLE #1
        if keys_pressed[pygame.K_w]:
            p1.moveY(-paddle_vel)
        elif keys_pressed[pygame.K_s]:
            p1.moveY(paddle_vel)
        # PADDLE #2
        if keys_pressed[pygame.K_UP]:
            p2.moveY(-paddle_vel)
        elif keys_pressed[pygame.K_DOWN]:
            p2.moveY(paddle_vel)

        # BALL PHYSICS
        b.move(dirX, dirY)

        if b.getY() < 0:
            dirY *= -1
        elif b.getY() + b.getHeight() > HEIGHT:
            dirY *= -1

        if p1.getPaddleTop().colliderect(b.getRect()) and dirY > 0:
            print("TOP going down")
            dirY *= -1
            dirX *= -1
        elif p1.getPaddleTop().colliderect(b.getRect()) and dirY < 0:
            print("TOP going up")
            dirX *= -1
        elif p1.getPaddleBottom().colliderect(b.getRect()) and dirY > 0:
            print("Bottom going down")
            dirX *= -1
        elif p1.getPaddleBottom().colliderect(b.getRect()) and dirY < 0:
            print("Bottom going up")
            dirY *= -1
            dirX *= -1
        
        if p2.getPaddleTop().colliderect(b.getRect()) and dirY > 0:
            print("TOP going down")
            dirY *= -1
            dirX *= -1
        elif p2.getPaddleTop().colliderect(b.getRect()) and dirY < 0:
            print("TOP going up")
            dirX *= -1
        elif p2.getPaddleBottom().colliderect(b.getRect()) and dirY > 0:
            print("Bottom going down")
            dirX *= -1
        elif p2.getPaddleBottom().colliderect(b.getRect()) and dirY < 0:
            print("Bottom going up")
            dirY *= -1
            dirX *= -1
        

        if b.getX() < 0:
            # player one wins a point
            reset_ball(b)
            dirY *= -1
            dirX *= -1
        elif b.getX() + b.getWidth() > WIDTH:
            # player two wins a point
            reset_ball(b)
            dirY *= -1
            dirX *= -1


        

        setBoundries(p1, p2)        

        
        WIN.fill((BLACK))
        draw_window()

    pygame.quit()
    

if __name__ == "__main__":
    main()


        