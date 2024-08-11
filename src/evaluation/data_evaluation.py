import matplotlib.pyplot as plt
import numpy as np

class DataEvaluation:
    """Class that manages the evaluation of the userdata.
    """
    def __init__(self, engine):
        """Inizialization of the DataEvaluation class.

        Args:
            engine (DisplayEngine): Engine that holds the configuration, image config, and user data.
        """
        self.engine = engine
        self.detail_modes = self.engine.config["detail_modes"]
        self.order = self.engine.config["order"]
        self.data = self.engine.data_manager.data
        self.username = self.engine.data_manager.user

    def get_current_user_data(self, user):
        """Returns lists of the data of the current user.

        Args:
            user (str): Name of the current user.

        Returns:
            list, list: Lists with the total and correct number of choices.
        """
        if not user:
            return None, None
        out_of = []
        correct = []
        for mode in self.detail_modes:
            value_out_of = self.data[user][self.order][mode]["overall"]["out_of"]
            out_of.append(value_out_of)
            value_correct = self.data[user][self.order][mode]["overall"]["correct"]
            correct.append(value_correct)
        
        return correct, out_of
    
    def get_overall_data(self):
        """Returns lists of the cummulated data of all users.

        Returns:
            list, list: Lists with the total and the correct number of choices of all users together.
        """
        correct_all = [0 for _ in range(len(self.detail_modes))]
        out_of_all = [0 for _ in range(len(self.detail_modes))]
        for user in self.data.keys():
            user_correct, user_out_of = self.get_current_user_data(user)
            correct_all = [c + u for c, u in zip(correct_all, user_correct)]
            out_of_all = [o + u for o, u in zip(out_of_all, user_out_of)]
        return correct_all, out_of_all
    
    def plot(self, correct, out_of, user):
        """Plots the data given in correct_out list and out_of list.

        Args:
            correct (list): List of number of correct choices per game mode.
            out_of (list): List of total number of choices per game mode.
            user (str): Username.
        """
        if not correct:
            print("No username.")
            return
        percentage = [(c / o * 100) if o != 0 else 0 for c, o in zip(correct, out_of)]
        print(f"percentage of {user} ", percentage)
        max_value = max(percentage)       
        fig, ax = plt.subplots()

        ax.axhline(y=25, color='r', linestyle='--') # Add a line at 25% (for comparison to random choice).

        ax.bar(self.detail_modes, percentage, label=self.detail_modes)
        ax.set_ylabel('Percentage')
        ax.set_title('Percentage of correct answers per game mode of user '+ user)
        ax.set_xticklabels(self.detail_modes, rotation=45, ha='right')  # Rotate the labels by 45 degrees
        ax.set_ylim(0, max(max_value, 25) + 5)
        plt.savefig("../result_data/plots/"+user+".png", format="png", dpi=300, bbox_inches="tight")

    def print_csv(self):
        """Prints the data dictionary into a csv file.
        """
        csv_file = open("../result_data/data.csv", "w")
        for user in self.data.keys():
            for order in ["exp_proc", "exp_unproc"]:
                for detail in self.detail_modes:
                    for mode in self.engine.config["game_modes"]:
                        string = user + ", " + order +", " + detail + ", " + mode + ", "
                        out_of = self.data[user][order][detail][mode]["out_of"]
                        correct = self.data[user][order][detail][mode]["correct"]
                        if out_of != 0:
                            percentage = (correct/out_of) * 100
                        else: 
                            percentage = 0

                        csv_file.write(string + str(out_of) + ", " +str(percentage) + "\n")
        csv_file.close()

    def eval(self):
        """Invokes collecting, plotting and printing of the data.
        """
        self.username = self.engine.data_manager.user
        user_c, user_o = self.get_current_user_data(self.username)
        self.plot( user_c, user_o, self.username)
        all_c, all_o = self.get_overall_data()
        self.plot(all_c, all_o, "overall")
        self.print_csv()