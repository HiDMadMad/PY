import unittest
#from modules.ForHandOutModule import count_char

def count_char(s, c):
    founded = 0
    for this_char in s:
        if this_char == c:
            founded+=1
    return founded

class AnyName(unittest.TestCase):
    # the name of functions must be start with 'test_'
    def test_simple(self):
        s = "anything"
        c = 'n'
        self.assertEqual(count_char(s, c), 2)

    def test_nothing(self):
        s = ""
        c = 'x'
        self.assertEqual(count_char(s, c), 0)
    
    def test_longer(self):
        s = "any any any any even anything"
        c = 'n'
        self.assertEqual(count_char(s, c), 7)

    def test_not_exist(self):
        s = "anything"
        c = 'm'
        self.assertEqual(count_char(s, c), 0)

    def test_all(self):
        s = "nnnnnnnnnnnn"
        c = 'n'
        self.assertEqual(count_char(s, c), 12)

if __name__ == "__main__":
    unittest.main()
#MadMad_40