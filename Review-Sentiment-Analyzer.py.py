import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.data.path.append('C:\\Users\\SAM-Tech\\AppData\\Roaming\\nltk_data')
data = pd.read_csv('Restaurant_Reviews.tsv',sep='\t')
data['word_count'] = data['Review'].apply(lambda x : len(str(x).split()))
print(data.shape)
print(data.isnull().sum())
data['char_count'] = data['Review'].apply(len)
print(data['Liked'].value_counts())
# data['Liked'].plot(kind='hist', bins=20,title='Liked')
# plt.gca().spines[['top','right']].set_visible(False)
# plt.show()
data['sent_count'] = data['Review'].apply(lambda x:len(nltk.sent_tokenize(str(x))))
print(data.head())
print(data[data['Liked']==1]['char_count'].mean())
print(data[data['Liked']==0]['char_count'].mean())
#Stemming the data
def stem(text):
    text = re.sub('[^a-zA-Z]',' ',text)
    text = text.lower()
    text = text.split()
    custom_stopwords = {'don',"dont't" , 'ain','aren','couldn',"aren't","couldn't", 'didn',"didn't",'doesn',"doesn't","hadn","hadn't",'hasn',"hasn't",'haven',"haven't","isn","isn't","ma","mightn","mightn't","mustn","mustn't","needn","needn't","shan","shan't","no","nor","not","shouldn","shouldn't","wasn","wasn't",'weren',"weren't","won","won't","wouldn","wouldn't"}
    all_stopwords = set(stopwords.words('english')) - custom_stopwords
    text = [word for word in text if word not in set(all_stopwords)]
    text = ' '.join(text)
    return text
data['stemmed_text'] = data["Review"].apply(stem)
print(data.head())
wc = WordCloud(width=500,height=500,min_font_size=8,background_color='white')
pos = wc.generate(data[data['Liked']==1]['stemmed_text'].str.cat(sep=" "))
plt.imshow(pos)
plt.axis("off") 
plt.tight_layout()
plt.show() 

