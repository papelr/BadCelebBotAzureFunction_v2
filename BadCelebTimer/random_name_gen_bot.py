
import ssl
import random
import pandas as pd
import numpy as np
from hyphen import Hyphenator  


# Stuck the whole thing in one large function for callability purposes
def name_gen():

    # Read in excel ----
    def data_read():

        # read in names list
        init_df = pd.read_csv('BadCelebSpreadsheets/bot-name-list.csv')
        return init_df


    # Clean firstNames ----
    def first_name_clean(init_df):

        # get firstName column, uppercase everything
        first_df = init_df['firstNames']
        # first_df = first_df.apply(lambda x: x.lower())
        first_df = first_df.apply(lambda x: str(x))

        return first_df


    # Clean lastNames ----
    def last_name_clean(init_df):

        # get lastName column, split it all correctly
        last_df = init_df['lastNames']

        last_df = last_df.apply(lambda x: str(x))
        last_df = last_df.apply(lambda x: x.split(':', 1)[0])

        return last_df


    # Split lastNames into syllables ----
    def syllable_split(last_df):

        # getting ready for splitting (also want it lowercase for split)
        names = last_df
        names = names.apply(lambda x: x.lower())
        h_en = Hyphenator('en_US')
        syllable_list = []
        ssl._create_default_https_context = ssl._create_unverified_context

        # use that syllable split library - doesn't split everything
        for i in names:
            splits = h_en.syllables(i)
            syllable_list.append(splits)

        return syllable_list


    # Convert those syllables into one large list ----
    def syllable_listing(syllable_list):

        # turn list into one big list of syllables
        syl = syllable_list
        syl = np.unique(np.hstack(syl)).tolist()

        return syl


    # Randomly pair (last)name syllables into new last names ----
    def pair_last(syl):

        # pair random syllables - create function
        pair_init = syl
        def pop_random(pair_init):
            idx = random.randrange(0, len(pair_init))
            return pair_init.pop(idx)

        # create random pairs - outputs list form
        pairs = []
        while len(pair_init) > 1:
            rand1 = pop_random(pair_init)
            rand2 = pop_random(pair_init)
            pair = rand1, rand2
            pairs.append(pair)

        # turn random pairs into a single word, capitlize first letter
        pair_list = pd.DataFrame(pairs)
        pair_join = pair_list[0] + pair_list[1]
        pair_join = pair_join.str.title()
        pair_join = pd.DataFrame(pair_join)

        return pair_join


    # Pair first names to randomly created last names ----
    def pair_first_last(first_df, pair_join):

        # join the two columns
        df1 = pd.DataFrame(first_df.str.title())
        df2 = pd.DataFrame(pair_join)
        df = pd.concat([df1, df2], axis = 1, join = 'outer')

        # randomize within in each column, and then shuffle both columns
        df = df.apply(lambda x: x.sample(frac = 1).values)
        df = df.rename(columns={0: 'lastNames'})

        # replace NaNs with random values already in lastNames column
        df = df.apply(lambda x: np.where(x.isnull(),
                                         x.dropna().sample(len(x),
                                                           replace = True), x))
        # return combo name, with upper class 'oth'
        df_all = df['firstNames'] + ' ' + df['lastNames']

        return df_all

    # run all functions
    one = data_read()
    two = first_name_clean(one)
    three = last_name_clean(one)
    four = syllable_split(three)
    five = syllable_listing(four)
    six = pair_last(five)
    seven = pair_first_last(two, six)
    name_list = random.choice(seven)

    # use print(name_list) if need to print w/out return
    # print(name_list)
    return name_list


# Main function ----
if __name__ == '__main__':
    name_gen()

