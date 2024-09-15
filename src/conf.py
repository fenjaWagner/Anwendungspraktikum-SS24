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

proc_path = "file_system/processed/"
unproc_path = "file_system/unprocessed/"

conf = {# Detail modes that will be used in the game.
        "detail_modes": ["generic_detail", "individual_detail", "coarse", "complete_identity_coarse", "complete_identity_detail"],
        # The order states whether the user is given a processed image and has to choose 
        # from unprocessed pictures or vice versa.
        "order": "exp_unproc", # or exp_unproc
        # Game modes that will be used in the game.
        "game_modes": ["mixed", 
                   "poc_between_non_pocs", 
                   "non_poc_between_pocs", 
                   "female_only", 
                   "male_only", 
                   "female_between_males",
                   "male_between_females"],
        "layout": {"caption": "Fancy Name",
                    "screen_size": (1400, 750),
                    "font": "arial",
                    "original_image_size": (178, 218), # for scaling
                   "processed_image_size": (224,224), # for scaling
                   "background_color": (140,140,140) # colour tuple
                   }
}

image_conf = {
                # States what lists in image_item.txt will be used for loading 
                # the images in the respective game mode.
                "game_modes": {"mixed": {"exp_list": 'identity_all',
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

                # Stores the paths to the processed images depending on the current game mode and order.
                # If one modifies the file_system structure, the changes need to be applied here.
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

