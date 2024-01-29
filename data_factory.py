import os
import random

import pandas as pd


class Data:
    def __init__(self):
        self.source_data = pd.read_csv("data/data.csv")
        try:
            self.words_to_learned = pd.read_csv("data/words_to_learned.csv")
        except FileNotFoundError:
            self.words_to_learned = self.source_data
            self.words_to_learned.to_csv("data/words_to_learned.csv")

        self.learned_words = None
        self.row = None
        self.index = None
        self.range = []

        # Read range from file or create a new one if it doesn't exist
        self.load_range()

    def load_range(self):
        if os.path.exists("data/range.txt"):
            with open("data/range.txt", "r") as file:
                self.range = [int(index) for index in file.read().splitlines()]
        else:
            self.range = []

    def save_range(self):
        with open("data/range.txt", "w") as file:
            file.write("\n".join(map(str, self.range)))

    def get_word(self):
        self.index = random.randrange(0, 2000)
        if self.index in self.range:
            self.get_word()
        self.row = self.words_to_learned.loc[self.index]
        deutsch = self.row["deutsch"]
        english = self.row["english"]
        return deutsch, english

    def save_learned_word(self, func):
        new_data_form = {
            "Deutsch": [self.row["deutsch"]],
            "English": [self.row["english"]]
        }
        new_data = pd.DataFrame(new_data_form)

        # Drop the row from the DataFrame
        self.words_to_learned = self.words_to_learned.drop(self.index)
        self.range.append(self.index)

        # Write the updated DataFrame back to the file
        self.words_to_learned.to_csv("data/words_to_learned.csv", index=False)

        # Save the updated range to the file
        self.save_range()

        # Check if the file exists
        try:
            pd.read_csv("data/learned_word.csv")
            # Append new data without index
            new_data.to_csv("data/learned_word.csv", mode="a", header=False, index=False)
        except FileNotFoundError:
            # Create a new file with header and add data with index
            new_data.to_csv("data/learned_word.csv", mode="w", header=True, index=False)

        func()

    def reset_all(self):
        os.remove("data/learned_word.csv")
        os.remove("data/words_to_learned.csv")
        os.remove("data/range.txt")
        # self.words_to_learned = self.source_data
        # self.words_to_learned.to_csv("data/words_to_learned.csv")
