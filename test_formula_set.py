import unittest
import formula_set as fs

class TestBasics(unittest.TestCase):
    def test_basic(self):
        formula_set = fs.Formula_set()
        formula_set.add_formula(["b - 26 = 4 * 3 + 6 * 2", "c = b + 2", "a = c + b", "d = 3"])
        self.assertEqual(formula_set.see('b'), 50)
        
    def test_add_var(self):
        formula_set = fs.Formula_set()
        formula_set.add_formula(["a + b = 2"])
        formula_set.add_variable([("a", 2)])
        self.assertEqual(formula_set.see('a'), 2)
        self.assertEqual(formula_set.see('b'), 0)
    
    def test_two_var(self):
        formula_set = fs.Formula_set()
        formula_set.add_formula(["a + b = 3", "a - b = 1"])
        self.assertEqual(formula_set.see('a'), 2)
        self.assertEqual(formula_set.see('b'), 1)