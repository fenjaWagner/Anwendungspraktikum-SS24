import matplotlib.pyplot as plt
import numpy as np

class DataEvaluation:
    def __init__(self, engine):
        self.engine = engine
        self.detail_modes = self.engine.config["detail_modes"]
        self.order = self.engine.config["order"]
        self.data = self.engine.data_manager.data
        self.username = self.engine.data_manager.user

    def get_current_user_data(self, user):
        print("user current user data: ", user)
        out_of = []
        correct = []
        for mode in self.detail_modes:
            value_out_of = self.data[user][self.order][mode]["overall"]["out_of"]
            out_of.append(value_out_of)
            value_correct = self.data[user][self.order][mode]["overall"]["correct"]
            correct.append(value_correct)
        
        return correct, out_of
    
    def get_overall_data(self):
        correct_all = [0 for _ in range(len(self.detail_modes))]
        out_of_all = [0 for _ in range(len(self.detail_modes))]
        for user in self.data.keys():
            user_correct, user_out_of = self.get_current_user_data(user)
            correct_all = [c + u for c, u in zip(correct_all, user_correct)]
            out_of_all = [o + u for o, u in zip(out_of_all, user_out_of)]
        return correct_all, out_of_all


    
    def plot(self, correct, out_of, user):
        percentage = [(c / o * 100) if o != 0 else 0 for c, o in zip(correct, out_of)]
        print(f"percentage of {user} ", percentage)
        max_value = max(percentage)       
        fig, ax = plt.subplots()

        ax.axhline(y=25, color='r', linestyle='--')

        ax.bar(self.detail_modes, percentage, label=self.detail_modes)
        ax.set_ylabel('Percentage')
        ax.set_title('Percentage of correct answers per game mode of user '+ user)
        ax.set_xticklabels(self.detail_modes, rotation=45, ha='right')  # Rotate the labels by 45 degrees
        ax.set_ylim(0, max(max_value, 25) + 5)
        plt.savefig("evaluation/"+user+".png", format="png", dpi=300, bbox_inches="tight")

    def eval(self):
        user_c, user_o = self.get_current_user_data(self.username)
        self.plot( user_c, user_o, self.username)
        all_c, all_o = self.get_overall_data()
        self.plot(all_c, all_o, "overall")