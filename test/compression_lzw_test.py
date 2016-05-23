import lzw
from unittest import TestCase

class TestEncodeLZW(TestCase):
    def test_encode(self):
        self.assertEqual([1,4,3,2,6],lzw.encode("aaacbcbcbc"))

    def test_decode(self):
        self.assertEqual("aaacbcbcbc", lzw.decode([1,4,3,2,6,8]))