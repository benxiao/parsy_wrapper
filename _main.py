from mcparface import *
from nltk.stem import WordNetLemmatizer
NOUNTYPES = ['NNP','NNS','NN','NNS']

lemmatizer = WordNetLemmatizer()
result = pos_tag(EXAMPLE)
print(result)
print([lemmatizer.lemmatize(w) for w, t in result if t in NOUNTYPES])


