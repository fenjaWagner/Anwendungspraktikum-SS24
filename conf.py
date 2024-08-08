import pygame
# detail modes: "generic_detail" (Detail of the dummy head)
#               "individual_detail" (Detail of the expression individual)
#               "no_detail" (coarse head shapes)
#               "identity" (Reconstruction of the whole face without expression transfer)
# game_modes:   "mixed" (random pictures)
#               "poc_only" (only pictures of poc)
#               "non_poc_only" (only picture of non_poc people)
#               "poc_between_non_pocs" (expression picture poc, others non_poc people)
#               "non_poc_between_poc" (expression picture non_poc people, others poc)
#               "female_only" (only pictures of females)
#               "male_only" (only pictures of males)
#               "female_between_males" (expression picture female, others male)
#               "male_between_females" (expression picture male, others female)


conf = {"detail_mode": "individual_detail",
        "order": "exp_unproc", # or exp_proc
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

image_conf = {"mixed": {"exp_list": 'identity_all',
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
                                    "comp_pic_list": "female"},

            "exp_proc": {"identity": {"exp_heads_path": "file_system/processed/identity/",
                                    "comp_heads_path": "file_system/unprocessed/"},
                        "generic_detail": {"exp_heads_path": "file_system/processed/generic_detail/",
                                    "comp_heads_path": "file_system/unprocessed/"},
                        "individual_detail": {"exp_heads_path": "file_system/processed/individual_detail/",
                                    "comp_heads_path": "file_system/unprocessed/"},
                        "no_detail": {"exp_heads_path": "file_system/processed/no_detail/",
                                    "comp_heads_path": "file_system/unprocessed/"}},
            
            "exp_unproc": {"identity": {"comp_heads_path": "file_system/processed/identity/",
                                    "exp_heads_path": "file_system/unprocessed/"},
                        "generic_detail": {"comp_heads_path": "file_system/processed/generic_detail/",
                                    "exp_heads_path": "file_system/unprocessed/"},
                        "individual_detail": {"comp_heads_path": "file_system/processed/individual_detail/",
                                    "exp_heads_path": "file_system/unprocessed/"},
                        "no_detail": {"comp_heads_path": "file_system/processed/no_detail/",
                                    "exp_heads_path": "file_system/unprocessed/"}}                   
            }

