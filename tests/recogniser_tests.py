import unittest
from nfsa_recognizer import compile_sheeptalk_nfsa, nd_recognize
from clinical_pipeline import custom_tokenize, remove_stopwords, lemmatize_tokens

class TestNFSARecognizer(unittest.TestCase):

    def setUp(self):
        # Instantiate the machine once before tests run
        self.machine = compile_sheeptalk_nfsa()

    def test_dfs_accepts_valid_string(self):
        self.assertTrue(nd_recognize("baa!", self.machine, strategy="DFS"))

    def test_bfs_accepts_valid_string(self):
        self.assertTrue(nd_recognize("baaaa!", self.machine, strategy="BFS"))

    def test_rejects_invalid_strings(self):
        self.assertFalse(nd_recognize("ba!", self.machine, strategy="DFS"))
        self.assertFalse(nd_recognize("xyz", self.machine, strategy="BFS"))

if __name__ == '__main__':
    unittest.main()
