from unittest import TestCase
from day4 import valid_passphrases, ADDED_SECURITY


class TestValidPassphrases(TestCase):
    def test_valid_passphrase(self):
        lines = ['aa bb cc dd ee',]
        self.assertEqual(1, valid_passphrases(lines))
        lines = ['aa bb cc dd aaa',]
        self.assertEqual(1, valid_passphrases(lines))

    def test_invalid_passphrase(self):
        lines = ['aa bb cc dd aa',]
        self.assertEqual(0, valid_passphrases(lines))

    def test_valid_passphrases_with_added_security(self):
        lines = ['abcde fghij',]
        self.assertEqual(1, valid_passphrases(lines, ADDED_SECURITY))
        lines = ['a ab abc abd abf abj',]
        self.assertEqual(1, valid_passphrases(lines, ADDED_SECURITY))
        lines = ['iiii oiii ooii oooi oooo',]
        self.assertEqual(1, valid_passphrases(lines, ADDED_SECURITY))

    def test_invalid_passphrases_with_added_security(self):
        lines = ['abcde xyz ecdab',]
        self.assertEqual(0, valid_passphrases(lines, ADDED_SECURITY))
        lines = ['oiii ioii iioi iiio',]
        self.assertEqual(0, valid_passphrases(lines, ADDED_SECURITY))
