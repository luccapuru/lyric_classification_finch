from nltk.stem import RSLPStemmer
from nltk.tokenize import TweetTokenizer
import numpy as np
import pandas as pd   
import pickle
import codecs
import string

def extract_features(text):
    with codecs.open('data/stopwords.txt', encoding="utf-8") as file:
        stop_words = file.readlines()
    stop_words = [word.strip() for word in stop_words]
    
    df_bow = pd.read_csv("bag_of_words.csv",sep=";")
        
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,reduce_len=True)
    tokens = tokenizer.tokenize(text)
    stemmer_pt = RSLPStemmer()
    tokens_without_sw = [stemmer_pt.stem(word) for word in tokens if not word in stop_words and not word in string.punctuation]
    dct = dict(zip(df_bow.columns, [0]*len(df_bow.columns)))
    for token in tokens_without_sw:
        if token in df_bow.columns:
            #print(token)
            #print(dct[token])
            dct[token] += 1
    return np.array(list(dct.values()))

def make_prediction(model, text):
    x = extract_features(text)
    class_model = model.predict(x.reshape(1, -1))[0]
    
    dct_classes = {0:["Bossa Nova"], 1:["Funk"], 2:["Gospel"],3:["Sertanejo"]}

    return dct_classes[class_model][0]

def open_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    return model