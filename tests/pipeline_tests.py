import unittest
from pipeline import custom_tokenize, remove_stopwords, lemmatize_tokens


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
        # Testing that 'recovering' successfully morphs to 'recover'
        tokens = ["patients", "recovering"]
        expected = ["patient", "recover"]
        self.assertEqual(lemmatize_tokens(tokens), expected)

if __name__ == '__main__':
    unittest.main()
