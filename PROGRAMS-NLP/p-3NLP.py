import nltk
from nltk.tokenize import word_tokenize

# Download required resources (only the first time)
nltk.download('punkt')
nltk.download('punkt_tab')

# Get input from the user
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

# Display the tokens
print("Tokens are:")
for word in words:
    print(word)