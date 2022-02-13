#!/usr/bin/env python
# coding: utf-8

# ## Setup

# In[1]:


# packages
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd

# data filename
filename = 'Musical_instruments_reviews.csv'


# ## Functions

# In[2]:


# function to read-in Amazon musical instruments dataset summary column and format it into a single string
def get_data(filename, cols_to_import):
    data = pd.read_csv(filename,usecols=cols_to_import)
    data = list(data.iloc[:,0].values)
    data = ' '.join(data)
    return data

# function to tokenize a dataset
def get_tokens(stem):
    tokens = nltk.word_tokenize(stem)
    return tokens

# function to stem a tokenized dataset
def execute_stemming(filtered, stem_type):
    stemmed = []
    for f in filtered:
        if stem_type == 'porter':
            stemmed.append(PorterStemmer().stem(f))
        elif stem_type == 'lancaster':
            stemmed.append(LancasterStemmer().stem(f))
        elif stem_type == 'snowball':
            stemmed.append(SnowballStemmer('english').stem(f))
    return stemmed

def execute_lemma(filtered, lemmatizer_obj):
    lemmize = []
    for f in filtered:
        lemmize.append(lmtzr.lemmatize(f,'v'))
    return lemmize

def create_output(tokens, reduced_tokens):
    result = dict(zip(tokens, reduced_tokens))
    return result


# ## Code Execution

# In[3]:


# load summary column of amazon dataset
data = get_data(filename,['summary'])

# get tokens from amazon dataset
tokens = get_tokens(data)

# perform stemming of tokens
stemmed_tokens = execute_stemming(tokens,'snowball')
stemmed_result = create_output(tokens, stemmed_tokens)

# perform lemmatization of tokens
lmtzr = WordNetLemmatizer()
lemma_tokens = execute_lemma(tokens, lmtzr)
lemma_result = create_output(tokens, lemma_tokens)

# output results
print('Stemmed Results:')
print(stemmed_result)
print()
print('Lemmatized Results:')
print(lemma_result)


# In[ ]:




