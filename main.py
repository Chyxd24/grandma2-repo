"""One Word From Grandma (make.fun) — writes ONE word to /output/entry.txt.

Grandma texts you about AI. She types it worried, warm, and a little baffled,
and she capitalizes proper nouns because that is how she was taught.
"""


def the_word() -> str:
    """Return the single word grandma texts about AI."""
    # She means robot but her thumbs are old. One word, typed the way she
    # actually types it: warm, a little baffled, and missing the middle.
    return "robit"


def main() -> None:
    word = the_word()
    # Gate: UTF-8 text, 1 to 30 characters, not only white space.
    assert 1 <= len(word) <= 30, f"word must be 1-30 chars, got {len(word)}"
    assert word.strip(), "word must not be blank"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    print(f"wrote {len(word)} chars to /output/entry.txt: {word!r}")


if __name__ == "__main__":
    main()
