import pygame

class Image_Loader:
    def __init__(self, engine, background) -> None:
        self.engine = engine
        self.background = background
        self.image_size = ((self.engine.size_y //3) * 0.818181, self.engine.size_y //3)
        self.load_image()
    
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

    def draw_image(self, surface):
        surface.fill(self.background)
        surface.blit(self.img1, ((self.engine.size_x-(4*self.image_size[0]))//5, 50))
        surface.blit(self.img2, ((self.engine.size_x-(4*self.image_size[0]))*2//5 + self.image_size[0], 50))
        surface.blit(self.img3, ((self.engine.size_x-(4*self.image_size[0]))*3//5 + 2*self.image_size[0], 50))
        surface.blit(self.img4, ((self.engine.size_x-(4*self.image_size[0])) * 4//5 + 3*self.image_size[0], 50))
        surface.blit(self.img5, ((self.engine.size_x - self.image_size[0]) //2 , (self.engine.size_y // 3)*1.5))

    def get_image(self):
        return self.img1, self.img2, self.img3, self.img4, self.img5