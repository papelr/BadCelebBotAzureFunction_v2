
# Packages
import pandas as pd
import re

# Class to keep celeb name the same throughout ----
class NameHandle():

    def __init__(self):

        handle_csv = pd.read_csv('BadCelebSpreadsheets/handle_list.csv', encoding='latin-1')
        ran_line = handle_csv.sample(n = 1, replace = False)
        self.reg_name = ran_line['name'].to_string()
        # print("one" + self.reg_name)
        self.handle_tag = ran_line['handle'].to_string()

    # format randomly pulled celeb name and twitter handle
    def name_and_handle(self, gen_name):

        # create & format sentence, to send back to main.py
        # print("two" + self.reg_name)
        name_hand_sent = self.reg_name + "'s real name is" + ' ' + gen_name + '. ' + self.handle_tag
        name_hand_sent = re.sub(r'\d+', '', name_hand_sent)
        name_hand_sent = " ".join(re.split("\s+", name_hand_sent,
                                           flags = re.UNICODE))
        # print(name_hand_sent)
        return name_hand_sent

    # function to keep celeb name the same through the entire process
    def name_insurance(self):

        same_name = re.sub(r'\d+', '', self.reg_name)
        same_name = same_name.strip()
        # print(same_name)
        return same_name

# Main function ----
if __name__ == '__main__':
    NameHandle().name_and_handle()
    NameHandle().name_insurance()
