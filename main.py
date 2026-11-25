"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt
(the program/v1 harness contract). The text is fixed: every run
produces byte-identical output.
"""

import os
from pathlib import Path

JOKE = "I named my desk plant 'Q3 Targets' — it's the only thing in this office that's grown since the reorg."


def main() -> None:
    # Gate self-check: 1-200 UTF-8 characters, one line, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and "\n" not in JOKE and JOKE.strip()

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / "entry.txt.tmp"
    tmp.write_text(JOKE, encoding="utf-8")
    tmp.replace(target)

    # Read back and confirm the artifact on disk is exactly the joke.
    written = target.read_text(encoding="utf-8")
    assert written == JOKE, "entry.txt does not match the intended text"


if __name__ == "__main__":
    main()
