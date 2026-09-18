import unittest
from pipeline import custom_tokenize, get_wordnet_pos, lemmatize_tokens, remove_stopwords


class TestClinicalPipeline(unittest.TestCase):

    def test_custom_tokenize_preserves_hyphens(self):
        raw_text = "The intensive-care patients."
        expected = ["the", "intensive-care", "patients"]
        self.assertEqual(custom_tokenize(raw_text), expected)

    def test_remove_stopwords(self):
        tokens = ["the", "intensive-care", "patients", "are", "recovering"]
        expected = ["intensive-care", "patients", "recovering"]
        self.assertEqual(remove_stopwords(tokens), expected)

    def test_lemmatize_inflectional_verbs(self):
        tokens = ["patients", "recovering"]
        expected = ["patient", "recover"]
        self.assertEqual(lemmatize_tokens(tokens), expected)
    def test_tokenize_lowercases_and_strips_punctuation(self):
        self.assertEqual(
            custom_tokenize("Doctors are analyzing data daily!"),
            ["doctors", "are", "analyzing", "data", "daily"],
        )

    def test_tokenize_multi_part_hyphenation(self):
        self.assertEqual(custom_tokenize("Well-known state-of-the-art"),
                         ["well-known", "state-of-the-art"])

    def test_tokenize_empty_and_punctuation_only(self):
        self.assertEqual(custom_tokenize(""), [])
        self.assertEqual(custom_tokenize("!?.,"), [])

    def test_tokenize_keeps_digits(self):
        self.assertEqual(custom_tokenize("Ward 4b, bed 12."), ["ward", "4b", "bed", "12"])

    def test_remove_stopwords_empty_and_all_stopwords(self):
        self.assertEqual(remove_stopwords([]), [])
        self.assertEqual(remove_stopwords(["the", "are", "is", "in", "and"]), [])

    def test_remove_stopwords_preserves_order_and_duplicates(self):
        self.assertEqual(remove_stopwords(["data", "the", "data"]), ["data", "data"])

    def test_remove_stopwords_does_not_mutate_input(self):
        tokens = ["the", "patients"]
        remove_stopwords(tokens)
        self.assertEqual(tokens, ["the", "patients"])

    def test_get_wordnet_pos_mapping(self):
        from nltk.corpus import wordnet as wn
        self.assertEqual(get_wordnet_pos("JJ"), wn.ADJ)
        self.assertEqual(get_wordnet_pos("VBG"), wn.VERB)
        self.assertEqual(get_wordnet_pos("RB"), wn.ADV)
        self.assertEqual(get_wordnet_pos("NNS"), wn.NOUN)
        self.assertEqual(get_wordnet_pos("DT"), wn.NOUN)  # unknown tags default to noun

    def test_lemmatize_empty(self):
        self.assertEqual(lemmatize_tokens([]), [])

    def test_lemmatize_preserves_length(self):
        tokens = ["doctors", "analyzing", "data", "daily"]
        self.assertEqual(len(lemmatize_tokens(tokens)), len(tokens))

    def test_full_pipeline_on_target_snippet(self):
        raw = ("The intensive-care patients are recovering surprisingly quickly. "
               "Doctors are analyzing data daily!")
        tokens = custom_tokenize(raw)
        filtered = remove_stopwords(tokens)
        self.assertNotIn("the", filtered)
        self.assertIn("intensive-care", filtered)
        lemmas = lemmatize_tokens(filtered)
        self.assertIn("patient", lemmas)
        self.assertIn("recover", lemmas)
        self.assertIn("doctor", lemmas)


if __name__ == '__main__':
    unittest.main()
