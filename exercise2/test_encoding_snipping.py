# coding=utf-8

from unittest import TestCase

from encoding_snipping import main, WordContainer


class TestEncodingSnipping(TestCase):
    def setUp(self):
        self.test_input = {
            "Tom": "I am with various words smaller and larger",
            "Amy": "Some word with same leng",
            "Carl": "Lorem ipsum dolor sit amet consectetur adipiscing elit Nunc facilisis urna sit amet massa laoreet",
        }
        self.test_expected_output = {
            "Tom": WordContainer("i am htiw suoirav sdrow rellams and regral"),
            "Amy": WordContainer("emos drow htiw emas gnel"),
            "Carl": WordContainer("merol muspi rolod sit amet rutetcesnoc gnicsipida elit nunc sisilicaf urna sit "
                                  "amet assam teeroal"),
        }

    def test_main_1(self):
        output = main(self.test_input)
        self.assertDictEqual(self.test_expected_output, output)

    def test_main_2(self):
        self.test_input["Michael"] = "A B C D E F G H I J K"
        self.test_expected_output["Michael"] = WordContainer("a b c d e f g h i j k")
        self.test_input["Karen"] = "IWantToSpeakWithYourManager"
        self.test_expected_output["Karen"] = WordContainer("reganamruoyhtiwkaepsottnawi")

        output = main(self.test_input)
        self.assertDictEqual(self.test_expected_output, output)

    def test_main_foreign_and_symbols(self):
        import six

        self.test_input["Polish"] = "test ęśąćż"
        self.test_expected_output["Polish"] = WordContainer("tset żćąśę")
        self.test_input["Symbols"] = "☀☁☂☃ ☎☏ ☐☑☒ ♠♥♣♦"
        self.test_expected_output["Symbols"] = WordContainer("☃☂☁☀ ☎☏ ☒☑☐ ♦♣♥♠")

        output = main(self.test_input)

        self.assertDictEqual(self.test_expected_output, output)
        for word_container in six.itervalues(output):
            self.assertIsInstance(word_container.words, six.text_type)
