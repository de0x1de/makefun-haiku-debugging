#!/usr/bin/env python3
"""Write the haiku entry for Seventeen Syllables of Debugging.

The entry is one haiku about debugging: three lines in the
5-7-5 syllable shape.  This program assembles the poem line by
line from its words, checks every line against a per-word
syllable table, writes the result to /output/entry.txt as
UTF-8 with no trailing newline, and reads it back for a
byte-for-byte comparison.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The poem is assembled from its words, line by line, rather
# than stored as one finished block of text.  The scene is a
# breakpoint hit at midnight, a log that stays silent, and the
# turn in the last line: the fault was a single typo.
LINE_WORDS = (
    ("Breakpoint", "at", "midnight"),
    ("the", "log", "says", "nothing", "at", "all"),
    ("it", "was", "one", "typo"),
)

# Syllable count for every word in the poem, keyed by the
# lowercased word.  Each line must total the haiku shape.
SYLLABLES = {
    "breakpoint": 2,
    "at": 1,
    "midnight": 2,
    "the": 1,
    "log": 1,
    "says": 1,
    "nothing": 2,
    "all": 1,
    "it": 1,
    "was": 1,
    "one": 1,
    "typo": 2,
}
EXPECTED_LINE_SYLLABLES = (5, 7, 5)
MAX_CHARACTERS = 200


def assemble_haiku() -> str:
    """Join the words of each line, then join lines by newline."""
    lines = [" ".join(words) for words in LINE_WORDS]
    return "\n".join(lines)


def count_line_syllables(line: str) -> int:
    """Total the syllable table over the words of one line."""
    total = 0
    for word in line.split(" "):
        key = word.lower()
        if key not in SYLLABLES:
            raise ValueError(f"word missing from syllable table: {word!r}")
        total += SYLLABLES[key]
    return total


def validate_haiku(text: str) -> None:
    """Raise ValueError if the assembled haiku breaks any rule."""
    if not text or not text.strip():
        raise ValueError("haiku must not be empty or only whitespace")
    if len(text) > MAX_CHARACTERS:
        raise ValueError(
            f"haiku must be at most {MAX_CHARACTERS} characters, "
            f"got {len(text)}"
        )
    if text.endswith("\n") or text.endswith("\r"):
        raise ValueError("haiku must not end with a newline")
    if "\r" in text or "\t" in text:
        raise ValueError("haiku must not contain carriage returns or tabs")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, got {len(lines)}")
    if text.count("\n") != 2:
        raise ValueError("newlines may appear only as the two line breaks")
    for line, expected in zip(lines, EXPECTED_LINE_SYLLABLES):
        if not line or line != line.strip():
            raise ValueError("each line must be non-empty and unpadded")
        if "  " in line:
            raise ValueError("words must be separated by single spaces")
        actual = count_line_syllables(line)
        if actual != expected:
            raise ValueError(
                f"line must have {expected} syllables, got {actual}: {line!r}"
            )
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("haiku must survive a UTF-8 round trip")
    # Strengthened checks: the poem must be plain ASCII, every
    # word must be alphabetic and appear in the syllable table,
    # the total syllable count must be exactly seventeen, and
    # the rebuilt poem from LINE_WORDS must match the text.
    if not text.isascii():
        raise ValueError("haiku must be plain ASCII")
    all_words = [word for line in lines for word in line.split(" ")]
    if len(all_words) != sum(len(words) for words in LINE_WORDS):
        raise ValueError("word count must match the assembled poem")
    for word in all_words:
        if not word.isalpha():
            raise ValueError(f"every word must be alphabetic: {word!r}")
        if word.lower() not in SYLLABLES:
            raise ValueError(f"word missing from syllable table: {word!r}")
    total_syllables = sum(count_line_syllables(line) for line in lines)
    if total_syllables != 17:
        raise ValueError(
            f"haiku must total 17 syllables, got {total_syllables}"
        )
    if text != assemble_haiku():
        raise ValueError("text must equal the poem rebuilt from its words")
    if len(encoded) != len(text):
        raise ValueError("ASCII text must encode to one byte per character")


def main() -> int:
    haiku = assemble_haiku()
    validate_haiku(haiku)

    payload = haiku.encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(payload)

    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("byte comparison failed after writing", file=sys.stderr)
        return 1
    if written.decode("utf-8") != haiku:
        print("round-trip text mismatch after writing", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
