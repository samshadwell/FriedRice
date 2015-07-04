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
back_n_days = 7

# The probability of swapping any individual word in the original post for another word
p_swap = 0.4
