import pygame
import json


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
        if self.active:
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
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                self.key_return = True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        self.render_text()
            


class Write_Data_Manager():
    """Handles new users.
    """
        # TODO: Handling doppelter Nutzername!
    def __init__(self) -> None:
        self.user = None
        self.data = self.read_data()
        self.user_data = None

    def read_data(self):
        """Reads data from file.

        Returns:
            dict: data from all users
        """
        with open('user_data.txt', 'r') as user_data_file:
            dict = json.loads(user_data_file.read())
        
        return dict
    
    def write_data(self):
        """Writes new user to datafile.
        """
        self.data[self.user] = self.user_data
        with open('user_data.txt', 'w') as user_data_file:
            user_data_file.write(json.dumps(self.data))

    




