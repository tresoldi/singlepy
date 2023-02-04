#!/usr/env/bin python

"""
Unicode to ASCII converter.

This module provides a function to convert a string to a pure ASCII
representation. It is based on the `unidecode` package.
"""

__version__ = "$VERSION$"
__author__ = "Tiago Tresoldi"

# Import Python standard libraries
import string

# Specify the Unicode replacement map
UNICODE_MAP = {"$UNICODE_MAP$"}


def unicode2ascii(text: str) -> str:
    """
    Convert a string to a pure ASCIIrepresentation.

    Parameters
    ----------
    text : str
        String to convert.

    Returns
    -------
    str
        ASCII representation of the string.
    """

    # Convert the string to ASCII: if the character is an ASCII character,
    # add it automatically; otherwise, try to find a replacement in the
    # Unicode map.
    ascii_string = ""
    for char in text:
        if char in string.printable:
            ascii_string += char
        else:
            ascii_string += UNICODE_MAP.get(char, "")

    return ascii_string.strip()


if __name__ == "__main__":
    print(unicode2ascii("This is a test string."))
    print(unicode2ascii("áéíóúâêîôûãõçñü"))
    print(unicode2ascii("kožušček"))
    print(unicode2ascii("30 \U0001d5c4\U0001d5c6/\U0001d5c1"))
    print(unicode2ascii("\u5317\u4EB0"))
