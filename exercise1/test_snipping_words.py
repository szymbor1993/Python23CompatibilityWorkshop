from unittest import TestCase

from snipping_words import main


class TestSnippingWords(TestCase):
    def setUp(self):
        self.test_input = {
            "Tom": "I am with various words smaller and larger",
            "Amy": "Some word with same leng",
            "Carl": "Lorem ipsum dolor sit amet consectetur adipiscing elit Nunc facilisis urna sit amet massa laoreet",
        }
        self.test_expected_output = {
            "Tom": "i am htiw suoirav sdrow rellams and regral",
            "Amy": "emos drow htiw emas gnel",
            "Carl": "merol muspi rolod sit amet rutetcesnoc gnicsipida elit nunc sisilicaf urna sit amet assam teeroal",
        }

    def test_main_1(self):
        output = main(self.test_input)
        self.assertDictEqual(self.test_expected_output, output)

    def test_main_2(self):
        self.test_input["Michael"] = "A B C D E F G H I J K"
        self.test_expected_output["Michael"] = "a b c d e f g h i j k"
        self.test_input["Karen"] = "IWantToSpeakWithYourManager"
        self.test_expected_output["Karen"] = "reganamruoyhtiwkaepsottnawi"

        output = main(self.test_input)
        self.assertDictEqual(self.test_expected_output, output)
