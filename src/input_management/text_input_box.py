import pygame

class TextInputBox(pygame.sprite.Sprite):
    """Displays a textinputbox at given coordinates.

    Args:
        sprite object to make it manageble
    """
    def __init__(self, x, y, w, font):
        """Initilizes the Inputbox 

        Args:
            x (int): x coordinate
            y (int): y coordinate
            w (int): width of the box
            font (_type_): font that should be used
        """
        super().__init__()
        self.color = "black"
        self.backcolor = "grey"
        self.color_active = "white"
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.key_return = False
        self.text = ""
        self.render_text()

    def render_text(self):
        """Renders the textbox, displays wether active, draws written text.
        """
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        self.image.fill(self.backcolor)

        if self.active: # Changes color when active.
            pygame.draw.rect(self.image, self.color_active, self.image.get_rect().inflate(-2, -2), 2)
        else:
            pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.image.blit(t_surf, (5, 5))    
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event):
        """Updates the textinputbox when somethin is written.

        Args:
            event_list (_type_): _description_
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.key_return = False
            self.active = self.rect.collidepoint(event.pos) # Detects when the user clicks on the input box.
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                self.key_return = True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        self.render_text()
            




    




