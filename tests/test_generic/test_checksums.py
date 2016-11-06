import unittest

from localflavor.generic import checksums


class TestUtilsChecksums(unittest.TestCase):

    def assertChecksumOuput(self, checksum, result_pairs):
        for value, output in result_pairs:
            self.assertEqual(checksum(value), output, "Expected %s(%s) == %s but got %s" % (
                checksum.__name__, repr(value), output, not output))

    def test_luhn(self):
        """Check that function(value) equals output."""
        result_pairs = (
            (4111111111111111, True),
            ('4111111111111111', True),
            (4222222222222, True),
            (378734493671000, True),
            (5424000000000015, True),
            (5555555555554444, True),
            (1008, True),
            ('0000001008', True),
            ('000000001008', True),
            (4012888888881881, True),
            (1234567890123456789012345678909, True),
            (4111111111211111, False),
            (42222222222224, False),
            (100, False),
            ('100', False),
            ('0000100', False),
            ('abc', False),
            (None, False),
            (object(), False),
        )
        self.assertChecksumOuput(checksums.luhn, result_pairs)

    def test_ean(self):
        result_pairs = (
            ('73513537', True),
            (73513537, True),
            ('73513538', False),
            (73513538, False),
            ('4006381333931', True),
            (4006381333931, True),
            ('abc', False),
            (None, False),
            (object(), False),
        )
        self.assertChecksumOuput(checksums.ean, result_pairs)
