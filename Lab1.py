#!/usr/bin/env python
# coding: utf-8

# # Do you remember how to check python version and
# # installed libraries? Write steps below: 

# In[1]:


import sys
sys.version


# In[6]:


import numpy
numpy.version.version


# In[3]:


pip install gensim


# In[21]:


import gensim as gs
print(gs.__version__)


# # Exercise 2

# #  Tokenize the following sentence and write down the result you obtain! 

# In[2]:


text= "Tokenization is the process of breaking down text document apart into those pieces"


# In[16]:


tokenizedWord=list(gs.utils.tokenize(text))
print(tokenizedWord)
#الفايدة من الكود هو تقطيع الجمله كامله الى كلمات متعدده 


# In[20]:


help(gs.utils.tokenize)


# # Exercise 3

# In[24]:


Sentence= "In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Computer science defines AI research as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfullyachieving its goals." 


# # What do you see? Page9

# In[3]:


from gensim import corpora
from pprint import pprint
text = [""" In computer science, artificial intelligence (AI), sometimes called machine intelligence, 
is intelligence demonstrated by machines, in contrast to the natural intelligence displayed 
by humans and animals. Computer science defines AI research as the study of intelligent agents:
any device that perceives its environment and takes actions that maximize its chance 
of successfullyachieving its goals."""]
tokens = [[token for token in sentence.split()] for sentence
in text]
gensim_dictionary = corpora.Dictionary()
gensim_corpus = [gensim_dictionary.doc2bow(token,
allow_update=True) for token in tokens]
print(gensim_corpus)


# In[4]:


word_frequencies= [[(gensim_dictionary[id], frequence) for id, frequence in couple] for couple in gensim_corpus]
print(word_frequencies)


# # Home exercise:
# # Create a bag of words corpus by reading a text file. 

# In[9]:


from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
tokens = [simple_preprocess(sentence, deacc=True) for sentence in open(r"C:\Users\RaKaN\Desktop\rakan.txt", encoding='utf-8')]
gensim_dictionary = corpora.Dictionary()
gensim_corpus = [gensim_dictionary.doc2bow(token, allow_update=True) for token in tokens]
word_frequencies = [[(gensim_dictionary[id], frequence) for id, frequence in couple] for couple in gensim_corpus]
print(word_frequencies)

