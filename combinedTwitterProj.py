import json
import textblob as tb
import matplotlib.pyplot as plot
import wordcloud as wc
#pull tweet data out of json file
tweetFile = open('tweets_small.json', 'r')
tweetData = json.load(tweetFile)
tweetFile.close()
#empyt lists
polarity=[]
subjectivity=[]
sumP=0.0
sumS=0.0
tweetString=""
filteredWords={}
commonWords=["I", "in", "if", "and", "and", "or", 'but', 'wow', 'the', 'about', 'http']
#push into tb system and variables
for i in tweetData:
    tB = tb.TextBlob(i["text"])
    polarity.append(tB.polarity)
    sumP+=tB.polarity
    subjectivity.append(tB.subjectivity)
    sumS+=tB.subjectivity
    tweetString+=i["text"]
tBstring=tb.TextBlob(tweetString)
tBlist=tBstring.words
#makes word frequency .word_counts[word], .count(), .words makes list
for x in tBlist:
    if x not in commonWords:
        if len(x)>3:
            if x not in filteredWords.keys():
                filteredWords[x]=tBlist.count(x)
#print(filteredWords)
        #find avgs
#avgp=sumP/len(polarity)
#avgs=sumS/len(subjectivity)
#print("Polarity average: ", avgp)
#print("Subjectivity average: ", avgs)

        #make histogram
        #plot.hist(whole data set, bin, color)
#plot.hist(polarity, bins = [-1, -.35, .35, 1], color = "blue")
        #make title
#plot.title("Polarity Plot")
#plot.xlabel("Polarity")
#plot.ylabel("Amount")
        #print histogram .show
#plot.show()
        #subjectivity histogram
#plot.hist(subjectivity, bins = [0, .30, .65, 1], color = "green")
#plot.title("Subjectivity Plot")
#plot.xlabel("Subjectivity")
#plot.ylabel("Amount")
#plot.show()

        #scatter plot: scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
#plot.scatter(subjectivity, polarity, color="lightpink")
#plot.title("Scatter Plot")
#plot.xlabel("Subjectivity")
#plot.ylabel("Polarity")
#plot.show()
