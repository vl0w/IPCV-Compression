from unittest import TestCase

import lz77


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

    def test_encode_two_chars2(self):
        bufsize = 6
        lookahead_bufsize = 4
        data = "abrakabrabra"
        expected = [0, 0, 'a',
                    0, 0, 'b',
                    0, 0, 'r',
                    4, 1, 'k',
                    2, 4, None,
                    4, 3, None,
                    None, None, None]

        result = lz77.encode(data, bufsize, lookahead_bufsize)

        self.assertEqual(expected, result)

    """def test_encode_one_word(self):
        data = jonas_uncompressed
        expected = jonas_compressed

        result = lz78.encode(data)

        self.assertEqual(expected, result)"""
