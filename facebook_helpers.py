"""
Library to help perform the facebook actions

Requires the python facebook-sdk is installed (https://github.com/pythonforfacebook/facebook-sdk)
Also requires a python file entitled 'credentials.py' exists in the same directory with two variables declared in it:
    'page_access_token', the page token that gives this app permission to post to the given page
"""

from datetime import date, timedelta

import facebook

import credentials

__author__ = 'github.com/samshadwell'


def get_page_posts(pages, back_n_days=-1):
    """
    Gets the posts from the given Facebook pages going back the given number of days (or all of them if none specified)
    :param pages: An array of strings that are the pages to get the posts of. Each string is the page URL which appears
        after www.facebook.com when navigating to the page
    :param back_n_days: optional parameter to set the number of days' posts to get. Defaults to all posts. Example, if
        this is specified as 7, will get all posts from the last 7 days.
    :return: dictionary which maps each page string in 'pages' to a list of its post strings
    """

    # App token used to authenticate with Facebook
    token = credentials.page_access_token
    graph = facebook.GraphAPI(access_token=token, version='2.2')

    # Set filter to be since the appropriate number of days if necessary
    if back_n_days != -1:
        cutoff = date.today() - timedelta(days=back_n_days)
        since_filter = '?since=' + str(cutoff)
    else:
        since_filter = ''

    # Array to populate with all posts
    all_posts = {}

    # Go through all the pages and get their posts
    for page in pages:
        graph_id = '/' + page + '/posts' + since_filter
        page_posts = graph.get_object(graph_id)
        all_posts[page] = []
        try:
            # For each post add its message to the array
            for post in page_posts['data']:
                message = post['message']
                all_posts[page].append(message)
        # Failed attempt indicates we have run out of pages, print message and go to next one
        except KeyError:
            print("Error getting post from " + page + ". Continuing")
            continue

    return all_posts


def get_longest_post(all_posts):
    """
    Get a tuple with information on the post with the most words from all posts in the given dictionary
    :param all_posts: a dictionary mapping page names to lists of posts
    :return: a tuple whose 0th element is the page from which the longest post came, and whose 1st element is the text
        of the longest post itself
    """
    longest_len = -1
    longest = ('None', 'None')
    # Go through all pages
    for page in all_posts.keys():
        # Go through all posts for the given page, check to see if it has more words than the previous 'longest'
        for post in all_posts[page]:
            num_words = len(post.split())
            if num_words > longest_len:
                longest = (page, post)
                longest_len = num_words

    return longest


def post_to_page(string):
    """
    Posts the given string to the facebook page for which permission is granted in credentials
    :param string:
    :return:
    """

    # Set up Facebook Graph API connection
    token = credentials.page_access_token
    graph = facebook.GraphAPI(access_token=token, version='2.2')

    # Post string to page's feed as the page
    graph.put_object(parent_object='me', connection_name='feed', message=string)

    return
