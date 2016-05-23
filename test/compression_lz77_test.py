from unittest import TestCase

import lz77


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


class TestCompressionLZ77(TestCase):
    def test_encode_single_char(self):
        data = "a"
        expected = [0, 0, 'a']

        result = lz77.encode(data, 5, 3)

        self.assertEqual(expected, result)

    def test_encode_two_chars(self):
        data = "aa"
        expected = [0, 0, 'a',
                    6, 1, None]

        result = lz77.encode(data, 5, 3)

        self.assertEqual(expected, result)

    def test_encode_abra(self):
        bufsize = 6
        lookahead_bufsize = 4
        data = "abrakabrabra"
        expected = [0, 0, 'a',
                    0, 0, 'b',
                    0, 0, 'r',
                    4, 1, 'k',
                    2, 4, None,
                    4, 3, None]

        result = lz77.encode(data, bufsize, lookahead_bufsize)

        self.assertEqual(expected, result)

    def test_decode_abra(self):
        bufsize = 6
        data = [0, 0, 'a',
                    0, 0, 'b',
                    0, 0, 'r',
                    4, 1, 'k',
                    2, 4, None,
                    4, 3, None]
        expected = "abrakabrabra"

        result = lz77.decode(data, bufsize)

        self.assertEqual(expected, result)

