import unittest
from pipeline import custom_tokenise, get_wordnet_pos, lemmatise_tokens, remove_stopwords


class TestClinicalPipeline(unittest.TestCase):

    def test_custom_tokenise_preserves_hyphens(self):
        raw_text = "The intensive-care patients."
        expected = ["the", "intensive-care", "patients"]
        self.assertEqual(custom_tokenise(raw_text), expected)

    def test_remove_stopwords(self):
        tokens = ["the", "intensive-care", "patients", "are", "recovering"]
        expected = ["intensive-care", "patients", "recovering"]
        self.assertEqual(remove_stopwords(tokens), expected)

    def test_lemmatise_inflectional_verbs(self):
        tokens = ["patients", "recovering"]
        expected = ["patient", "recover"]
        self.assertEqual(lemmatise_tokens(tokens), expected)
    def test_tokenise_lowercases_and_strips_punctuation(self):
        self.assertEqual(
            custom_tokenise("Doctors are analyzing data daily!"),
            ["doctors", "are", "analyzing", "data", "daily"],
        )

    def test_tokenise_multi_part_hyphenation(self):
        self.assertEqual(custom_tokenise("Well-known state-of-the-art"),
                         ["well-known", "state-of-the-art"])

    def test_tokenise_empty_and_punctuation_only(self):
        self.assertEqual(custom_tokenise(""), [])
        self.assertEqual(custom_tokenise("!?.,"), [])

    def test_tokenise_keeps_digits(self):
        self.assertEqual(custom_tokenise("Ward 4b, bed 12."), ["ward", "4b", "bed", "12"])

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
        self.assertEqual(lemmatise_tokens([]), [])

    def test_lemmatize_preserves_length(self):
        tokens = ["doctors", "analyzing", "data", "daily"]
        self.assertEqual(len(lemmatise_tokens(tokens)), len(tokens))

    def test_full_pipeline_on_target_snippet(self):
        raw = ("The intensive-care patients are recovering surprisingly quickly. "
               "Doctors are analyzing data daily!")
        tokens = custom_tokenise(raw)
        filtered = remove_stopwords(tokens)
        self.assertNotIn("the", filtered)
        self.assertIn("intensive-care", filtered)
        lemmas = lemmatise_tokens(filtered)
        self.assertIn("patient", lemmas)
        self.assertIn("recover", lemmas)
        self.assertIn("doctor", lemmas)


if __name__ == '__main__':
    unittest.main()
