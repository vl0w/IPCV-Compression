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


class TestCompressionLZ78(TestCase):
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

    def test_encode_lorem(self):
        data = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat."

        result = lz78.encode(data)
        print(data)
        print(result)