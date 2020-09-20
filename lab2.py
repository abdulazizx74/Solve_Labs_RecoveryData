#!/usr/bin/env python
# coding: utf-8

# In[77]:


pip install nltk


# In[17]:


import nltk


# # Do you remember what do we mean by tokenization? 
# Cut the sentences into multiple words

# In[2]:


nltk.download('punkt')


# # 2. Tokenization in NLTK , Page2

# In[9]:


text="welcome readers. I hope u find it intresting. please do reply"


# In[7]:


from nltk.tokenize import sent_tokenize
text1="welcome readers. I hope u find it intresting. please do reply"
sent_tokenize(text1)

# Page3 Part1
# How many sentence you had? 
# 3Sentences
# How many sentence will we have if we replace full stop “.” With “,” in text? 2 sentences


# In[8]:


import nltk
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
t="Hello everyone. Hope all are fine and doing well. Hope you find the book interesting."
sent_tokenize(t)
#Page3 Part2


# # Exercise 2: Try to tokenize this sentence:
# ## Page4

# In[31]:


import nltk
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
arabic_text="مرحبا بكم. نحن نتعلم اساسيات مبادئ استرجاع المعلومات."
sent_tokenize(arabic_text)
#Page4 


# In[10]:


#هنا اقسم الجمله الى كل كلمه لحالها 
import nltk
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
arabic_text=nltk.word_tokenize("مرحبا بكم. نحن نتعلم اساسيات مبادئ استرجاع المعلومات.")
print(arabic_text)
#Page4


# # Exercise 3: Try to tokenize a given sentence from user into words. Use input() function to enter a text from keyboard. 

# In[11]:


import nltk
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
arabic_text=nltk.word_tokenize(input())
print(arabic_text)
#Page5 input text


# # Exercise 4: Modify the regular expression at step 3 above to find email address. 

# In[16]:


from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("\S+@+\S+") #هنا اطلع صيغه الايميل 
tokenizer.tokenize("Don't hesitate to ask questions or send to me your question to mohsarem@gmail.com") 
# page5


# In[12]:


from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w]+") # هنا عشان اجيب كلمات فقط 
tokenizer.tokenize("Don't hesitate to ask questions or send to me your question to mohsarem@gmail.com") 
# page5


# In[23]:


text=[" It is a pleasant evening.","Guests, who camefrom US arrived at the venue","Food was tasty."]
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc) for doc in text]
print(tokenized_docs) 
import re
import string
x=re.compile('[%s]' % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review:
        new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    tokenized_docs_no_punctuation.append(new_review)
print(tokenized_docs_no_punctuation)


# # Exercise 5. What is the role of re.compile(),re.escape() functions?

# In[21]:


help(re.compile)


# In[24]:


help(re.escape)


# ## Exercise 6. Apply lower () function and upper() functionon the sentence 
# ## below:Text= ‘NLTK allows you to convert Text into Lowercase and uppercase’ 

# In[25]:


A1="NLTK allows you to convert Text into Lowercase and uppercase. Don't hesitate to ask questions"
print(A1.lower())
print(A1.upper())


# In[26]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
words=["Don't",'hesitate','to','ask','questions']
[words for words in words if words not in stops]


# # Exercise 7.

# In[9]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stops=set(stopwords.words('english'))
text = "NLTK allows you to convert Text into Lowercase and uppercase. Don't hesitate to ask questions"
text_tokens = word_tokenize(text)
[text_tokens for text_tokens in text_tokens  if text_tokens not in stops]
#EX7 Page7


# # Exercise 8. Given a text in directory, demonstrate how touse NLTK to treat its content. 

# In[86]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stops=set(stopwords.words('english'))
file_content = open(r"C:\Users\RaKaN\Desktop\rakan.txt").read().lower() # we use lower() to convert letters small to diffine
text_tokens = word_tokenize(file_content)
[text_tokens for text_tokens in text_tokens  if text_tokens not in stops]


# In[67]:


print(stopwords.words('english'))
print(stopwords.words('arabic'))


# In[27]:


A1="NLTK allows you to convert Text into Lowercase and uppercase. Don't hesitate to ask questions"
print(A1[0].lower())
print(A1[0].upper())


# In[ ]:




