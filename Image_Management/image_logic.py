import pygame

class Image_Loader:
    def __init__(self, engine) -> None:
        self.engine = engine
        self.load_image()
    
    def load_image(self):
        self.image_1 = pygame.image.load("example1.jpg").convert()
        self.image_2 = pygame.image.load("example2.jpg").convert()
        self.image_3 = pygame.image.load("example3.jpg").convert()
        self.image_4 = pygame.image.load("example4.jpg").convert()
        self.image_5 = pygame.image.load("example5.jpg").convert()

    def get_image(self):
        return self.image_1, self.image_2, self.image_3, self.image_4, self.image_5