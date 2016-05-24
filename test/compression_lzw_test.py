import lzw
from unittest import TestCase


class TestEncodeLZW(TestCase):
    def test_encode(self):
        self.assertEqual([1, 4, 3, 2, 6, 8], lzw.encode("aaacbcbcbc"))

    def test_decode(self):
        self.assertEqual("aaacbcbcbc", lzw.decode([1, 4, 3, 2, 6, 8]))

    def test_encode_decode(self):
        base_dictionary = ["t", "i", "y", "n", "b", " "]
        expected_encoded = [2, 1, 1, 3, 6, 5, 7, 9, 11, 7]
        expected_decoded = "itty bitty bit"

        actual_encoded = lzw.encode(expected_decoded, base_dictionary)
        self.assertEqual(expected_encoded, actual_encoded)

        actual_decoded = lzw.decode(actual_encoded, base_dictionary)
        self.assertEqual(expected_decoded, actual_decoded)
