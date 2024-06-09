import pygame
import input_management.text_input_box as geo
import Image_Management.image_logic as image

class User_Screen:
    def __init__(self, size_x, size_y, color, font) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.screen = pygame.display.set_mode((self.size_x, self.size_y))
        self.font = font  
        self.image_size = (250, 360) 
        self.group = pygame.sprite.Group()
        self.image_loader = image.Image_Loader()
        self.get_images()


        self.running = True
        pygame.display.set_caption("Funny Game")

    def get_images(self):
        self.img1, self.img2, self.img3, self.img4, self.img5 = self.image_loader.get_image()
        self.img1 =  pygame.transform.scale(self.img1, self.image_size)
        self.img2 =  pygame.transform.scale(self.img2, self.image_size)
        self.img3 =  pygame.transform.scale(self.img3, self.image_size)
        self.img4 =  pygame.transform.scale(self.img4, self.image_size)
        self.img5 =  pygame.transform.scale(self.img5, self.image_size)

    def update(self):
        self.screen.fill(self.color)
        self.screen.blit(self.img1, ((self.size_x-(4*self.image_size[0]))//5, 50))
        self.screen.blit(self.img2, ((self.size_x-(4*self.image_size[0]))*2//5 + self.image_size[0], 50))
        self.screen.blit(self.img3, ((self.size_x-(4*self.image_size[0]))*3//5 + 2*self.image_size[0], 50))
        self.screen.blit(self.img4, ((self.size_x-(4*self.image_size[0])) * 4//5 + 3*self.image_size[0], 50))
        self.screen.blit(self.img5, ((self.size_x - self.image_size[0]) //2 , 490))

        self.group.draw(self.screen)
        pygame.display.flip()
        pygame.display.update()

    
    def listening(self):   
        event_list = pygame.event.get() 
        self.group.update(event_list)
            
    
    def end_Login_Window(self):
        self.running = False
                

    def run(self):
        while self.running:
            self.listening()
            self.update()

class User:
    def __init__(self, user, data, font) -> None:
        self.user = user
        self.data = data
        self.font = font
        self.screen = User_Screen(1200,900, (140,140,140), font)
    
    def run(self):
        self.screen.run()

