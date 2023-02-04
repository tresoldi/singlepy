#!/usr/bin/env python3

"""
Building script for the projects of `singlepy`.
"""

# Import Python standard libraries
import unicodedata
from pathlib import Path

# Import third-party libraries
from unidecode import unidecode

ROOT_PATH = Path(__file__).parent.resolve()


def fill_template(template_path: Path, replacements: dict) -> str:
    """
    Fill a template file with the given replacements.

    Parameters
    ----------
    template_path : Path
        Path to the template file.
    replacements : dict
        Dictionary with the replacements to perform.

    Returns
    -------
    str
        The filled template.
    """

    # Read the template file
    with open(template_path, "r") as template_file:
        source = template_file.read()

    # Perform the replacements
    for key, value in replacements.items():
        source = source.replace(f'"${key}$"', value)

    return source


def build_unicode2ascii():
    """
    Build the `unicode2ascii` project.
    """

    # Obtain a dictionary with all the Unicode characters that have a
    # corresponding ASCII representation.
    exclude_categories = frozenset(["Cn", "Co", "Cs"])
    exclude_chars = frozenset(["LINE SEPARATOR", "PARAGRAPH SEPARATOR"])

    unicode_map = {}
    for charpoint in range(0x110000):
        category = unicodedata.category(chr(charpoint))
        if category not in exclude_categories:
            # Skip over excluded characters
            try:
                if unicodedata.name(chr(charpoint)) in exclude_chars:
                    continue
            except ValueError:
                pass

            # Build the representation and add it to the map if it contributes
            representation = unidecode(chr(charpoint))
            if representation and (representation != chr(charpoint)):
                unicode_map[chr(charpoint)] = representation

    # Build replacement dictionary string
    unicode_repl = []
    for cp, r in unicode_map.items():
        r = r.replace("\\", "\\\\")
        r = r.replace('"', '\\"')
        unicode_repl.append(f'    "{cp}": "{r}", # {unicodedata.name(cp)}')

    # Build all string replacements
    replacements = {"UNICODE_MAP": "\n".join(unicode_repl) + "\n"}

    # Read the template file, perform the replacements, and write back to disk
    source = fill_template(ROOT_PATH / "templates" / "unicode2ascii.py", replacements)
    with open(ROOT_PATH / "projects" / "unicode2ascii.py", "w") as output_file:
        output_file.write(source)


def build_database():
    """
    Build the `database` project.
    """

    # Build all string replacements
    replacements = {}

    # Read the template file, perform the replacements, and write back to disk
    source = fill_template(ROOT_PATH / "templates" / "database.py", replacements)
    with open(ROOT_PATH / "projects" / "database.py", "w") as output_file:
        output_file.write(source)


def main():
    """
    Script entry point.
    """

    # Build the `unicode2ascii` project.
    build_unicode2ascii()

    # Build the `database` project.
    build_database()

    # TODO: run black (and isort?) on the output files


if __name__ == "__main__":
    main()
