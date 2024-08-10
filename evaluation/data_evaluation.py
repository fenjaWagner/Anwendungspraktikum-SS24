import matplotlib.pyplot as plt
import numpy as np

class DataEvaluation:
    def __init__(self, engine):
        self.engine = engine

    def plot(self):

        detail_modes = self.engine.config["detail_modes"]
        order = self.engine.config["order"]
        username = self.engine.data_manager.user
        out_of = []
        correct = []
        for mode in detail_modes:
            value_out_of = self.engine.data_manager.user_data[order][mode]["overall"]["out_of"]
            out_of.append(value_out_of)
            value_correct = self.engine.data_manager.user_data[order][mode]["overall"]["correct"]
            correct.append(value_correct)
        percentage = [c/o * 100 for c, o in zip(correct, out_of)]
        max_value = max(percentage)
       
        fig, ax = plt.subplots()

        ax.bar(detail_modes, percentage, label=detail_modes)
        ax.set_ylabel('Percentage')
        ax.set_title('Percentage of correct answers per game mode of user '+ username)
        ax.set_xticklabels(detail_modes, rotation=45, ha='right')  # Rotate the labels by 45 degrees
        ax.set_ylim(0, max_value + 5)
        plt.savefig("evaluation/"+username+".png", format="png", dpi=300, bbox_inches="tight")