from textblob import TextBlob
import preprocessor as p
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
with open('sentimentcorpus.txt') as f:
    for i in f:
		try:
			text=i.split('\t')[2].lower()
			text=text.replace('#', '')
			p.set_options(p.OPT.URL, p.OPT.MENTION)
			text=p.clean(text)		
			blob = TextBlob(text)	
			blob=blob.correct()
			print(blob)
			polarity=0
			num=len(blob.sentences)		
			for sentence in blob.sentences:
				polarity+=sentence.sentiment.polarity
			print(float(polarity)/float(num))
		except Exception:
			print(sys.exc_info()[0])
			
