import pymongo
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from gensim import corpora
from gensim.models import LdaModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import string


nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["women_cricket"]
collection = db["cricket_articles"]


nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


documents = [doc["headline"] for doc in collection.find({}, {"headline": 1, "_id": 0})]


if not documents:
    raise ValueError("No headlines found in the database.")

def preprocess_text(text):
    """Apply tokenization, stopword removal, lemmatization, and stemming."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))  
    tokens = word_tokenize(text) 
    tokens = [word for word in tokens if word.isalpha()]  
    tokens = [word for word in tokens if word not in stop_words] 
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens] 
    stemmed = [stemmer.stem(word) for word in lemmatized]  
    return stemmed


preprocessed_docs = [preprocess_text(doc) for doc in documents]


filtered_docs = [doc for doc in preprocessed_docs if len(doc) > 0]

if not filtered_docs:
    raise ValueError("Preprocessing removed all terms, leading to an empty corpus.")


def apply_topic_modeling(texts, num_topics=3):
    """Perform LDA topic modeling."""
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
   
    if not any(corpus):
        raise ValueError("Cannot compute LDA over an empty collection (no terms).")
    
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    topics = lda_model.print_topics(num_words=5)
    return topics


def extract_named_entities(text):
    """Extract named entities such as players, tournaments using SpaCy."""
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return entities


def sentiment_analysis(text):
    """Perform sentiment analysis using VADER and TextBlob."""
    analyzer = SentimentIntensityAnalyzer()
    vader_score = analyzer.polarity_scores(text)["compound"]
    textblob_score = TextBlob(text).sentiment.polarity
    return {"VADER": vader_score, "TextBlob": textblob_score}


topics = apply_topic_modeling(filtered_docs)
print("Extracted Topics:", topics)


for i, doc in enumerate(documents):
    print(f"\nDocument {i+1}: {doc}")
    print("Named Entities:", extract_named_entities(doc))
    print("Sentiment Analysis:", sentiment_analysis(doc))
