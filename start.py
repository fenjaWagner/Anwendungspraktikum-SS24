import pygame
import input_management.text_input_box as geo
import user as us
import sys
from pygamepopup.menu_manager import MenuManager
from pygamepopup.components import TextElement, InfoBox


class Login_Window(pygame.sprite.Sprite):
    """Login Window

    Args:
        pygame (_type_): _description_
    """
    def __init__(self, size_x, size_y, color, font) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.screen = pygame.display.set_mode((self.size_x, self.size_y))
        self.menu_manager = MenuManager(self.screen)
        self.font = font
        self.user_text = self.font.render("Username:", False, 0, self.color)
        self.new_user_text = self.font.render("Sign up:", False, 0, self.color)   
        self.group = pygame.sprite.Group()
        
        # User Input Boxes
        self.user_input = geo.TextInputBox(20, self.size_y * 5 //15, self.size_x -40, self.font)
        self.group.add(self.user_input)
        self.new_user_input = geo.TextInputBox(20, self.size_y *11 //15, self.size_x -40, self.font)
        self.group.add(self.new_user_input)

        self.mode = "login"


        self.running = True
        pygame.display.set_caption("Funny Game")
        
    def update(self):
        self.screen.fill(self.color)
        self.group.draw(self.screen)
        self.screen.blit(self.user_text, (20, self.size_y*3 // 15))
        self.screen.blit(self.new_user_text, (20, self.size_y *9// 15))
        pygame.display.flip()
        pygame.display.update()

    def user_handling(self):
        if not self.new_user_input.active and self.new_user_input.text:
            self.user, self.data = geo.Login_Manager(self.new_user_input.text, 1).sign_up()
            geo.Write_Data_Manager(self.user, self.data).write_data()
            self.mode = "user"
            print(self.mode)
        elif not self.user_input.active and self.user_input.text:
            self.user, self.data = geo.Login_Manager(self.user_input.text, 0).sign_up()
            if self.user == 'Error':
                self.user_input.text = ''
                print("Error")
                #my_custom_menu = InfoBox("Exception",[[TextElement(text = "Wrong username.Try again.")]], width=400,title_color=pygame.Color("red"), close_button_text="ok!")
                #self.menu_manager.open_menu(my_custom_menu)
            else:
                self.user_input.text = ''
                self.mode = "user"
                print(self.mode)
                
        else:
            pass

    def listening(self):   
        event_list = pygame.event.get() 
        self.group.update(event_list)
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                quit()
                sys.exit()
            #elif event.type == pygame.VIDEORESIZE:
            #    self.screen.blit(pygame.transform.scale( self.screen, event.dict['size']), (0, 0))
                
            #elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
            #    self.screen.fill((0, 0, 0))
            #    self.screen.blit(pygame.transform.scale(self.screen,  self.screen.get_size()), (0, 0))
    
                

    def run(self):
        while self.running:
            self.listening()
            self.user_handling()
            self.update()

                    


class Exception_Window(pygame.sprite.Sprite):
    def __init__(self, text) -> None:
        self.screen = pygame.display.set_mode((200,400))
        self.font = pygame.font.SysFont(None, 60)
        self.text = self.font.render(text, False, 'red', 'white')   
        self.running = True
        pygame.display.set_caption("Exception")
        
    def update(self):
        self.screen.fill('white')
        self.screen.blit(self.text, (20, self.size_y//2))
        pygame.display.flip()
        pygame.display.update()


    def listening(self):   
        event_list = pygame.event.get() 
        self.group.update(event_list)
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False  
    

    def run(self):
        while self.running:
            self.listening()
            self.update()

                    




