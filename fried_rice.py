"""
Main portion of the Fried Rice content creation/posting
"""

import sys
import config
import random

import facebook_helpers as fb
import tagging_helpers as pos

__author__ = 'github.com/samshadwell'

def main():
    """
    Generates a scrambled post and prompts user to ask if they want to post it to their page.
    :return: None. Posts generated post to page if requested, otherwise does nothing
    """
    # Get config settings
    pages_to_parse = config.pages
    back_n_days = config.back_n_days
    p_swap = config.p_swap

    # Get all the facebook posts, as well as the longest post
    posts = fb.get_page_posts(pages_to_parse, back_n_days)
    longest = fb.get_longest_post(posts)

    # Convert the mapping of the posts into a single list of the posts themselves
    posts_text = []
    for page_posts in posts.values():
        posts_text += page_posts

    # Map the POS to words to choose from for the text generation
    pos_dict = pos.map_pos_to_words(posts_text)

    # Go through the longest post, and swap out words in it
    scrambled = ""
    for word, tag in pos.get_string_tags(longest[1]):
        # Randomly decide to swap out this word.
        rand = random.random()
        # If swapping, randomly choose a word with the same tag
        if rand < p_swap:
            scrambled += random.choice(pos_dict[tag]) + ' '
        # Otherwise, append the word and move on
        else:
            scrambled += word + ' '

    # See if the user wants to post to Facebook, and post if they do
    print("Generated post: ")
    print(scrambled)
    print()
    response = input("Would you like to post to page? (y/n): ")
    if response.lower() == 'y' or response.lower() == 'yes':
        fb.post_to_page(scrambled)

if __name__ == '__main__':
    sys.exit(main())
