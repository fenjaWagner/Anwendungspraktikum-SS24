import pygame
import screenmanager as sc
import states 
    
def main():
    pygame.init()
    engine = sc.DisplayEngine()
    engine.run(states.StartState(engine))
    pygame.quit()

if __name__ == "__main__":
    main()