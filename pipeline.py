import re
from typing import List

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import pos_tag

# Ensure morphological corpora are available (usually handled in environment setup)
# nltk.download('punkt', quiet=True)
# nltk.download('averaged_perceptron_tagger', quiet=True)
# nltk.download('wordnet', quiet=True)

def custom_tokenize(text: str) -> List[str]:
    """
    Binds hyphenated clinical jargon (e.g., 'intensive-care') as single semantic entities[cite: 1].
    """
    text_lower = text.lower()
    pattern = r'\b[a-z0-9]+(?:-[a-z0-9]+)*\b'
    return re.findall(pattern, text_lower)

def remove_stopwords(token_list: List[str]) -> List[str]:
    """
    Strips high-frequency structural stopwords using hash table lookup[cite: 1].
    """
    custom_stopwords = {"the", "are", "is", "in", "and", "of", "to", "a"}
    return [token for token in token_list if token not in custom_stopwords]

def get_wordnet_pos(treebank_tag: str) -> str:
    """
    Maps complex Penn Treebank POS tags to WordNet morphological constants[cite: 1].
    """
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('R'):
        return wn.ADV
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    return wn.NOUN

def lemmatize_tokens(token_list: List[str]) -> List[str]:
    """
    Context-aware lemmatizer that maps tokens to base linguistic lemmas using POS tags[cite: 1].
    """
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = pos_tag(token_list)

    lemmatized_output = []
    for word, tag in tagged_tokens:
        wordnet_tag = get_wordnet_pos(tag)
        lemmatized_output.append(lemmatizer.lemmatize(word, wordnet_tag))

    return lemmatized_output
