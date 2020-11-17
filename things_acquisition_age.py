"""
Program for producing ages of acquisition for the objects of the THINGS database
 by using the AoAs of the words representing those THINGS
"""
import re
import math
import pandas as pd


def filter_to_az(text: str):
    """Filters characters to non-accented English a-to-z"""
    return re.sub("[^a-zA-Z]+", "", text)


if __name__ == '__main__':
    things_df = pd.read_csv('things_concepts.tsv', sep='\t')
    aoas_df = pd.read_csv('AoA_ratings_Kuperman_et_al_BRM.tsv', sep='\t')

    # Prepare word/synonym list
    thingwords_and_synonyms = [(canon_word, synonyms.split(', '))
                               for canon_word, synonyms in zip(things_df['Word'], things_df['WordNet Synonyms'])]


    print("Word\tLowest_AoA\tHighest_AoA\tAll_Synonyms_Had_AoAs")
    # Take the synonyms for each object in the things database and find the lowest/highest age of acquisition

    # The ages of acquisitions are for words, not senses. If this changes, this setup needs to be reconsidered
    aoa_words_and_values = zip(aoas_df['Word'].astype(str), aoas_df['Rating.Mean'])
    normalized_aoa_dict = {filter_to_az(word.lower()): value
                           for word, value in aoa_words_and_values}

    for thingword, synonyms in thingwords_and_synonyms:
        lowest_aoa = math.nan
        highest_aoa = math.nan
        normalized_synonyms = {filter_to_az(synonym.lower()) for synonym in synonyms}
        synonyms_having_aoas = normalized_synonyms & normalized_aoa_dict.keys()

        for normalized_synonym in synonyms_having_aoas:
            aoavalue = normalized_aoa_dict[normalized_synonym]
            if lowest_aoa > aoavalue or math.isnan(lowest_aoa):
                lowest_aoa = aoavalue
            if highest_aoa < aoavalue or math.isnan(highest_aoa):
                highest_aoa = aoavalue

        all_synonyms_had_aoas = len(normalized_synonyms) == len(synonyms_having_aoas)

        print(f"{thingword}\t{lowest_aoa}\t{highest_aoa}\t{all_synonyms_had_aoas}")
