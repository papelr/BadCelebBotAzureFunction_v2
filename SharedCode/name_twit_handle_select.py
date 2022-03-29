
# Packages
import pandas as pd
import re

# Class to keep celeb name the same throughout ----
class NameHandle():

    # Constructor function - read in the sheet
    def __init__(self):

        handle_csv = pd.read_csv('BadCelebSpreadsheets/handle_list.csv', encoding='latin-1')
        ran_line = handle_csv.sample(n = 1, replace = False)
        self.reg_name = ran_line['name'].to_string()
        # print("one" + self.reg_name)
        self.handle_tag = ran_line['handle'].to_string()


    # Regular Tweet: format randomly pulled celeb name and twitter handle
    def name_and_handle(self, gen_name):

        # create & format sentence, to send back to main.py
        # print("two" + self.reg_name)
        name_hand_sent = self.reg_name + "'s real name is" + ' ' + gen_name + '. ' + self.handle_tag
        name_hand_sent = re.sub(r'\d+', '', name_hand_sent)
        name_hand_sent = " ".join(re.split("\s+", name_hand_sent,
                                           flags = re.UNICODE))
        # print(name_hand_sent)
        return name_hand_sent


    def handle_only(self):

        # pull out just the handle and return!
        just_handle = self.handle_tag
        just_handle = re.sub(r'\d+', '', just_handle)
        just_handle = " ".join(re.split("\s+", just_handle, flags = re.UNICODE))
        just_handle = just_handle.lstrip()
        return just_handle


    # Reply Tweet: format randomly pulled celeb name and twitter handle
    def name_and_handle_reply(self, gen_name):

        # create & format sentence, to send back to main.py
        name_hand_sent = self.reg_name + "'s real name is" + ' ' + gen_name + '. Oops! ' + self.handle_tag
        name_hand_sent = 'FYI, ' + name_hand_sent 
        name_hand_sent = re.sub(r'\d+', '', name_hand_sent)
        name_hand_sent_reply = " ".join(re.split("\s+", name_hand_sent,
                                           flags = re.UNICODE))
        # print(name_hand_sent)
        return name_hand_sent_reply    


    # function to keep celeb name the same through the entire process
    def name_insurance(self):

        same_name = re.sub(r'\d+', '', self.reg_name)
        same_name = same_name.strip()
        # print(same_name)
        return same_name

# Main function ----
if __name__ == '__main__':
    NameHandle().name_and_handle()
    NameHandle().name_and_handle_reply()
    NameHandle().handle_only()
    NameHandle().name_insurance()
    
