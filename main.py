"""The 3AM Fridge Text — make.fun bounty entry.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt. Gate: 1-140 characters of UTF-8 text, not only
whitespace. Pure standard library; the text is embedded here.
"""

import os

ENTRY = (
    "3am. I'm just the fridge. But the leftover pizza you swore "
    "you'd eat? It's plotting against you. Eat it or bury it."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars, {len(text.split())} words to /output/entry.txt")


if __name__ == "__main__":
    main()
