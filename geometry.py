import pygame
from pygame.sprite import Group 

class resize_window:
    def __init__(self, size, color, name: str) -> None:
        self.size = size
        self.color = color
        self.name = name
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption(name)
        self.start_listening()
        

    def start_listening(self):
        running = True
        while running:
        # event handling, gets all event from the event queue
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                self.screen.blit(pygame.transform.scale( self.screen, event.dict['size']), (0, 0))
                pygame.display.update()
            elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
                self.screen.fill((0, 0, 0))
                self.screen.blit(pygame.transform.scale(self.screen,  self.screen.get_size()), (0, 0))
                pygame.display.update()
            self.screen.fill(self.color)
            pygame.display.update()


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = "black"
        self.backcolor = "grey"
        self.color_active = "white"
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        self.image.fill(self.backcolor)
        if self.active:
            pygame.draw.rect(self.image, self.color_active, self.image.get_rect().inflate(-2, -2), 2)
        else:
            pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.image.blit(t_surf, (5, 5))    
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
            self.render_text()
            
class LogInManager():
    def __init__(username) -> None:
        pass


