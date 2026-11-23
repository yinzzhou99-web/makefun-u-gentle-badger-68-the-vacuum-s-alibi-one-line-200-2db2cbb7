"""The Vacuum's Alibi: one deadpan excuse for a missed spot.

Writes a single line of at most 200 characters to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library only,
deterministic, no network. The output directory itself is never removed;
only entry.txt is written inside it.

Chosen line: that spot remains uncleaned; I have filed it under "the cat's
problem now" and moved on. Deadpan robot voice, a surprising bureaucratic
twist, and no wasted words.
"""

import os

LINE = "That spot remains uncleaned. I have filed it under 'the cat's problem now' and moved on."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)
    # Guard: confirm the file on disk holds exactly the line we meant.
    with open(target, encoding="utf-8") as fh:
        if fh.read() != text:
            raise SystemExit("entry.txt does not match the chosen line")


if __name__ == "__main__":
    main()
