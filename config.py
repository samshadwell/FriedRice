"""
Contains the configuration information for FriedRice

Does not contain the AppID or AppSecret required to run, those are in a separate .py file entitled "credentials.py"
which the user must create themselves using their own AppID/AppSecret from Facebook
"""

__author__ = 'github.com/samshadwell'

# The pages to crawl for their posts. Given is the part of the URL after www.facebook.com
pages = ["diningAtSammys", "ricecampanile", "TheRiceThresher", "ricefarmersmarket", "SustainabilityAtRice",
         "riceuniversitydining", "FEPatRice", "riceprogramcouncil", "RAFStudentInitiative", "R2TheRiceReview",
         "TheRiceStandard", "willyspub", "RiceFutureAlumni", "RiceUniversity", "RiceFYP", "LowreyArboretum"]

# The number of days worth of facebook posts to go back and get (e.g. 7 means get posts from the last week)
# Set to -1 to do for all posts.
back_n_days = -1

# The probability of swapping any individual word in the original post for another word
p_swap = 0.5

# Type of generator to use. Currently supported are "markov" and "replace"
generator = "markov"

# For a markov generator the mode. If 'pos' makes a chain using tagged parts of speech. 'words' uses the words
# themselves
markov_type = 'words'