from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from extractor import extract_descriptions


bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
analyze = bigram_vectorizer.build_analyzer()

descriptions = extract_descriptions('listings.csv')
counts = bigram_vectorizer.fit_transform(descriptions.corpus).toarray()
transformer = TfidfTransformer()

weighted = transformer.fit_transform(counts)
print weighted.toarray()[0][20]
