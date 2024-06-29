import pygame
import screenmanager as sc
import states 



    
def main():
    pygame.init()
    font = pygame.font.SysFont(None, 30)
    engine = sc.DisplayEngine('Example State machine', 60, 800, 450, font)
    engine.run(states.StartState(engine, (140,140,140)))
    pygame.quit()






if __name__ == "__main__":
    main()