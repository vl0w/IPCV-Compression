from unittest import TestCase

import lz77
import lz78

jonas_compressed = [0, 'j',  # 1  j
            0, 'o',  # 2  o
            0, 'n',  # 3  n
            0, 'a',  # 4  a
            0, 's',  # 5  s
            0, ' ',  # 6  _
            0, 'h',  # 7  h
            4, 'n',  # 8  an
            5, 'e',  # 9 se
            3, None]  #10 n

jonas_uncompressed = "jonas hansen"

ittybitti_compressed = [0, 'i',  # 1  i
              0, 't',  # 2  t
              2, 'y',  # 3  ty
              0, ' ',  # 4  _
              0, 'b',  # 5  b
              1, 't',  # 6  it
              3, ' ',  # 7  ty_
              0, 'n',  # 8  n
              6, 't',  # 9  itt
              0, 'y',  # 10  y
              4, 'g',  # 11  _g
              0, 'r',  # 12  r
              12, 'r',  # 13  rr
              9, 'y',  # 14  itty
              4, 'b',  # 15  _b
              6, ' ',  # 16  it_
              5, 'i',  # 17  bi
              8, None] # 18  n

ittybitty_uncompressed = "itty bitty nitty grrritty bit bin"


class TestLineDetectionImpl(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        data = ""
        expected = []

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_encode_single_char(self):
        data = "a"
        expected = [0, 'a']

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_encode_two_chars(self):
        data = "aa"
        expected = [0, 'a', 1, None]

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_encode_two_chars2(self):
        data = "ab"
        expected = [0, 'a', 0, 'b']

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_encode_one_word(self):
        data = jonas_uncompressed
        expected = jonas_compressed

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_encode_ittybitty(self):
        data = ittybitty_uncompressed
        expected = ittybitti_compressed

        result = lz78.encode(data)

        self.assertEqual(expected, result)

    def test_decode_jonas(self):
        data = jonas_compressed
        expected = jonas_uncompressed

        result = lz78.decode(data)

        self.assertEqual(expected, result)

    def test_decode_ittybitty(self):
        data = ittybitti_compressed
        expected = ittybitty_uncompressed

        result = lz78.decode(data)

        self.assertEqual(expected, result)









