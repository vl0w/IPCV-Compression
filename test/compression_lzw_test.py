import lzw
from unittest import TestCase

class TestEncodeLZW(TestCase):
    def test_encode(self):
        lzw.encode([1,4,3,2,6],lzw.encode("aaacbcbcbc"))

    def test_decode(self):
        lzw.decode("aaacbcbcbc", lzw.decode([1,4,3,2,6]))