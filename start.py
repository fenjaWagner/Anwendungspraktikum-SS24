import pygame
import geometry as geo


class start_window(pygame.sprite.Sprite):
    def __init__(self, size_x, size_y, color, font) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.screen = pygame.display.set_mode((self.size_x, self.size_y))
        self.font = font
        self.user_text = self.font.render("Username:", False, 0, self.color)
        self.new_user_text = self.font.render("Sign up:", False, 0, self.color)   
        self.group = pygame.sprite.Group()
        self.user_input = geo.TextInputBox(20, self.size_y * 5 //15, self.size_x -40, self.font)
        self.group.add(self.user_input)
        self.new_user_input = geo.TextInputBox(20, self.size_y *11 //15, self.size_x -40, self.font)
        self.group.add(self.new_user_input)
        self.running = True
        pygame.display.set_caption("Funny Game")
        
    def update(self):
        self.screen.fill(self.color)
        self.group.draw(self.screen)
        self.screen.blit(self.user_text, (20, self.size_y*3 // 15))
        self.screen.blit(self.new_user_text, (20, self.size_y *9// 15))
        pygame.display.flip()
        pygame.display.update()


    def listening(self):   
        event_list = pygame.event.get() 
        self.group.update(event_list)
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
            #elif event.type == pygame.VIDEORESIZE:
            #    self.screen.blit(pygame.transform.scale( self.screen, event.dict['size']), (0, 0))
                
            #elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
            #    self.screen.fill((0, 0, 0))
            #    self.screen.blit(pygame.transform.scale(self.screen,  self.screen.get_size()), (0, 0))
                

    

    def run(self):
        while self.running:
            self.listening()
            self.update()

                    
