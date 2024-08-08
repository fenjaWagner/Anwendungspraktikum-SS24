import pygame
import data_manager as dm
import conf

class Machine:
    """Holds the current state of the screen.
    """
    def __init__(self):
        self.current = None
        self.next_state = None

    def update(self):
        """Changes the state, if a new state is set.
        """
        if self.next_state:
            self.current = self.next_state
            self.next_state = None

class DisplayEngine:
    """Holds the screen and updates it depending on the state of the machine.
    """
    def __init__(self, flags=0):
        """DisplayEngine Init

        Args:
            caption (str): Name of the display
            fps (_type_): frames per second
            size_x (_type_): width of the screen
            size_y (_type_): hight of the screen
            font (_type_): used font
            flags (int, optional): _description_. Defaults to 0.
        """
        
        self.read_configs()
        self.set_layout()
        self.running = True
        self.data_manager = dm.Data_Manager(self)
        self.machine = Machine()

    def read_configs(self):
        self.config = conf.conf
        self.layout_config = conf.conf["layout"]
        self.image_config = conf.image_conf


    def set_layout(self):
        self.caption = self.layout_config["caption"]
        pygame.display.set_caption(self.caption)
        self.size_x = self.layout_config["screen_size"][0]
        self.size_y = self.layout_config["screen_size"][1]
        self.font = self.layout_config["font"]
        self.surface = pygame.display.set_mode((self.size_x, self.size_y), flags)
        self.rect = self.surface.get_rect()
        

    def loop(self):
        """Updates the screen.
        """
        while self.running:
            self.machine.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data_manager.write_data()
                    self.running = False

                else:
                    self.machine.current.on_event(event)

            self.machine.current.on_draw(self.surface)
            self.machine.current.on_update()
            pygame.display.flip()
            
    def run(self, state):
        """Starts the first state of the machine.

        Args:
            state (State): start state
        """
        self.machine.current = state
        self.loop()

