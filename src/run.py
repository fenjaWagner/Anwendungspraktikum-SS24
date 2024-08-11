import pygame
import screenmanager as sc
import states 
    
def run():
    pygame.init()
    # Build display engine
    engine = sc.DisplayEngine()
    # Start the engine with the first state: StartState (for log in)
    engine.run(states.StartState(engine))
    pygame.quit()

if __name__ == "__main__":
    run()