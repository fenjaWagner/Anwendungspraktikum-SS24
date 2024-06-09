# Decided to avoid resizing.
class resize_window:
    """Displays a resizable window.
    """
    def __init__(self, size, color, name: str) -> None:
        self.size = size
        self.color = color
        self.name = name
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption(name)
        self.start_listening()
        

    def start_listening(self):
        running = True
        while running:
        # event handling, gets all event from the event queue
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                self.screen.blit(pygame.transform.scale( self.screen, event.dict['size']), (0, 0))
                pygame.display.update()
            elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
                self.screen.fill((0, 0, 0))
                self.screen.blit(pygame.transform.scale(self.screen,  self.screen.get_size()), (0, 0))
                pygame.display.update()
            self.screen.fill(self.color)
            pygame.display.update()
