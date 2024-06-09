# import the pygame module, so you can use it
import pygame
import input_management.text_input_box as geo
import start as start
#https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame

#interesting for group stuff
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    group = pygame.sprite.Group()
    screen = start.start_window(700,700, (140,140,140), group)
    font = pygame.font.SysFont(None, 25)
    text_input_box = geo.TextInputBox(50, 50, 400, font)
    #inputRect = geo.InputRect(screen.size[0]//4, screen.size[1]//4, (screen.size[0]//2, screen.size[1]//2), (120,120,120), 0, "LOGIN", screen.size[1]//20)
    screen.group.add(text_input_box)
    screen.run()

    
    
     
     
    # define a variable to control the main loop
    
     
    # main loop
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()





    