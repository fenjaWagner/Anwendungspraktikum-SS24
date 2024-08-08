import pygame
import screenmanager as sc
import states 



    
def main():
    pygame.init()
    font = pygame.font.SysFont(None, 30)
    engine = sc.DisplayEngine(font)
    engine.run(states.StartState(engine))
    pygame.quit()






if __name__ == "__main__":
    main()