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

    lemmatised_output = []
    for word, tag in tagged_tokens:
        wordnet_tag = get_wordnet_pos(tag)
        lemmatised_output.append(lemmatiser.lemmatize(word, wordnet_tag))

    return lemmatised_output

def run_pipeline(raw_text: str) -> List[str]:
    tokens = custom_tokenise(raw_text)
    print(f"1. Tokenised:{tokens}")

    filtered = remove_stopwords(tokens)
    print(f"2. Stopwords removed:{filtered}")

    lemmas = lemmatise_tokens(filtered)
    print(f"3. Lemmatised:{lemmas}")

    return lemmas

if __name__ == "__main__":
    raw_text = (
        "The intensive-care patients are recovering surprisingly quickly. "
        "Doctors are analyzing data daily!"
    )
    print(f"0. Raw text: {raw_text!r}")
    run_pipeline(raw_text)
