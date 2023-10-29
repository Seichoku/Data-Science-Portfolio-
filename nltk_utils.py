import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

# Create an Instance of PorterStemmer
 
stemmer = PorterStemmer()

def tokenize(sentence):
    """
    split sentence into an array of words or
    token
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    steming = finding the root form of the word 
    """
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """

    # stem each word 
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
    