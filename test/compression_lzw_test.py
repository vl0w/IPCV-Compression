import lzw
from unittest import TestCase


class TestEncodeLZW(TestCase):
    def test_encode(self):
        self.assertEqual([1, 4, 3, 2, 6, 8], lzw.encode("aaacbcbcbc"))


    def test_encode_with_non_default_dictionary(self):
        base_dictionary = ["t", "i", "y", "n", "b", " "]
        self.assertEqual([2, 1, 1, 3, 6, 5, 7, 9, 11, 7, 17], lzw.encode("itty bitty bit bin", base_dictionary))

    def test_decode(self):
        self.assertEqual("aaacbcbcbc", lzw.decode([1, 4, 3, 2, 6, 8]))

    def test_encode_decode(self):
        base_dictionary = ["t", "i", "y", "n", "b", " "]
        input = "itty bitty bit bin"

        encoded = lzw.encode("itty bitty bit bin", base_dictionary)
        decoded = lzw.decode(encoded, base_dictionary)
        self.assertEqual(input, decoded)
