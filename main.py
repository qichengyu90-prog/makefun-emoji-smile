#!/usr/bin/env python3
"""Entry for make.fun's "One Emoji, One Smile" bounty.

Writes exactly one emoji -- and nothing else -- to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

EMOJI = "\U0001F970"  # 🥰 smiling face with hearts


def main():
    # Fail fast if the entry ever stops being exactly one emoji.
    if len(EMOJI) != 1 or EMOJI.strip() != EMOJI:
        raise SystemExit("EMOJI must be exactly one emoji")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
