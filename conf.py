import pygame
# detail modes: "generic_detail" (Detail of the dummy head)
#               "individual_detail" (Detail of the expression individual)
#               "coarse" (coarse head shapes)
#               "complete_identity_coarse" (Reconstruction of the whole face without expression transfer)
#               "complete_identity_detail" (Reconstruction of the whole face without expression transfer with details)
# game_modes:   "mixed" (random pictures)
#               "poc_only" (only pictures of poc)
#               "non_poc_only" (only picture of non_poc people)
#               "poc_between_non_pocs" (expression picture poc, others non_poc people)
#               "non_poc_between_poc" (expression picture non_poc people, others poc)
#               "female_only" (only pictures of females)
#               "male_only" (only pictures of males)
#               "female_between_males" (expression picture female, others male)
#               "male_between_females" (expression picture male, others female)
pygame.init()
proc_path = "file_system/processed/"
unproc_path = "file_system/unprocessed/"

conf = {"detail_modes": ["generic_detail", "individual_detail", "coarse", "complete_identity_coarse", "complete_identity_detail"],
        "order": "exp_proc", # or exp_unproc
        "game_modes": ["mixed", 
                   "poc_between_non_pocs", 
                   "non_poc_between_pocs", 
                   "female_only", 
                   "male_only", 
                   "female_between_males",
                   "male_between_females"],
        "layout": {"font": pygame.font.SysFont(None, 30), 
                    "caption": "Fancy Name",
                    "screen_size": (1400,750),
                    "original_image_size": (178, 218),
                   "processed_image_size": (224,224),
                   "background_color": (140,140,140)
                   }
}

image_conf = {"game_modes": {"mixed": {"exp_list": 'identity_all',
                                "comp_pic_list": 'identity_all'}, 
                        "poc_between_non_pocs": {"exp_list": "poc",
                                                "comp_pic_list": "non_poc"}, 
                        "poc_only": {"exp_list": "poc",
                                        "comp_pic_list": "poc"},

                        "non_poc_between_pocs": {"exp_list": "non_poc",
                                                "comp_pic_list": "poc"}, 
                        "non_poc_only": {"exp_list": "non_poc",
                                        "comp_pic_list": "non_poc"},
                        "female_only": {"exp_list": "female",
                                        "comp_pic_list": "female"}, 
                        "male_only": {"exp_list": "male",
                                        "comp_pic_list": "male"}, 
                        "female_between_males": {"exp_list": "female",
                                                "comp_pic_list": "male"},
                        "male_between_females": {"exp_list": "male",
                                                "comp_pic_list": "female"}},

            "exp_proc": {"identity": {"exp_heads_path": proc_path +"identity/",
                                    "comp_heads_path": unproc_path},
                        "generic_detail": {"exp_heads_path": proc_path +"generic_detail/",
                                    "comp_heads_path": unproc_path},
                        "individual_detail": {"exp_heads_path": proc_path +"individual_detail/",
                                    "comp_heads_path": unproc_path},
                        "coarse": {"exp_heads_path": proc_path +"coarse/",
                                    "comp_heads_path": unproc_path},
                        "complete_identity_coarse": {"exp_heads_path": proc_path +"complete_identity_coarse/",
                                    "comp_heads_path": unproc_path},
                        "complete_identity_detail": {"exp_heads_path": proc_path +"complete_identity_detail/",
                                    "comp_heads_path": unproc_path}},
            
            "exp_unproc": {"identity": {"comp_heads_path": proc_path +"identity/",
                                    "exp_heads_path": unproc_path},
                        "generic_detail": {"comp_heads_path": proc_path +"generic_detail/",
                                    "exp_heads_path": unproc_path},
                        "individual_detail": {"comp_heads_path": proc_path +"individual_detail/",
                                    "exp_heads_path": unproc_path},
                        "coarse": {"comp_heads_path": proc_path +"coarse/",
                                    "exp_heads_path": unproc_path},      
                        "complete_identity_coarse": {"comp_heads_path": proc_path +"complete_identity_coarse/",
                                    "exp_heads_path": unproc_path},  
                        "complete_identity_detail": {"comp_heads_path": proc_path +"complete_identity_detail/",
                                    "exp_heads_path": unproc_path}}   
            }

