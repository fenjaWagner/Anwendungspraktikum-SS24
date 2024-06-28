import pygame
import json
import numpy as np

class Image_Loader:
    def __init__(self, engine, background, user) -> None:
        self.engine = engine
        self.background = background
        self.image_size = ((self.engine.size_y //3) * 0.818181, self.engine.size_y //3)
        self.user = user
        self.load_image()
        self.image_manager = Image_Manager(self.engine, self.user)
    
    def load_image(self):
        self.img1 = pygame.image.load("example1.jpg").convert()
        self.img2 = pygame.image.load("example2.jpg").convert()
        self.img3 = pygame.image.load("example3.jpg").convert()
        self.img4 = pygame.image.load("example4.jpg").convert()
        self.img5 = pygame.image.load("example5.jpg").convert()
        self.img1 =  pygame.transform.scale(self.img1, self.image_size)
        self.img2 =  pygame.transform.scale(self.img2, self.image_size)
        self.img3 =  pygame.transform.scale(self.img3, self.image_size)
        self.img4 =  pygame.transform.scale(self.img4, self.image_size)
        self.img5 =  pygame.transform.scale(self.img5, self.image_size)
        self.rect1 = self.img1.get_rect()
        self.rect2 = self.img2.get_rect()
        self.rect3 = self.img3.get_rect()
        self.rect4 = self.img4.get_rect()
        

    def draw_image(self, surface):
        surface.fill(self.background)
        surface.blit(self.img1, ((self.engine.size_x-(4*self.image_size[0]))//5, 50))
        surface.blit(self.img2, ((self.engine.size_x-(4*self.image_size[0]))*2//5 + self.image_size[0], 50))
        surface.blit(self.img3, ((self.engine.size_x-(4*self.image_size[0]))*3//5 + 2*self.image_size[0], 50))
        surface.blit(self.img4, ((self.engine.size_x-(4*self.image_size[0])) * 4//5 + 3*self.image_size[0], 50))
        surface.blit(self.img5, ((self.engine.size_x - self.image_size[0]) //2 , (self.engine.size_y // 3)*1.5))

    def get_image(self):
        return self.img1, self.img2, self.img3, self.img4, self.img5
    
    def on_event(self, event):
             
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if self.rect1.collidepoint(event.pos):
                pass
            elif self.rect2.collidepoint(event.pos):
                pass
            elif self.rect3.collidepoint(event.pos):
                pass
            elif self.rect4.collidepoint(event.pos):
                pass


class Image_Manager:
    def __init__(self, engine):
        self.engine = engine
        self.detail_mode = self.engine.config["detail_mode"]
        self.game_modes = self.engine.config["game_modes"]
        self.item_dict = self.get_image_item_dict()
        """self.male = self.dict["gender"]["male"]
        self.female = self.dict["gender"]["female"]
        self.poc = self.dict["ethnicy"]["poc"]
        self.white = self.dict["ethnicy"]["white"]
        self.identity = self.dict["identity"]"""

        self.current_images = []


    def get_image_item_dict(self):
        with open("image_item.txt", "r") as file:
            dict = json.loads(file.read())
        return dict
    
    def load_images(self):
        np.random.seed()
        mode_index = np.random.randint(0, len(self.game_modes))
        mode = self.game_modes[mode_index]

        if mode == "mixed":
            
            



"poc_only"
"white_only"
"poc_between_whites"
"white_between_poc"
"female_only"
"male_only"
"female_between_males"
"male_between_female"


