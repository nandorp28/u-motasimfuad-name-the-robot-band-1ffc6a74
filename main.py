#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song
(under 200 characters) to /output/entry.txt.
"""
import os

ENTRY = (
    "The Drone Strikes \u2014 hit single 'Buzz Kill' topped the charts "
    "for 11 days. Our lead singer flew into a wedding, and the venue "
    "billed us for the cake."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == text, "round-trip mismatch"
    assert not back.endswith("\n"), "no trailing newline"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
