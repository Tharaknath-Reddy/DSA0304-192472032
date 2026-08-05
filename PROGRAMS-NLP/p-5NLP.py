from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "running", "studies", "cats", "better"]

# Display original and stemmed words
print("Original Word -> Stemmed Word")
for word in words:
    print(word, "->", ps.stem(word))