"""
Main portion of the Fried Rice content creation/posting
"""

import sys

import config
import facebook_helpers as fb
import generators.markov
import generators.replace

__author__ = 'github.com/samshadwell'


def main():
    # """
    # Generates a random post and prompts user to ask if they want to post it to their page.
    # :return: None. Posts generated post to page if requested, otherwise does nothing
    # """

    if config.generator == "markov":
        post = generators.markov.generate(config.markov_type)
    elif config.generator == "replace":
        post = generators.replace.generate()
    else:
        print("Invalid generator set in config.py")
        return

    # See if the user wants to post to Facebook, and post if they do
    print("Generated post: ")
    print(post)
    response = input("Would you like to post to page? (y/n): ")
    if response.lower() == 'y' or response.lower() == 'yes':
        fb.post_to_page(post)


if __name__ == '__main__':
    sys.exit(main())
