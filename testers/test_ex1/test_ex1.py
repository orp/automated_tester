import unittest
import logging
import sys
import functools 
import ex1

#~ scores = dict()
#~ def with_score(score):
    #~ def wrap(func):
        #~ scores[func.__name__] = score
        #~ return func
    #~ return wrap

default_penalty = 5
penalties = {"test_fizzbuzz" : 20,
     "test_count_in_str" : 30}
    
class TestEx1(unittest.TestCase):
    def test_radius_1(self):
        "Test that the area of a circle with radius 1 is 3.14"
        self.assertEqual(ex1.circle_area(1),3.14)
    def test_radius_0(self):
        self.assertEqual(ex1.circle_area(0),0)
    def test_radius_10(self):
        self.assertEqual(ex1.circle_area(10),314)

    def test_fizzbuzz(self):
        self.assertEqual(ex1.fizzbuzz(1),1)
        self.assertEqual(ex1.fizzbuzz(8),1 + 2 + 3 + 4 + 6 + 8) #5 and 7 are skipped
        self.assertEqual(ex1.fizzbuzz(35),490)
    
    def test_count_in_str(self):
        self.assertEqual(ex1.count_in_str("a", "abcaabc"),3)
        self.assertEqual(ex1.count_in_str("ab", "abcaabc"),2)
        self.assertEqual(ex1.count_in_str("abx", "abx"),1)
        self.assertEqual(ex1.count_in_str("abx", "ab"),0)
    
    def test_flip_ends(self):
        self.assertEqual(ex1.flip_ends(""),"")
        self.assertEqual(ex1.flip_ends("a"),"a")
        self.assertEqual(ex1.flip_ends("ab"),"ba")
        self.assertEqual(ex1.flip_ends("abc"),"cba")
    
    def test_is_prime(self):
        self.assertEqual(ex1.is_prime(1),False)
        self.assertEqual(ex1.is_prime(2),True)
        self.assertEqual(ex1.is_prime(3),True)
        self.assertEqual(ex1.is_prime(5),True)
        self.assertEqual(ex1.is_prime(9),False)
        self.assertEqual(ex1.is_prime(14),False)
        self.assertEqual(ex1.is_prime(17),True)
    
    def test_sum_primes(self):
        self.assertEqual(ex1.sum_primes(5),5)
        self.assertEqual(ex1.sum_primes(10),17)
        
def load_tests(loader, tests, patten):
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(TestEx1)
    suite.addTests(tests)
    return suite
    
def run_tests(log_file = None):
    runner = unittest.TextTestRunner(stream=sys.stdout)
    loader = unittest.TestLoader()
    suite = load_tests(loader, [], None)
    results = runner.run(suite)
    return results

