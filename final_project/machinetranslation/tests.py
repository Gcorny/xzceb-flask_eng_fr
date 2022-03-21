import unittest
from translator import englishtoFrench, frenchToEnglish
class testEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtoFrench("How are you ?"), "Comment es-tu?")
        self.assertEqual(englishtoFrench("Who are you?"), "Qui êtes-vous?")

class testFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Comment es-tu?"), "How are you?")
        self.assertEqual(frenchToEnglish("Qui êtes-vous?"), "Who are you?")


unittest.main()