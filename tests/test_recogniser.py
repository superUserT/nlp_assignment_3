import unittest
from nd_recognise import NFSA, compile_sheeptalk_nfsa, nd_recognize

class TestNFSARecognizer(unittest.TestCase):

    def setUp(self):
        self.machine = compile_sheeptalk_nfsa()

    def test_dfs_accepts_valid_string(self):
        self.assertTrue(nd_recognize("baa!", self.machine, strategy="DFS"))

    def test_bfs_accepts_valid_string(self):
        self.assertTrue(nd_recognize("baaaa!", self.machine, strategy="BFS"))

    def test_rejects_invalid_strings(self):
        self.assertFalse(nd_recognize("ba!", self.machine, strategy="DFS"))
        self.assertFalse(nd_recognize("xyz", self.machine, strategy="BFS"))

    def test_strategies_agree_on_many_inputs(self):
        cases = {
            "baa!": True, "baaa!": True, "baaaaaa!": True,
            "": False, "b": False, "ba": False, "baa": False, "baa!!": False,
            "baa!a": False, "aa!": False, "!": False, "bab!": False,
            "BAA!": False,
        }
        for tape, expected in cases.items():
            for strategy in ("DFS", "BFS"):
                with self.subTest(tape=tape, strategy=strategy):
                    self.assertEqual(
                        nd_recognize(tape, self.machine, strategy=strategy), expected
                    )

    def test_default_strategy_is_dfs(self):
        self.assertTrue(nd_recognize("baa!", self.machine))

    def test_invalid_strategy_raises(self):
        with self.assertRaises(ValueError):
            nd_recognize("baa!", self.machine, strategy="A*")

    def test_epsilon_transition_is_followed(self):
        machine = NFSA(
            states={0, 1, 2},
            start_state=0,
            accept_states={2},
            transitions={(0, "ε"): [1], (1, "a"): [2]},
        )
        for strategy in ("DFS", "BFS"):
            with self.subTest(strategy=strategy):
                self.assertTrue(nd_recognize("a", machine, strategy=strategy))
                self.assertFalse(nd_recognize("", machine, strategy=strategy))

    def test_empty_tape_accepted_when_start_is_accepting(self):
        machine = NFSA({0}, 0, {0}, {})
        self.assertTrue(nd_recognize("", machine))

    def test_nondeterministic_branch_explores_all_options(self):
        # Only the second branch out of state 0 on 'a' reaches acceptance.
        machine = NFSA(
            states={0, 1, 2},
            start_state=0,
            accept_states={2},
            transitions={(0, "a"): [1, 2]},
        )
        for strategy in ("DFS", "BFS"):
            with self.subTest(strategy=strategy):
                self.assertTrue(nd_recognize("a", machine, strategy=strategy))

    def test_sheeptalk_machine_structure(self):
        self.assertEqual(self.machine.start_state, 0)
        self.assertEqual(self.machine.accept_states, {4})
        self.assertEqual(self.machine.transitions[(2, "a")], [2, 3])

if __name__ == '__main__':
    unittest.main()
