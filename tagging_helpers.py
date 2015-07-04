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


def split_on_apostrophe(words):
    """
    Given the set of words as tokenized by TextBlob.tokens, split all the words that contain
    apostrophes into three elements, text before the apostrophe, the apostrophe itself, and text after the apostrophe
    :param words: A list of words as split using TextBlob's 'tokens'
    :return: A list of words with the modification made to words with "'" as noted above
    """
    split_words = []
    for word in words:
        # If the word contains a "'" and is not "''" (which is a quotation mark), split it up before adding
        # the parts to the split words
        if "'" in word and word != "''":
            before = word[:word.index("'")]
            if len(before) > 0:
                split_words.append(before)

            split_words.append("'")

            after = word[word.index("'") + 1:]
            if len(after) > 0:
                split_words.append(after)

        # Otherwise add the word without modification
        else:
            split_words.append(word)

    return split_words


def convert_string_to_structure(string):
    """
    Convert the given string of text into a list of its parts of speech
    :param string: the sentence to get the POS structure of
    :return: a list beginning with 'START' and ending with 'END' which contains the tagged parts of speech of the given
        text. Untagged parts of the original string are left unmodified and appended in their usual positions.
    """
    # Tokenize the string and handle apostrophes appropriately
    blob = TextBlob(string)
    sentence = split_on_apostrophe(blob.tokens)

    # Begin with a start tag, and add the tags of each token in the sentence
    structure = ['START']
    tag_idx = 0
    for token in sentence:
        # If token is tagged, add its tag
        if tag_idx < len(blob.tags) and (token == blob.tags[tag_idx][0]):
            structure.append(blob.tags[tag_idx][1])
            tag_idx += 1
        # Otherwise, add the token itself
        else:
            structure.append(token)

    structure.append('END')

    return structure
