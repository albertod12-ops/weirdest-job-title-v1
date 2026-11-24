#!/usr/bin/env python3
"""Weirdest Job Title — v1 (original).

Writes exactly one job title to /output/entry.txt:

    Tax Auditor for the Tooth Fairy

Why this title: a tax auditor is the most mundane, bureaucratic,
paperwork-bound job there is, and the Tooth Fairy is a mythical figure
who literally leaves untraceable cash under children's pillows. Put
them together and you can picture the whole scene at once — a tired
auditor in a grey office demanding receipts from a tiny winged figure
who has never filed a return in her life. Real-sounding title, one
gloriously specific twist, and it lands on the first read.
"""

import os

TITLE = "Tax Auditor for the Tooth Fairy"


def main():
    data = TITLE.encode("utf-8")
    assert 1 <= len(data) <= 60, "entry must be 1-60 characters"
    assert TITLE.strip() == TITLE and "\n" not in TITLE, "entry must be one line"
    assert TITLE.isprintable(), "entry must be printable text only"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    try:
        os.chmod(path, 0o644)
    except PermissionError:
        pass


if __name__ == "__main__":
    main()
