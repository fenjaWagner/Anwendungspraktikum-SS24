import pygame
import input_management.text_input_box as in_box
import Image_Management.image_logic as im
import evaluation.data_evaluation as eval
class State:
    """Interface for the states.
    """
    def __init__(self, engine):
        self.engine = engine

    def on_draw(self, surface) -> None: pass
    def on_event(self, event) -> None: pass
    def on_update(self): pass

class StartState(State):
    """State that manages the Login.
    """
    def __init__(self, engine): 
        """Initializes the StartState.

        Args:
            engine (Display engine): Engine that holds the configuration, image config, and user data.
            background (tuple): Background color (R, G, B).
        """
        super().__init__(engine)
        self.engine = engine
        self.background = self.engine.layout_config["background_color"]
        self.init_texts()
        self.init_input_boxes()

    def init_texts(self):
        """Initializes the static text objects."""
        self.user_text = self.engine.font.render("Username:", False, 0, self.background)
        self.new_user_text = self.engine.font.render("Sign up:", False, 0, self.background)

    def init_input_boxes(self):
        """Initializes input boxes."""
        self.group = pygame.sprite.Group()
        self.user_input = in_box.TextInputBox(20, self.engine.size_y * 5 // 15, self.engine.size_x - 40, self.engine.font)
        self.new_user_input = in_box.TextInputBox(20, self.engine.size_y * 11 // 15, self.engine.size_x - 40, self.engine.font)
        self.group.add(self.user_input, self.new_user_input)
        

    def handle_user_input(self):
        """Handles user input for login or sign-up.
        """
        if self.new_user_input.key_return and self.new_user_input.text:
            self.engine.data_manager.sign_up(self.new_user_input.text, new_user_flag = 1)
            self.user_input.text = ''


        elif self.user_input.key_return and self.user_input.text:
            self.engine.data_manager.sign_up(self.user_input.text, new_user_flag = 0)
            self.user_input.text = ''

  
    def on_draw(self, surface):
        """Draws the current objects on the given surface.

        Args:
           surface (pygame.Surface): Surface on which the images should be displayed.
        """
        surface.fill(self.background)
        self.group.draw(surface)
        surface.blit(self.user_text, (20, self.engine.size_y*3 // 15))
        surface.blit(self.new_user_text, (20, self.engine.size_y *9// 15))

    def on_event(self, event):
        """Passes the given event to the group of sprites and invokes user handling.

        Args:
            event (pygame.event): _description_
        """
        self.group.update(event)
        self.handle_user_input()



class UserModeState(State):
    """State that holds the image loader and manages the result data of a certain user.

    Args:
        State (_type_): Inherits from State
    """
    def __init__(self, engine):
        """Inizializes the UserState.

        Args:
            engine (Display engine): Engine that holds the configuration, image config, and user data.
            background (tuple): Background color (R, G, B)
        """
        super().__init__(engine)
        self.engine = engine
        self.background = self.engine.layout_config["background_color"]
        self.group = pygame.sprite.Group()
        self.image_loader = im.Image_Loader(self.engine, self.background)
        self.eval = eval.DataEvaluation(self.engine)
        
    def on_draw(self, surface):
        """Draws the images on the given surface.

        Args:
           surface (pygame.Surface): Surface on which the images should be displayed.
        """
        self.image_loader.draw_image(surface)
        self.group.draw(surface)

    def on_event(self, event):
        """Passes the given event to the group of sprites and invokes user handling.

        Args:
            event (pygame.event): _description_
        """
        self.group.update(event)
        self.image_loader.on_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.engine.data_manager.write_data()
                self.eval.eval()
                self.engine.machine.next_state = StartState(self.engine)



class ErrorState(State):
    """Base class for error states that display messages."""

    def __init__(self, engine, error_message, sub_message):
        """Initializes the ErrorState.

        Args:
            engine (DisplayEngine): Engine that holds the configuration, image config, and user data.
            background (tuple): Background color (R, G, B)
            error_message (str): The main error message.
            sub_message (str): The subtext for the error.
        """
        super().__init__(engine)
        self.engine = engine
        self.background = self.engine.layout_config["background_color"]
        self.init_texts(error_message, sub_message)

    def init_texts(self, error_message, sub_message):
        """Initializes the error and subtext messages."""
        self.error_font = pygame.font.SysFont(None, 60)
        self.error = self.error_font.render(error_message, False, ('darkred'), self.background)
        self.subtext = self.engine.font.render(sub_message, False, 0, self.background)

    def on_draw(self, surface):
        """Draws the error messages on the surface."""
        surface.fill(self.background)
        surface.blit(self.error, (20, self.engine.size_y * 5 // 15))
        surface.blit(self.subtext, (20, self.engine.size_y * 9 // 15))

    def on_event(self, event):
        """Handles the given event and returns the engine to the StartState."""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.engine.machine.next_state = StartState(self.engine)

class LogInErrorState2(ErrorState):
    """State that displays the log-in error screen."""
    def __init__(self, engine):
        """Initializes the LogInErrorState."""
        super().__init__(
            engine,
            "Error:",
            "Wrong Username. Press Space to return to Login."
        )

class ChosenUsernameErrorState2(ErrorState):
    """State that displays that the username is already taken."""
    def __init__(self, engine):
        """Initializes the ChosenUsernameErrorState."""
        super().__init__(
            engine,
            "Error:",
            "This username is already used. Press Space to return to Login."
        )
