"""
Helper functions used to do the part of speech tagging. Requires the textblob library is installed
"""
from textblob import TextBlob

__author__ = 'github.com/samshadwell'

def get_string_tags(string):
    """
    Get the part-of-speech tag associated with each word in the string
    :param string: the string to tag
    :return: An array of tuples, where the index of the tuple is its position in the original string, its first element
        is the tagged word, and the second element is the tag itself
    """
    blob = TextBlob(string)
    return blob.tags

def map_pos_to_words(strings):
    """
    Map each part of speech found in the given collection of strings to an array of words which were tagged with that
    part of speech
    :param strings: the list of strings to do the tagging/mapping for
    :return: a dictionary mapping a string of each POS tag found in the strings list to a list of words that were
        assigned that tag by the POS tagger
    """
    mapping = {}
    for string in strings:
        tags = get_string_tags(string)
        for word, tag in tags:
            if tag in mapping.keys():
                mapping[tag].append(word)
            else:
                mapping[tag] = [word]

    return mapping
