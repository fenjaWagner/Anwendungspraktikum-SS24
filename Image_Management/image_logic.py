import pygame
import json
import numpy as np

class Image_Loader:
    def __init__(self, engine, background, user) -> None:
        self.engine = engine
        self.background = background
        self.image_size = ((self.engine.size_y //3) * 0.818181, self.engine.size_y //3)
        self.user = user
        self.image_manager = Image_Manager(self.engine, self.user)
        self.image_manager.load_images()    
        self.load_image()
        
    def load_image(self):
        
        self.img1 = self.image_manager.current_images[0]
        self.img2 = self.image_manager.current_images[1]
        self.img3 = self.image_manager.current_images[2]
        self.img4 = self.image_manager.current_images[3]
        self.img5 = self.image_manager.proc_head
        self.img1 =  pygame.transform.scale(self.img1, self.image_size)
        self.img2 =  pygame.transform.scale(self.img2, self.image_size)
        self.img3 =  pygame.transform.scale(self.img3, self.image_size)
        self.img4 =  pygame.transform.scale(self.img4, self.image_size)
        self.img5 =  pygame.transform.scale(self.img5, self.image_size)
        self.rect1 = self.img1.get_rect()
        self.rect2 = self.img2.get_rect()
        self.rect3 = self.img3.get_rect()
        self.rect4 = self.img4.get_rect()
        

    def draw_image(self, surface):
        surface.fill(self.background)
        surface.blit(self.img1, ((self.engine.size_x-(4*self.image_size[0]))//5, 50))
        surface.blit(self.img2, ((self.engine.size_x-(4*self.image_size[0]))*2//5 + self.image_size[0], 50))
        surface.blit(self.img3, ((self.engine.size_x-(4*self.image_size[0]))*3//5 + 2*self.image_size[0], 50))
        surface.blit(self.img4, ((self.engine.size_x-(4*self.image_size[0])) * 4//5 + 3*self.image_size[0], 50))
        surface.blit(self.img5, ((self.engine.size_x - self.image_size[0]) //2 , (self.engine.size_y // 3)*1.5))

    def get_image(self):
        return self.img1, self.img2, self.img3, self.img4, self.img5
    
    def on_event(self, event):
             
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if self.rect1.collidepoint(event.pos):
                self.image_manager.verify_and_renew(1)
                self.load_image()
            elif self.rect2.collidepoint(event.pos):
                self.image_manager.verify_and_renew(2)
                self.load_image()
            elif self.rect3.collidepoint(event.pos):
                self.image_manager.verify_and_renew(3)
                self.load_image()
            elif self.rect4.collidepoint(event.pos):
                self.image_manager.verify_and_renew(4)
                self.load_image()


class Image_Manager:
    def __init__(self, engine):
        self.engine = engine
        self.detail_mode = self.engine.config["detail_mode"]
        self.game_modes = self.engine.config["game_modes"]
        self.mode = None

        self.item_dict = self.get_image_item_dict()
        self.male = self.dict["gender"]["male"]
        self.female = self.dict["gender"]["female"]
        self.poc = self.dict["ethnicy"]["poc"]
        self.white = self.dict["ethnicy"]["white"]
        self.identity = self.dict["identity"]
        self.len_id = len(list(self.identity.keys()))

        self.img_path = "file_system/"+self.detail_mode+"/"

        self.id = None
        self.comp_pic_place = None
        self.current_images = []

        self.user_data = self.engine.data_manager.user_data


    def get_image_item_dict(self):
        with open("image_item.txt", "r") as file:
            dict = json.loads(file.read())
        return dict
    
    def get_compare_images(self):
        pic_num = np.random.randint(2)
        proc_num = self.identity[self.id][pic_num]
        self.proc_head = pygame.image.load(self.img_path + proc_num+".jpg").convert()

        pic_num = (pic_num -1)%2
        comp_num = self.identity[self.id][pic_num]
        self.comp_pic = pygame.image.load(self.img_path + comp_num+".jpg").convert()

    def get_random_image_list(self, list):
        np.random.seed()
        length = len(list)
        img_index_list= np.random.randint(length, size = 3)
        int_1 = img_index_list[0]
        int_2 = img_index_list[1]
        int_3 = img_index_list[2]

        while list[int_1] == self.id :
            int_1 = (int_1 + 1)%length

        while list[int_2] == self.id or int_2 == int_1:
            int_2 = (int_2 + 1)%length
        
        while list[int_3] == self.id or int_3 == int_1 or int_3 == int_2:
            int_3 = (int_3 + 1)%length

        pic_num = sum(list) % 2
        
        for i in [int_1, int_2, int_3]:
            img = pygame.image.load(self.img_path + self.identity[list[i]][pic_num]+".jpg").convert()
            self.current_images.append(img)

    def place_com_img(self):
        self.comp_pic_place = np.random.randint(4)
        self.current_images.insert(self.comp_pic_place, self.comp_pic)
            
    
    def load_images(self):
        np.random.seed()
        mode_index = 0
        self.mode = self.game_modes[mode_index]

        if self.mode == "mixed":
            id_index = np.random.randint(self.len_id)
            self.id = self.identity.keys()[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.identity.keys())
            self.place_com_img()

        elif self.mode == "poc_only":
            id_index = np.random.randint(len(self.poc))
            self.id = self.poc[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.poc)
            self.place_com_img()

        elif self.mode =="white_only":
            id_index = np.random.randint(len(self.white))
            self.id = self.white[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.white)
            self.place_com_img()

        elif self.mode =="poc_between_whites":
            id_index = np.random.randint(len(self.poc))
            self.id = self.poc[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.white)
            self.place_com_img()

        elif self.mode =="white_between_poc":
            id_index = np.random.randint(len(self.white))
            self.id = self.white[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.poc)
            self.place_com_img()

        elif self.mode =="female_only":
            id_index = np.random.randint(len(self.female))
            self.id = self.female[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.female)
            self.place_com_img()

        elif self.mode =="male_only":
            id_index = np.random.randint(len(self.male))
            self.id = self.male[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.male)
            self.place_com_img()

        elif self.mode =="male_between_females":
            id_index = np.random.randint(len(self.male))
            self.id = self.male[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.female)
            self.place_com_img()

        elif self.mode =="female_between_males":
            id_index = np.random.randint(len(self.female))
            self.id = self.female[id_index]

            self.get_compare_images()
            self.get_random_image_list(self.male)
            self.place_com_img()
        

    def verify_and_renew(self, picked_img):
        if picked_img == self.comp_pic_place:
            self.user_data['detail_mode'][self.detail_mode]['correct'] += 1
            self.user_data['game_modes'][self.mode]['correct'] +=1
        
        self.user_data['detail_mode'][self.detail_mode]['out_of'] += 1
        self.user_data['game_modes'][self.mode]['out_of'] +=1

        self.load_images()

