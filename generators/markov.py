"""
Generates text from the configured pages and post history using a first-order Markov model
"""
import random
from textblob import TextBlob

import config
import facebook_helpers as fb
import tagging_helpers as pos

__author__ = 'github.com/samshadwell'


def construct_first_order_markov(markov, sequence):
    """
    Add data from the sequence to the given first-order Markov model
    :param markov: the existing Markov model
    :param sequence: sequence of states to add to the model
    :return: an updated version of 'markov'
    """
    # Go through every sequential two states in the given sequence
    for idx in range(1, len(sequence)):
        first = sequence[idx - 1]
        second = sequence[idx]
        # If the first state has never been a 'from' state before, add it
        if first not in markov.keys():
            markov[first] = {second: 1}
        # Otherwise, if we have come from the first state before, either add to the count of our 'second' or add
        # our 'second' to the set of possible places to go from 'first' as appropriate
        else:
            if second in markov[first].keys():
                markov[first][second] += 1
            else:
                markov[first][second] = 1

    return markov


def weighted_choice(choices):
    """
    Randomly choose one of the keys in the 'choices' dictionary as weighted by the value it maps to
    :param choices: dictionary mapping keys to their desired relative probabilities. Probabilities can be
        any numbers, all that matters are their relative magnitudes. e.g. (a: 0.5, b: 1) is the same as (a: 1, b: 2)
    :return: the weighted random choice that was made
    """
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    up_to = 0
    for c, w in choices.items():
        if up_to + w > r:
            return c
        up_to += w


def next_pos(current, markov_model):
    """
    Given the current state, determine the next state from the given markov model
    :param current: current state we want to go from
    :param markov_model: the markov model to use
    :return: the next state generated using the markov model
    """
    # If the current state is a 'from' state in the markov model, use it to find the next state
    if current in markov_model.keys():
        choices = markov_model[current]
        return weighted_choice(choices)

    # Otherwise, choose randomly from all the 'to' states in the markov model
    else:
        possible_to = set([])
        for choices in markov_model.values():
            for choice in choices.keys():
                possible_to.add(choice)

        return random.choice(list(possible_to))


def generate_sentence_structure(markov):
    """
    From the given markov model, generate a sentence structure that starts with the 'START' state
    and ends with 'END'
    :param markov:
    :return:
    """
    constructed = ['START']
    next_part = next_pos('START', markov)
    while next_part != 'END':
        constructed.append(next_part)
        next_part = next_pos(next_part, markov)

    constructed.append('END')
    return constructed


def generate(mode):
    """
    Generate text using a first-order markov chain. Requires pages and back_n_days are correct in the config.py
    :return: The text generated
    """
    # Get config settings
    pages_to_parse = config.pages
    back_n_days = config.back_n_days

    # Get all the facebook posts
    posts = fb.get_page_posts(pages_to_parse, back_n_days)

    # Convert the mapping of the posts into a single list of the posts themselves
    posts_text = []
    for page_posts in posts.values():
        posts_text += page_posts

    # Map the POS to words to choose from for the text generation
    pos_dict = pos.map_pos_to_words(posts_text)

    # Construct a Markov chain with the posts
    markov = {}
    for post in posts_text:
        if mode == 'pos':
            post_structure = pos.convert_string_to_structure(post)
        elif mode == 'words':
            post_structure = TextBlob(post).tokens
            post_structure.insert(0, 'START')
            post_structure.append('END')
        else:
            post_structure = ['START', 'END']
        markov = construct_first_order_markov(markov, post_structure)

    # Generate post's structure
    structure = generate_sentence_structure(markov)

    # Finally, generate the post text itself
    post = ""
    idx = 1
    while structure[idx] != 'END':
        tag = structure[idx]
        if tag == 'POS':
            post += "'"
        elif tag in pos_dict:
            post += random.choice(pos_dict[tag]) + " "
        else:
            post += tag + " "

        idx += 1

    return post
