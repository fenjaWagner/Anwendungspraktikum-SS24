import pygame
import input_management.text_input_box as in_box
import Image_Management.image_logic as im

class State:
    """Interface for the states.
    """
    def __init__(self, engine):
        self.engine = engine

    def on_draw(self, surface) -> None: pass
    def on_event(self, event) -> None: pass
    def on_update(self): pass#, delta) -> None: pass

class StartState(State):
    """State that manages the Login.

    Args:
        State (_type_): inherits from State
    """
    def __init__(self, engine, background): 
        """_summary_

        Args:
            engine (_type_): _description_
            background (_type_): _description_
        """
        super().__init__(engine)
        self.engine = engine
        self.background = background
        self.user_text = self.engine.font.render("Username:", False, 0, self.background)
        self.new_user_text = self.engine.font.render("Sign up:", False, 0, self.background)   
        self.group = pygame.sprite.Group()
        
        # User Input Boxes
        self.user_input = in_box.TextInputBox(20, self.engine.size_y * 5 //15, self.engine.size_x -40, self.engine.font)
        self.group.add(self.user_input)
        self.new_user_input = in_box.TextInputBox(20, self.engine.size_y *11 //15, self.engine.size_x -40, self.engine.font)
        self.group.add(self.new_user_input)


    def user_handling(self):
        #print("user handling")
        if not self.new_user_input.active and self.new_user_input.text:
            print("register")
            self.engine.data_manager.sign_up(self.new_user_input.text, new_user_flag = 1)
            self.user_input.text = ''


        elif not self.user_input.active and self.user_input.text:
            #self.user, self.data = in_box.Login_Manager(self.user_input.text, 0).sign_up()
            print("sign in")
            self.engine.data_manager.sign_up(self.user_input.text, new_user_flag = 0)
            self.user_input.text = ''

                
        else:
            pass


    def update(self, screen):
        #print("update")
        screen.fill(self.background)
        self.group.draw(screen)
        screen.blit(self.user_text, (20, self.engine.size_y*3 // 15))
        screen.blit(self.new_user_text, (20, self.engine.size_y *9// 15))
        #pygame.display.flip()
        #pygame.display.update()

    def on_draw(self, surface):
        #print("draw")
        surface.fill(self.background)
        self.update(surface)

    def on_event(self, event):
        #print("on_event")
        self.group.update(event)
        self.user_handling()








class UserModeState(State):
    def __init__(self, engine, background):
        super().__init__(engine)
        self.engine = engine
        self.background = background
        self.image_size = ((self.engine.size_y //3) * 0.818181, self.engine.size_y //3)
        self.group = pygame.sprite.Group()
        self.image_loader = im.Image_Loader(self.engine)
        self.get_images()

    def get_images(self):
        self.img1, self.img2, self.img3, self.img4, self.img5 = self.image_loader.get_image()
        self.img1 =  pygame.transform.scale(self.img1, self.image_size)
        self.img2 =  pygame.transform.scale(self.img2, self.image_size)
        self.img3 =  pygame.transform.scale(self.img3, self.image_size)
        self.img4 =  pygame.transform.scale(self.img4, self.image_size)
        self.img5 =  pygame.transform.scale(self.img5, self.image_size)
        
    def on_draw(self, surface):
        surface.fill(self.background)
        surface.blit(self.img1, ((self.engine.size_x-(4*self.image_size[0]))//5, 50))
        surface.blit(self.img2, ((self.engine.size_x-(4*self.image_size[0]))*2//5 + self.image_size[0], 50))
        surface.blit(self.img3, ((self.engine.size_x-(4*self.image_size[0]))*3//5 + 2*self.image_size[0], 50))
        surface.blit(self.img4, ((self.engine.size_x-(4*self.image_size[0])) * 4//5 + 3*self.image_size[0], 50))
        surface.blit(self.img5, ((self.engine.size_x - self.image_size[0]) //2 , (self.engine.size_y // 3)*1.5))

        self.group.draw(surface)

    def on_event(self, event):
        self.group.update(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = StartState(self.engine, (140,140,140))



class LogInError(State):
    def __init__(self, engine, background):
        super().__init__(engine)
        self.background = background
        self.engine = engine
        self.error_font = pygame.font.SysFont(None, 60)
        self.error = self.error_font.render("Error:", False, ('darkred'), self.background)
        self.subtext = self.engine.font.render("Wrong Username. Press Space to return to Login.", False, 0, self.background)
        

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = StartState(self.engine, (140,140,140))

    def update(self, screen):
        screen.fill(self.background)
        screen.blit(self.error, (20, self.engine.size_y*5 // 15))
        screen.blit(self.subtext, (20, self.engine.size_y *9// 15))


    def on_draw(self, surface):
        #print("draw")
        surface.fill(self.background)
        self.update(surface)

class ChosenUsernameError(State):
    def __init__(self, engine, background):
        super().__init__(engine)
        self.background = background
        self.engine = engine
        self.error_font = pygame.font.SysFont(None, 60)
        self.error = self.error_font.render("Error:", False, ('darkred'), self.background)
        self.subtext = self.engine.font.render("Please choose another username. Press Space to return to Login.", False, 0, self.background)
        

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = StartState(self.engine, (140,140,140))

    def update(self, screen):
        screen.fill(self.background)
        screen.blit(self.error, (20, self.engine.size_y*5 // 15))
        screen.blit(self.subtext, (20, self.engine.size_y *9// 15))


    def on_draw(self, surface):
        #print("draw")
        surface.fill(self.background)
        self.update(surface)

