from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
text = ""
sentences = []
postive_score = 0.0
negative_score = 0.0
neutral_score = 0.0
total_count = 0.0


# Opens input file and determines polarity score
with open("input.txt","r") as f:
    for line in f.read().split('\n'):
        text = analyzer.polarity_scores(line)
        sentences.append(text)
        if text['compound'] >= .05:
            postive_score += 1
        elif text['compound']  <= -.05:
            negative_score +=1
        else:
            neutral_score +=1
        total_count +=1
    f.close()

#Writes individual scores to file. 
with open("sentenceSentiment.txt", "w") as g:
    for sentence in sentences:
        g.write("%s\n" % sentence)
    g.close()

print("Total positve score is {}%".format(postive_score/total_count*100.0))
print("Total negative score is {}%".format(negative_score/total_count*100.0))
print("Total neutral score is {}%".format(neutral_score/total_count*100.0))
        


