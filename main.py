import pygame
import start
import geometry as geo


def main():
    pygame.init()
    font = pygame.font.SysFont(None, 30)
    screen = start.start_window(400,200, (140,140,140), font)
    screen.run()
    







if __name__ == "__main__":
    main()