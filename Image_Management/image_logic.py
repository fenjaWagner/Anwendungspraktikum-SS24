import pygame
import json
import numpy as np


class Image_Loader:
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
        self.image_manager = Image_Manager(self.engine)
        self.detail_mode = self.engine.config["detail_mode"]
        self.comp_mode = self.engine.config["order"]

        self.get_comp_image_size()
        self.image_manager.load_images()
        self.load_image()
        
    def get_comp_image_size(self):
        """Calculates and sets the size for comparison and experimental images."""
        size_dict = {"exp_proc": [self.engine.layout_config["original_image_size"],
                                 self.engine.layout_config["processed_image_size"]],
                    "exp_unproc": [self.engine.layout_config["processed_image_size"],
                                 self.engine.layout_config["original_image_size"]]}
        comp_size = size_dict[self.comp_mode][0]
        exp_size = size_dict[self.comp_mode][1]
                
        width_factor = (6 / 24) * self.engine.size_x
        height_factor = (6 / 16) * self.engine.size_y

        if (width_factor / height_factor) <= comp_size[0]/ comp_size[1]:
            factor = width_factor / comp_size[0]
            self.comp_pic_size = (int(width_factor), int(comp_size[1] * factor))
            self.exp_pic_size = (int(exp_size[0] * factor), int(exp_size[1] * factor))
        else: 
            factor = height_factor /comp_size[1]
            self.comp_pic_size = (int(comp_size[0] * factor),int(height_factor))
            self.exp_pic_size = (int(exp_size[0] * factor), int(exp_size[1] * factor))

    def load_image(self):
        """Loads and scales the images from the image manager.
        """ 

        self.current_images = [pygame.transform.scale(img, self.comp_pic_size) for img in self.image_manager.current_images]
        self.proc_head = pygame.transform.scale(self.image_manager.proc_head, self.exp_pic_size)

        # Store rects for mouse collision detection
        self.image_rects = [img.get_rect() for img in self.current_images]
        

    def draw_image(self, surface):
        """Displays the images on the given surface.

        Args:
            surface (pygame.Surface): Surface on which the images should be displayed.
        """
        surface.fill(self.background)

        x_spacing = (self.engine.size_x - 4 * self.comp_pic_size[0]) // 5
        for i, img in enumerate(self.current_images):
            x_position = x_spacing * (i + 1) + self.comp_pic_size[0] * i
            y_position = (self.engine.size_y // 2 - self.comp_pic_size[1]) // 2
            surface.blit(img, (x_position, y_position))
            self.image_rects[i].topleft = (x_position, y_position)

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
            if event.key in key_to_index:
                print(key_to_index[event.key])
                self.image_manager.verify_and_renew(key_to_index[event.key])
                self.load_image()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.image_rects, start=1):
                if rect.collidepoint(event.pos):
                    print(i)
                    self.image_manager.verify_and_renew(i)
                    self.load_image()
                    break
       

class Image_Manager:
    """Class that chooses the images depending on the given game modes and saves the user resulsts.
    """
    def __init__(self, engine):
        """Inizialization of the Image Manager.

        Args:
            engine (Display engine): Engine that holds the configuration, image config, and user data.
        """
        self.engine = engine
        self.detail_mode = self.engine.config["detail_mode"]
        self.game_modes = self.engine.config["game_modes"]
        self.comp_mode = self.engine.config["order"]
        self.mode = None

        self.item_dict = self.get_image_item_dict()
        self.image_config = self.engine.image_config
        self.mode = "mixed"
        self.exp_list = self.item_dict[self.image_config[self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config[self.mode]['comp_pic_list']]
        self.identity = self.item_dict['identity_pic']

        self.img_path_exp = self.engine.image_config[self.comp_mode][self.detail_mode]["exp_heads_path"]
        self.img_path_comp = self.engine.image_config[self.comp_mode][self.detail_mode]["comp_heads_path"]

        self.id = None
        self.comp_pic_place = None
        self.current_images = []

        self.user_data = self.engine.data_manager.user_data


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

        print("TestList:", test_list)
    
    def update_image_lists(self):
        """Updates experimental and comparison image lists based on the current mode.
        """
        self.exp_list = self.item_dict[self.image_config[self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config[self.mode]['comp_pic_list']]

    def place_com_img(self):
        """Places the comparison image randomly among the current images.
        """
        self.comp_pic_place = np.random.randint(4)
        print("place:", self.comp_pic_place +1)
        self.current_images.insert(self.comp_pic_place, self.comp_pic)    
    
    def load_images(self):
        """Loads a new set of images for comparison.
        """
        np.random.seed()
        mode_index = np.random.randint(len(self.game_modes))
        self.mode = self.game_modes[mode_index]
        print(self.mode)

        self.update_image_lists()
        id_index = np.random.randint(len(self.exp_list))
        self.id = self.exp_list[id_index]
        self.get_compare_images()
        self.get_random_image_list(self.comp_pic_list)
        self.place_com_img()
        
    def verify_and_renew(self, picked_img):
        """Verifies the user's choice and updates the image set.

        Args:
            picked_img (int): Index of the image picked by the user.
        """
        if picked_img -1 == self.comp_pic_place:
            print("right choice")
            self.user_data['detail_mode'][self.detail_mode]['correct'] += 1
            self.user_data['game_modes'][self.mode]['correct'] +=1
        else:
            print("wrong choice")
        
        self.user_data['detail_mode'][self.detail_mode]['out_of'] += 1
        self.user_data['game_modes'][self.mode]['out_of'] +=1

        self.load_images()

