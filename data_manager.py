import json
import states


class Data_Manager():
    """Manages the username and -data.
    """
    def __init__(self, engine) -> None:
        self.engine = engine
        self.user = None
        self.data = self.read_data()
        self.user_data = {  "detail_mode":{"generic_detail":{"correct": 0,
                                                           "out_of": 0},
                                        "individual_detail":{"correct": 0,
                                                           "out_of": 0},
                                        "no_detail":{"correct": 0,
                                                           "out_of": 0},
                                        "identity":{"correct": 0,
                                                           "out_of": 0}},
                            "game_modes":{  }}
        for mode in list(self.engine.image_config.keys()):
            self.user_data['game_modes'][mode] = {"correct": 0,
                                                    "out_of": 0}

    def read_data(self):
        """Reads data from file.

        Returns:
            dict: data from all users
        """
        with open('user_data.txt') as user_data_file:
            data_in = user_data_file.read()
            return json.loads(data_in)
    
    def sign_up(self, username: str, new_user_flag):
        """Signs in a user and returns the specific name and data.

        Returns:
            dict: userdata
        """
        if not new_user_flag:
            #print("Data - sign in: ", self.data)
            print("Username: ", username)
            if username in self.data.keys():
                self.user = username
                self.user_data = self.data[self.user]
                self.engine.machine.next_state = states.UserModeState(self.engine, (140,140,140))

                
            else:
                self.engine.machine.next_state = states.LogInError(self.engine, (140,140,140))
    
        else:
            if self.user in self.data.keys():
                self.engine.machine.next_state = states.ChosenUsernameError(self.engine, (140,140,140))
            else: 
                self.user = username
                self.data[self.user] = self.user_data
                self.write_data()
                self.engine.machine.next_state = states.UserModeState(self.engine, (140,140,140))
    
        
    def write_data(self):
        """Writes new user to datafile.
        """
        with open('user_data.txt', 'w') as user_data_file:
            user_data_file.write(json.dumps(self.data))



