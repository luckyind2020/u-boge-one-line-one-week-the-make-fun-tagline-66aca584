"""Tagline entry for the make.fun one-line tagline bounty.

Reads the single tagline from entry.txt, checks it against the
bounty's 100-character limit, and prints it.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).resolve().parent / "entry.txt"
MAX_CHARS = 100


def load_tagline(path=ENTRY_FILE):
    if not path.exists():
        raise SystemExit(f"entry file missing: {path}")
    raw = path.read_text(encoding="utf-8")
    return raw.strip()


def main():
    line = load_tagline()
    if not line:
        raise SystemExit("entry file is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"tagline is {len(line)} chars, over the 100-char limit")
    print(line)
    print(f"({len(line)}/{MAX_CHARS} chars)", file=__import__("sys").stderr)


if __name__ == "__main__":
    main()
