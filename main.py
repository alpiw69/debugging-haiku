"""make.fun bounty: Seventeen Syllables of Debugging.

Deterministic, no-network program. Writes one haiku about debugging, three
lines in the 5-7-5 syllable shape, at most 200 characters, to
/output/entry.txt. Running twice writes identical bytes.
"""
from pathlib import Path

HAIKU = "three am, cursor blinks\nthe log says nothing is wrong\nso it must be me"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(HAIKU, encoding="utf-8")
    print(f"Wrote {OUT} ({len(HAIKU)} chars)")


if __name__ == "__main__":
    main()
