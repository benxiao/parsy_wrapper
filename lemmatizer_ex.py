from nltk.stem import WordNetLemmatizer
import time
wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('dogs'))



start = time.time()
for i in range(10000):
    print(wordnet_lemmatizer.lemmatize('black_holes'))
print(time.time()-start)
