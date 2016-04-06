import unittest
from findingOcurrences import findingOcurrences


__author__ = 'josebermudez'


class TestFindingOcurrences(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFindingOcurrences, self).__init__(*args, **kwargs)

    def test_textToSearch_none(self):
        textToSearch = None
        subtext = 'hola'
        self.assertRaises(ValueError, findingOcurrences, textToSearch=textToSearch, subtext=subtext)

    def test_subtext_none(self):
        textToSearch = 'hola'
        subtext = None
        self.assertRaises(ValueError, findingOcurrences, textToSearch=textToSearch, subtext=subtext)

    def test_hola(self):
        textToSearch = 'Hola holita hola hhola'
        subtext = 'hola'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = [1, 13, 19]
        self.assertListEqual(out, expected_response)

    def test_example1(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'Peter'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = [1, 20, 75]
        self.assertListEqual(out, expected_response)

    def test_example2(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'peter'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = [1, 20, 75]
        self.assertListEqual(out, expected_response)

    def test_example3(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'pick'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = [30, 58]
        self.assertListEqual(out, expected_response)

    def test_example4(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'pi'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = [30, 37, 43, 51, 58]
        self.assertListEqual(out, expected_response)

    def test_example5(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'z'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = []
        self.assertListEqual(out, expected_response)

    def test_example6(self):
        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'Peterz'
        out = findingOcurrences(textToSearch=textToSearch, subtext=subtext)
        expected_response = []
        self.assertListEqual(out, expected_response)
