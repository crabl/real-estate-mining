from sklearn.feature_extraction.text import TfidfVectorizer
from extractor import extract_descriptions
import numpy as np
from collections import defaultdict

vectorizer = TfidfVectorizer(ngram_range=(1,2))

# - [x] Read the CSV file
# - [x] From every row, extract Description into a corpus list
# - [x] From every row, extract target attribute (selling price, etc) into a list
descriptions = extract_descriptions('listings.csv')

# - [x] Create stemmed n-grams from words
# - [x] Vectorize n-gram counts
counts = vectorizer.fit_transform(descriptions.corpus).toarray()

# - [ ] Keep a max. of top n-attrs according to term frequency
indices = np.argsort(vectorizer.idf_)[::-1]
features = vectorizer.get_feature_names()
top_n = 200
top_features = [features[i] for i in indices[:top_n]]
print top_features


# - [ ] Transform n-gram vectors into tfi-idf scores



# - [ ] Create a vocabulary of n-grams used for analysis
# - [ ] Create a dataset with Numpy containing the data: n-gram tf-idf scores, and the numerical target vars
