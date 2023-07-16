import re

from unittest import TestCase

from modules.generator import generate
from modules.generator import PasswordGenerationException


class TestGenerator(TestCase):
    def test_generate(self) -> None:
        lowercase_pattern = r"^([a-z]){12}"
        uppercase_pattern = r"^([A-Z]){12}"
        digit_pattern = r"^\d{12}"
        symbol_pattern = r"^([\(\)\[\]\{\}\;\:\-\_\/\\?\+\*\#\=\&\%\@\|])"

        lowercase_suggestion = generate(
                    12,
                    True,
                    False,
                    False,
                    False,
                )
        
        self.assertTrue(re.match(lowercase_pattern, lowercase_suggestion))

        uppercase_suggestion = generate(
                    12,
                    False,
                    True,
                    False,
                    False,
                )
        
        self.assertTrue(re.match(uppercase_pattern, uppercase_suggestion))
        
        digit_suggestion = generate(
                    12,
                    False,
                    False,
                    True,
                    False,
                )
        
        self.assertTrue(re.match(digit_pattern, digit_suggestion))

        symbol_suggestion = generate(
                    12,
                    False,
                    False,
                    False,
                    True,
                )

        self.assertTrue(re.match(symbol_pattern, symbol_suggestion))

        length_test = generate(10)

        self.assertEqual(len(length_test), 10)

        with self.assertRaises(PasswordGenerationException):
            _ = generate(0)
            
        with self.assertRaises(PasswordGenerationException):
            _ = generate(-1)
            
        with self.assertRaises(PasswordGenerationException):
            _ = generate(12, False, False, False, False)
