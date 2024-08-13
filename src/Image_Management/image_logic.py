import pygame
import json
import numpy as np


class ImageDrawer:
    """Loads the images given by the Image Manager, scales and displays them and manages the user input.
    """
    def __init__(self, engine, background) -> None:
        """Inizializes the Image Loader.

        Args:
            engine (Displayengine): Engine that holds the configuration, image config, and user data.
            background (tuple): Background color (R, G, B)
        """
        self.engine = engine
        self.background = background
        self.image_loader = ImageLoader(self.engine)
        self.order = self.engine.config["order"]

        self.get_comp_image_size()
        self.image_loader.load_images()
        self.load_image()
        
    def get_comp_image_size(self):
        """Calculates and sets the size for comparison and experimental images."""
        size_dict = {"exp_proc": [self.engine.layout_config["original_image_size"],
                                 self.engine.layout_config["processed_image_size"]],
                    "exp_unproc": [self.engine.layout_config["processed_image_size"],
                                 self.engine.layout_config["original_image_size"]]}
        comp_size = size_dict[self.order][0]
        exp_size = size_dict[self.order][1]

        width_factor = (6 / 24) * self.engine.size_x # scaling factor
        height_factor = (6 / 16) * self.engine.size_y # scaling factor

        # Scaling depends on the width-height ratio, so the images fit to the screen and
        # are scaled with the same factor.
        if (width_factor / height_factor) <= comp_size[0]/ comp_size[1]:
            factor = width_factor / comp_size[0]
            self.comp_pic_size = (int(width_factor), int(comp_size[1] * factor))
            self.exp_pic_size = (int(exp_size[0] * factor), int(exp_size[1] * factor))
        else: 
            factor = height_factor /comp_size[1]
            self.comp_pic_size = (int(comp_size[0] * factor),int(height_factor))
            self.exp_pic_size = (int(exp_size[0] * factor), int(exp_size[1] * factor))

    def load_image(self):
        """Loads and scales the images from the image loader.
        """ 
        self.current_images = [pygame.transform.scale(img, self.comp_pic_size) for img in self.image_loader.current_images]
        self.proc_head = pygame.transform.scale(self.image_loader.proc_head, self.exp_pic_size)

        # Store rects for mouse collision detection
        self.image_rects = [img.get_rect() for img in self.current_images]
        

    def draw_image(self, surface):
        """Displays the images on the given surface.

        Args:
            surface (pygame.Surface): Surface on which the images should be displayed.
        """
        surface.fill(self.background)

        x_spacing = (self.engine.size_x - 4 * self.comp_pic_size[0]) // 5 # space between images

        # Calculate position for each image in the current image list.
        for i, img in enumerate(self.current_images):
            x_position = x_spacing * (i + 1) + self.comp_pic_size[0] * i
            y_position = (self.engine.size_y // 2 - self.comp_pic_size[1]) // 2
            surface.blit(img, (x_position, y_position))
            self.image_rects[i].topleft = (x_position, y_position)

        # Calculate position for the picture of the person that is to be found.
        exp_x_position = (self.engine.size_x - self.exp_pic_size[0]) // 2
        exp_y_position = self.engine.size_y // 2 + (self.engine.size_y // 2 - self.exp_pic_size[1]) // 2
        surface.blit(self.proc_head, (exp_x_position, exp_y_position))
        
    def get_image(self):
        """Returns the loaded images for testing or further processing."""
        return self.current_images + [self.proc_head]
    
    def on_event(self, event):
        """Handles the given event and invokes result management in the image manager.

        Args:
            event (pygame.event): The event to handle
        """
        if event.type == pygame.KEYDOWN:
            key_to_index = {
                pygame.K_1: 1,
                pygame.K_2: 2,
                pygame.K_3: 3,
                pygame.K_4: 4
            }
            if event.key in key_to_index:  # processes key instructions
                self.image_loader.verify_and_renew(key_to_index[event.key])
                self.load_image()

        elif event.type == pygame.MOUSEBUTTONDOWN: # processes clicking on the images
            for i, rect in enumerate(self.image_rects, start=1):
                if rect.collidepoint(event.pos):
                    self.image_loader.verify_and_renew(i)
                    self.load_image()
                    break
       

class ImageLoader:
    """Class that chooses the images depending on the given game modes and saves the user resulsts.
    """
    def __init__(self, engine):
        """Inizialization of the Image Manager.

        Args:
            engine (Display engine): Engine that holds the configuration, image config, and user data.
        """
        self.engine = engine

        self.get_config_settings() # read in the config settings
        self.get_detail_mode() # randomly choose first detail mode
        self.get_game_mode() # randomly choose first game mode
        
        self.get_image_settings() # read in the image item lists from the config
        
        self.id = None
        self.comp_pic_place = None
        self.current_images = []
        self.user_data = self.engine.data_manager.user_data
    
    def get_config_settings(self):
        """Retrieves configuration settings from the engine's configuration.
        """
        self.order = self.engine.config["order"]
        self.detail_modes = self.engine.config["detail_modes"]
        self.game_modes = self.engine.config["game_modes"]

        # The dict that contains a list of the images for each game mode
        self.item_dict = self.get_image_item_dict() 
        self.image_config = self.engine.image_config

    def get_image_settings(self):
        """Retrieves and sets the image settings based on the current game mode.
        """
        self.exp_list = self.item_dict[self.image_config["game_modes"][self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config["game_modes"][self.mode]['comp_pic_list']]
        self.identity = self.item_dict['identity_pic']

    def get_detail_mode(self):
        """Randomly selects and sets the current detail mode.

        """
        np.random.seed()
        detail_mode_num = np.random.randint(len(self.detail_modes))
        self.detail_mode = self.detail_modes[detail_mode_num]

    def get_game_mode(self):
        """ Randomly selects and sets the current game mode.
        """
        np.random.seed()
        mode_index = np.random.randint(len(self.game_modes))
        self.mode = self.game_modes[mode_index]
    
    def get_img_path(self):
        """Retrieves and sets the paths for the experimental and comparison images.
        """
        self.img_path_exp = self.image_config[self.order][self.detail_mode]["exp_heads_path"]
        self.img_path_comp = self.image_config[self.order][self.detail_mode]["comp_heads_path"]

    def get_image_item_dict(self):
        """Reads the image item dictionary from a file.

        Returns:
            dict: Dictionary containing image items.
        """
        with open("image_item.txt", "r") as file:
            dict = json.loads(file.read())
        return dict
    
    def get_compare_images(self):
        """Loads the comparison images based on the current identity.
        """

        pic_num = np.random.randint(2)
        proc_num = self.identity[self.id][pic_num]
        self.proc_head = pygame.image.load(self.img_path_exp + proc_num+".jpg").convert()

        pic_num = (pic_num -1)%2
        comp_num = self.identity[self.id][pic_num]
        self.comp_pic = pygame.image.load(self.img_path_comp + comp_num+".jpg").convert()

    def get_random_image_list(self, li):
        """Generates a list of random images excluding the current identity.

        Args:
            li (list): List of image identifiers.
        """
        self.current_images = []
        length = len(li)
        indices = set()

        while len(indices) < 3:
            idx = np.random.randint(length)
            if li[idx] != self.id:
                indices.add(idx)

        pic_num = np.random.randint(2)
        test_list = [self.identity[li[idx]][pic_num] for idx in indices]

        self.current_images = [
            pygame.image.load(f"{self.img_path_comp}{img}.jpg").convert()
            for img in test_list
        ]
    
    def update_image_lists(self):
        """Updates experimental and comparison image lists based on the current mode.
        """
        self.exp_list = self.item_dict[self.image_config["game_modes"][self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config["game_modes"][self.mode]['comp_pic_list']]

    def place_com_img(self):
        """Places the comparison image randomly among the current images.
        """
        self.comp_pic_place = np.random.randint(4)
        self.current_images.insert(self.comp_pic_place, self.comp_pic)    
    
    def load_images(self):
        """Loads a new set of images for comparison.
        """
        np.random.seed()
        self.get_game_mode()
        self.get_detail_mode()
        self.get_img_path()

        self.update_image_lists()
        id_index = np.random.randint(len(self.exp_list))
        self.id = self.exp_list[id_index]
        self.get_compare_images()
        self.get_random_image_list(self.comp_pic_list)
        self.place_com_img()
    
    def print_results(self, correct_detail, out_of_detail, correct_game_mode, out_of_game_mode):
        print("-"*45)
        print(f"Detail Mode: {self.detail_mode}")
        print(f"Mode: {self.mode}")
        print(f"Statistic: {correct_detail} out of {out_of_detail} in detail mode {self.detail_mode}")
        print(f"Statistic: {correct_game_mode} out of {out_of_game_mode} in game_mode mode {self.mode}")
        print("-"*45)
        
    def verify_and_renew(self, picked_img):
        """Verifies the user's choice and updates the image set.

        Args:
        picked_img (int): Index of the image picked by the user.
    """
        # Increment the counters for overall, detail mode, and game mode
        self.user_data[self.order]['overall']['out_of'] += 1
        self.user_data[self.order][self.detail_mode]['overall']['out_of'] += 1
        self.user_data[self.order][self.detail_mode][self.mode]['out_of'] += 1
        
        # Retrieve updated counters
        out_of_overall = self.user_data[self.order]['overall']['out_of']
        out_of_detail = self.user_data[self.order][self.detail_mode]['overall']['out_of']
        out_of_game_mode = self.user_data[self.order][self.detail_mode][self.mode]['out_of']

        # Check if the user's choice is correct
        is_correct = (picked_img - 1) == self.comp_pic_place
        if is_correct:
            # Increment the correct counters if the choice was correct
            self.user_data[self.order]['overall']['correct'] += 1
            self.user_data[self.order][self.detail_mode]['overall']['correct'] += 1
            self.user_data[self.order][self.detail_mode][self.mode]['correct'] += 1

        # Retrieve updated correct counters
        correct_of_overall = self.user_data[self.order]['overall']['correct']
        correct_detail = self.user_data[self.order][self.detail_mode]['overall']['correct']
        correct_game_mode = self.user_data[self.order][self.detail_mode][self.mode]['correct']

        # Print results based on current counters
        self.print_results(correct_detail, out_of_detail, correct_game_mode, out_of_game_mode)

        # Load the next set of images
        self.load_images()