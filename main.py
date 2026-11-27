#!/usr/bin/env python3
"""Describe your ex in one word.

Entry: a program that writes one text to /output/entry.txt: one word
only, describing your ex.
"""
import os

JOKE = "Ghosted."

# The entry must be one word only.
assert len(JOKE.split()) == 1, "JOKE must be one word only"
assert "\n" not in JOKE, "JOKE must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
