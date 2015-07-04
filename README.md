# FriedRice
Python script behind the Facebook page https://www.facebook.com/FriedRiceNews

This script gets posts from a set of Facebook pages as defined in config.py, and has a couple of techniques to generate posts based upon the posts found on the pages. Right now can either generate a post using a 1st-order markov model, or by substituting parts of speech in an existing post.

I made this because I was tired of being asked to like random Rice University Facebook pages, so I wanted to humorously combine all the content from those pages onto this one.

This project is not associated with Rice University in any official context.

# Setup
If you want to use this on your own, you'll have to make a file entitle "credentials.py" in the same folder that declares the variable "page_access_token" with the access token for your own page. You can then play around with the pages that are crawled, number of days to go back, and the probability of swapping any individual word out by editing the config.py file.

# Required Packages
This project requires both facebook-sdk (https://github.com/pythonforfacebook/facebook-sdk) and TextBlob (https://textblob.readthedocs.org/en/dev/), and is written in Python 3
