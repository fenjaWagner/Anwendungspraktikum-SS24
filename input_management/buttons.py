import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, font, text=''):
        super().__init__()
        self.color = (110,110,110)
        self.color_hovered = (120,120,120)
        self.pos = (x,y)
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.hovered = False
        #self.button_surface = pygame.Surface(self.width, self.height)
        #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        #self.image.fill(self.color)
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        
    def render_button(self):
        """Renders the textbox, displays wether active, draws written text.
        """
        #t_surf = self.font.render(self.text, True, 0, self.color)
        #self.image = pygame.Surface(((max(self.width, t_surf.get_width()+10)), max(t_surf.get_height()+10, self.height)), pygame.SRCALPHA)
        #self.rect = self.image.get_rect(topleft = self.pos)
        if self.hovered:
            #self.rect(self.image, self.color_hovered, self.image.get_rect().inflate(-2, -2), 2)
            pygame.draw.rect(self.surface, self.color, self.button_rect.inflate(-2, -2), 2)
        else:
            pygame.draw.rect(self.surface, self.color_hovered, self.button_rect.inflate(-2, -2), 2)
       
        #self.image.blit(self.image, (5, 5))    
        


    def update(self, event):
        
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(pos):
                hovered = True
            else:
                hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if self.button_rect.collidepoint(event.pos):
                pass
        self.render_button()
            