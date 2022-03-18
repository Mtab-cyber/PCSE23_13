"""Twitter App using Flask"""
import project
from flask import Flask, request, render_template

app = Flask("app")

@app.route('/')
def home():
  return render_template('Twitter.html')

@app.route('/keyword',methods=['POST','GET'])
def keyword():
  val=request.from["keyword"]
  word=project.keyword.key(val)
  polarity=project.plotting.PolarityAndSubjectivity(word)
  word_cld=project.plotting.show_wordcloud(word['tweets'])
  negative_positive_plot=project.plotting.sentiment(word)
  return render_template('Twitter.html',prediction=word['tweets'].head(),Top_Five_Tweets="Top Five Raw Tweets:",plot=word_cld,Word_cloud="Word Cloud for common words used in the Tweets",plot_polarity=polarity,polatiry_plot="Relationship between Subjectivity and Polarity",plot_sentiment=negative_positive_plot,Sentiment="Count of Positive, Negative and Neutral Tweets")

if __name__ == "app":
    app.run()
