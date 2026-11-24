#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one horror story of exactly two sentences to /output/entry.txt
(UTF-8, inside the 1 to 400 character gate). Deterministic, standard
library only, no network, no environment reads.

The story: a father pretends to laugh along while his young daughter
talks in her sleep to the man she says lives inside her bedroom wall.
The second sentence turns the first: last night she told him the man
knows he can hear him too, so the pretending was never protection,
only politeness the thing in the wall no longer requires. The horror
is implied, never explained: nothing says what the man is, or what
happens now that the father has been noticed.
"""

import os

TEXT = (
    "Every night my daughter talks in her sleep to the man she says "
    "lives inside her bedroom wall, and I smile along so she will not "
    "be scared. Last night she whispered, 'He says you can stop "
    "smiling now \u2014 he knows you hear him too.'"
)


def main() -> None:
    # The gate requires 1-400 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 400, "entry must be 1-400 characters"
    # Exactly two sentences: two sentence-ending periods in the text.
    assert TEXT.count(".") == 2, "story must be exactly two sentences"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
