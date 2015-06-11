import os
import unittest
import sys
import sines


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_file.svg'

    def test_argument_parsing(self):
        parser = sines.create_parser()
        options = parser.parse_args()

        self.assertEqual(options.num, 3)
        self.assertTrue(options.legend)
        self.assertEqual(options.file, 'afile.png')

    def test_argument_checking(self):
        parser = sines.create_parser()
        options = parser.parse_args('-n -1')
        self.assertFalse(sines.check_args(options))

        with open(self.filename, 'w') as f:
            f.write("Hi there!")

        options = parser.parse_args('-n 1 -f '.format(self.filename))
        self.assertFalse(sines.check_args(options))

        try:
            os.remove(self.filename)
        except:
            pass

    def check_file_created(self):
        parser = sines.create_parser()

        options = parser.parse_args('-n 1 -f '.format(self.filename))
        self.assertTrue(sines.check_args(options))

        sines.main(options)

        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()