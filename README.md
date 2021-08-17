# Coding-Challenge-Fall2021
ACM Research Challenge

For this challenge I calculated the overall sentiment score of the input text. To make it easier to parse I edited the input.txt file so that each line was a sentence. I was originally going to replace the questions marks and exclamation marks with periods and split off of that. However, as will be discuessed later they were too important. 

The library I used was vaderSentiment. This library has a large dataset that is already included. When you run a sentence through the analyzer it returns a dictionary that contains four keys. Those keys are, positive, neutral, negative, and compound. The compound key is what is used to determine the overall sentiment of the sentence. A compound score greater than or equal to .05 can be considered a positive sentiment. Less than or equal to -.05 is negative and in between is neutral. 

My program reads the input file one line at a time and passes that line into the analyzer. A dictionary with the four keys is produced and the compound score is compared to the scoring mentioned above. Depending on that score, either the positive score, negative score, or neutral score is incremented by one. A total count is also maintaned. Once every line has been read it calculates the total percentage of positive, negative and neutral scores. The highest of the three is the overall sentiment of the text. I also store the individual line scores in a seperate file. 

The final score for this text was a postive sentiment at 48.28%. The negative score ended at roughly 27.59%. And the neutral score ended up at 24.13% This means that overall the sentiment of the text was positive. This was kind of surprising to me given the the first paragraph. I expected it to be pretty neutral in all. 

Need to run pip install vadersentiment to install the required libraries.

Resources:
  Simplifying Sentiment Analysis using VADER in Python (on Social Media Text)  
  https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f

  Sentiment Analysis in Python with TextBlob and VADER Sentiment (also Dash p.6)  
  https://www.youtube.com/watch?v=qTyj2R-wcks
