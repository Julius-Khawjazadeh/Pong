import pygame

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)

def draw_window():
    pygame.display.update()


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    WIN.fill((BLACK))
    draw_window()
    

if __name__ == "__main__":
    main()


        