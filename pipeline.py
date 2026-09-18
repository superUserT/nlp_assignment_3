import re
from typing import List

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import pos_tag

def custom_tokenise(text: str) -> List[str]:
    text_lower = text.lower()
    match_single_hyphen = r'\b[a-z0-9]+(?:-[a-z0-9]+)*\b'
    return re.findall(match_single_hyphen, text_lower)

def remove_stopwords(token_list: List[str]) -> List[str]:
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

def lemmatise_tokens(token_list: List[str]) -> List[str]:
    lemmatiser = WordNetLemmatizer()
    tagged_tokens = pos_tag(token_list)

    lemmatized_output = []
    for word, tag in tagged_tokens:
        wordnet_tag = get_wordnet_pos(tag)
        lemmatized_output.append(lemmatiser.lemmatize(word, wordnet_tag))

    return lemmatized_output
