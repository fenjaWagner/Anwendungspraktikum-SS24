import pygame
import json
import numpy as np


class Image_Loader:
    def __init__(self, engine, background) -> None:
        self.engine = engine
        self.background = background
        self.get_comp_image_size()
        self.image_manager = Image_Manager(self.engine)
        self.image_manager.load_images()    
        self.load_image()

    def get_comp_image_size(self):
        if ((6/24)*self.engine.size_x) / ((6/16)*self.engine.size_y) <= 178/ 218:
            x = (6/24)*self.engine.size_x
            factor = x / 178
            self.comp_pic_size = (int(x), int(218 * factor))
            self.exp_pic_size = (int(224 * factor), int(224 * factor))
        else: 
            y = (6/16)*self.engine.size_y
            factor = y /218
            self.comp_pic_size = (int(178 * factor),int(y))
            self.exp_pic_size = (int(224 * factor), int(224 * factor))


    def load_image(self):
        
        self.img1 = self.image_manager.current_images[0]
        self.img2 = self.image_manager.current_images[1]
        self.img3 = self.image_manager.current_images[2]
        self.img4 = self.image_manager.current_images[3]
        self.img5 = self.image_manager.proc_head
        self.img1 =  pygame.transform.scale(self.img1, self.comp_pic_size)
        self.img2 =  pygame.transform.scale(self.img2, self.comp_pic_size)
        self.img3 =  pygame.transform.scale(self.img3, self.comp_pic_size)
        self.img4 =  pygame.transform.scale(self.img4, self.comp_pic_size)
        self.img5 =  pygame.transform.scale(self.img5, self.exp_pic_size)
        self.rect1 = self.img1.get_rect()
        self.rect2 = self.img2.get_rect()
        self.rect3 = self.img3.get_rect()
        self.rect4 = self.img4.get_rect()
        

    def draw_image(self, surface):
        surface.fill(self.background)
        surface.blit(self.img1, ((self.engine.size_x-(4*self.comp_pic_size[0]))//5, ((self.engine.size_y//2)-self.comp_pic_size[1])//2))
        surface.blit(self.img2, ((self.engine.size_x-(4*self.comp_pic_size[0]))*2//5 + self.comp_pic_size[0],  ((self.engine.size_y//2)-self.comp_pic_size[1])//2))
        surface.blit(self.img3, ((self.engine.size_x-(4*self.comp_pic_size[0]))*3//5 + 2*self.comp_pic_size[0],  ((self.engine.size_y//2)-self.comp_pic_size[1])//2))
        surface.blit(self.img4, ((self.engine.size_x-(4*self.comp_pic_size[0])) * 4//5 + 3*self.comp_pic_size[0],  ((self.engine.size_y//2)-self.comp_pic_size[1])//2))
        surface.blit(self.img5, ((self.engine.size_x - self.exp_pic_size[0]) //2 , self.engine.size_y //2 + (self.engine.size_y//2-self.exp_pic_size[1])//2))

    def get_image(self):
        return self.img1, self.img2, self.img3, self.img4, self.img5
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("1")
                self.image_manager.verify_and_renew(1)
                self.load_image()

            elif event.key == pygame.K_2:
                print("2")
                self.image_manager.verify_and_renew(2)
                self.load_image()

            elif event.key == pygame.K_3:
                print("3")
                self.image_manager.verify_and_renew(3)
                self.load_image()

            elif event.key == pygame.K_4:
                print("4")
                self.image_manager.verify_and_renew(4)
                self.load_image()

             
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Call the on_mouse_button_down() function
            if self.rect1.collidepoint(event.pos):
                print("1")
                self.image_manager.verify_and_renew(1)
                self.load_image()

            elif self.rect2.collidepoint(event.pos):
                print("2")
                
                self.image_manager.verify_and_renew(2)
                self.load_image()

            elif self.rect3.collidepoint(event.pos):
                print("3")
                
                self.image_manager.verify_and_renew(3)
                self.load_image()

            elif self.rect4.collidepoint(event.pos):
                print("4")
                
                self.image_manager.verify_and_renew(4)
                self.load_image()


class Image_Manager:
    def __init__(self, engine):
        self.engine = engine
        self.detail_mode = self.engine.config["detail_mode"]
        self.game_modes = self.engine.config["game_modes"]
        self.mode = None

        self.item_dict = self.get_image_item_dict()
        self.image_config = self.engine.image_config
        self.mode = "mixed"
        self.exp_list = self.item_dict[self.image_config[self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config[self.mode]['comp_pic_list']]
        self.identity = self.item_dict['identity_pic']


        self.img_path = "file_system/"+self.detail_mode+"/"
        self.img_path_unproc = "file_system/unprocessed/"

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
        self.comp_pic = pygame.image.load(self.img_path_unproc + comp_num+".jpg").convert()

        print("Exp_Head:", proc_num)
        print("Comp_Head:", comp_num)

    def get_random_image_list(self, li):
        self.current_images = []
        np.random.seed()
        test_list = []
        length = len(li)
        img_index_li= np.random.randint(length, size = 3)
        int_1 = img_index_li[0]
        int_2 = img_index_li[1]
        int_3 = img_index_li[2]

        while li[int_1] == self.id :
            int_1 = (int_1 + 1)%length

        while li[int_2] == self.id or int_2 == int_1:
            int_2 = (int_2 + 1)%length
        
        while li[int_3] == self.id or int_3 == int_1 or int_3 == int_2:
            int_3 = (int_3 + 1)%length
        
        pic_num = sum(img_index_li)%2
        
        for i in [int_1, int_2, int_3]:
            test_list.append(self.identity[li[i]][pic_num])
            img = pygame.image.load(self.img_path_unproc + self.identity[li[i]][pic_num]+".jpg").convert()
            self.current_images.append(img)

        print("TestList:", test_list)
        


    def place_com_img(self):
        self.comp_pic_place = np.random.randint(4)
        print("place:", self.comp_pic_place +1)
        self.current_images.insert(self.comp_pic_place, self.comp_pic)
            
    
    def load_images(self):
        np.random.seed()
        mode_index = np.random.randint(len(self.game_modes))
        self.mode = self.game_modes[mode_index]
        print(self.mode)

        self.exp_list = self.item_dict[self.image_config[self.mode]['exp_list']]
        self.comp_pic_list = self.item_dict[self.image_config[self.mode]['comp_pic_list']]     

        id_index = np.random.randint(len(self.exp_list))
        self.id = self.exp_list[id_index]
        self.get_compare_images()
        self.get_random_image_list(self.comp_pic_list)
        self.place_com_img()

        
    def verify_and_renew(self, picked_img):
        if picked_img -1 == self.comp_pic_place:
            print("right choice")
            self.user_data['detail_mode'][self.detail_mode]['correct'] += 1
            self.user_data['game_modes'][self.mode]['correct'] +=1
        else:
            print("wrong choice")
        
        self.user_data['detail_mode'][self.detail_mode]['out_of'] += 1
        self.user_data['game_modes'][self.mode]['out_of'] +=1

        self.load_images()

