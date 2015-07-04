# FriedRice
Python script behind the Facebook page https://www.facebook.com/FriedRiceNews

Script crawls the Facebook pages specified in config.py and gets their posts (from the last n days as specified in config.py). Then runs part of speech tagging on those posts and randomly swaps out text for other text of the same tag.

I made this because I was tired of being asked to like random Rice University Facebook pages, so I wanted to humorously combine all the content from those pages onto this one.

This project is not associated with Rice University in any official context.

# Setup
If you want to use this on your own, you'll have to make a file entitle "credentials.py" in the same folder that declares the variable "page_access_token" with the access token for your own page. You can then play around with the pages that are crawled, number of days to go back, and the probability of swapping any individual word out by editing the config.py file.
