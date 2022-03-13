import pygame

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, yvel):
        self.y += yvel

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosY(self, ypos):
        self.y = ypos

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))

P1_SIZE_X, P1_SIZE_Y = 8, 110

# Paddles
p1 = Paddle(P1_SIZE_X, HEIGHT/2 - P1_SIZE_Y/2, P1_SIZE_X, P1_SIZE_Y)
p2 = Paddle((WIDTH - P1_SIZE_X) - P1_SIZE_X, HEIGHT/2 - P1_SIZE_Y/2, P1_SIZE_X, P1_SIZE_Y)


def draw_window():
    p1.draw()
    p2.draw()
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


def main():
    run = True
    paddle_vel = 8
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        # PADDLE #1
        if keys_pressed[pygame.K_w]:
            p1.move(-paddle_vel)
        elif keys_pressed[pygame.K_s]:
            p1.move(paddle_vel)
        # PADDLE #2
        if keys_pressed[pygame.K_UP]:
            p2.move(-paddle_vel)
        elif keys_pressed[pygame.K_DOWN]:
            p2.move(paddle_vel)

        setBoundries(p1, p2)        

        
        WIN.fill((BLACK))
        draw_window()

    pygame.quit()
    

if __name__ == "__main__":
    main()


        