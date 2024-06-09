import pygame
import data_manager as dm

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
    def __init__(self, caption: str, fps, size_x, size_y, font, flags=0):
        """DisplayEngine Init

        Args:
            caption (str): Name of the display
            fps (_type_): frames per second
            size_x (_type_): width of the screen
            size_y (_type_): hight of the screen
            font (_type_): used font
            flags (int, optional): _description_. Defaults to 0.
        """
        pygame.display.set_caption(caption)
        self.size_x = size_x
        self.size_y = size_y
        self.font = font
        self.surface = pygame.display.set_mode((size_x, size_y), flags)
        self.rect = self.surface.get_rect()
        #self.clock = pygame.time.Clock()
        self.running = True
        #self.delta = 0
        #self.fps = fps
        self.data_manager = dm.Data_Manager(self)

        self.machine = Machine()

    def loop(self):
        """Updates the screen.
        """
        while self.running:
            self.machine.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.machine.current.on_event(event)

            self.machine.current.on_draw(self.surface)
            self.machine.current.on_update()#self.delta)

            pygame.display.flip()
            #self.delta = self.clock.tick(self.fps)

    def run(self, state):
        """Starts the first state of the machine.

        Args:
            state (State): start state
        """
        self.machine.current = state
        self.loop()

