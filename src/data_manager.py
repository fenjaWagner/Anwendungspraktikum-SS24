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
        self.data = self.read_data() # Reads in the data of all users.
        self.default_user_data = {}
        self.get_default_user_data()
        
    def get_default_user_data(self):
        """Generates the dictionary for one user that is stored in the data dictionary.
        """
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
        if not new_user_flag: # Login process
            if username in self.data.keys():
                self.user = username
                self.user_data = self.data[self.user]
                return states.InstructionState(self.engine)        
                
            else:
                return states.LogInErrorState2(self.engine)
    
        else: # A new user signs up.
            if username in self.data.keys():
                return states.ChosenUsernameErrorState2(self.engine)
            else: 
                self.user = username
                self.user_data = copy.deepcopy(self.default_user_data) # Create a new user data dictionary.
                self.data[self.user] = self.user_data # Store it in the data dictionary.
                self.write_data()
                return states.InstructionState(self.engine)
    
        
    def write_data(self):
        """Writes new user to datafile.
        """
        with open('data/user_data.txt', 'w') as user_data_file:
            user_data_file.write(json.dumps(self.data))

        with open('../result_data/readable_data.txt', 'w') as user_data_file:
            pprint.pprint(self.data, stream = user_data_file)

            


