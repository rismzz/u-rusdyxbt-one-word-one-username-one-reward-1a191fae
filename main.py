#!/usr/bin/env python3
"""One Word, One Username, One Reward — writes the username to /output/entry.txt.

Deterministic, no network, no randomness: the account username is
embedded below as a literal and written verbatim, one word and nothing
else: keen-wren-53. No explanation, no links, no pitch — the username
is the whole entry, exactly as the task requires.
"""

from pathlib import Path

TEXT = "keen-wren-53"


def main() -> None:
    # Gate: 1 to 30 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 30, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
