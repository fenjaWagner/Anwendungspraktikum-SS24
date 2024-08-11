import json
import states
import pprint
import copy


class Data_Manager():
    """Manages the username and -data.
    """
    def __init__(self, engine) -> None:
        self.engine = engine
        self.user = None
        self.data = self.read_data()
        self.default_user_data = {}
        self.get_default_user_data()
        
    def get_default_user_data(self):
        for order in ["exp_proc", "exp_unproc"]:
            self.default_user_data[order] = {"overall": {"correct": 0,
                                                        "out_of": 0,
                                                         "history": []}}
            for detail_mode in self.engine.config["detail_modes"]:
                self.default_user_data[order][detail_mode] = {"overall": {"correct": 0,
                                                                        "out_of": 0,
                                                                "history": []}}
                for game_mode in self.engine.config["game_modes"]:
                    self.default_user_data[order][detail_mode][game_mode] = {"correct": 0,
                                                        "out_of": 0,
                                                        "history":[]}

    def read_data(self):
        """Reads data from file.

        Returns:
            dict: data from all users
        """
        with open('data/user_data.txt') as user_data_file:
            data_in = user_data_file.read()
            return json.loads(data_in)
    
    def sign_up(self, username: str, new_user_flag):
        """Signs in a user and returns the specific name and data.

        Returns:
            dict: userdata
        """
        if not new_user_flag:
            print("Username: ", username)
            if username in self.data.keys():
                self.user = username
                self.user_data = self.data[self.user]
                self.engine.machine.next_state = states.UserModeState(self.engine)

                
            else:
                self.engine.machine.next_state = states.LogInErrorState2(self.engine)
    
        else:
            print(self.data.keys())
            if username in self.data.keys():
                self.engine.machine.next_state = states.ChosenUsernameErrorState2(self.engine)
            else: 
                self.user = username
                self.user_data = copy.deepcopy(self.default_user_data)
                self.data[self.user] = self.user_data
                self.write_data()
                self.engine.machine.next_state = states.UserModeState(self.engine)
    
        
    def write_data(self):
        """Writes new user to datafile.
        """
        with open('data/user_data.txt', 'w') as user_data_file:
            user_data_file.write(json.dumps(self.data))

        with open('data/readable_data.txt', 'w') as user_data_file:
            pprint.pprint(self.data, stream = user_data_file)

            


