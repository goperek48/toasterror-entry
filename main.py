#!/usr/bin/env python3
"""Write the toaster's error line to the output file.

One job, done plainly: the competition wants a single line of text, the
message a kitchen toaster puts on its little screen when things go wrong,
and this program drops exactly that line into /output/entry.txt.

Nothing here reads input, touches the network, or rolls dice. The entry
lives in one constant below, so anyone opening this file sees the whole
behaviour at a glance. The gate wants 1-120 UTF-8 characters; the line
below is 67, one sentence of deadpan followed by one sentence of regret.
"""

import os
import sys

# The entry itself. The first sentence is a genuine toaster fault — a full
# crumb tray is a real thing a real appliance reports. The second sentence
# is where the joke lives: the machine totals itself up as mostly crumbs
# with a small, measurable share of remorse. Deadpan voice throughout,
# nothing to explain, funny on the first read.
ENTRY = "ERROR 03: Crumb tray full. Toaster is now 94% crumbs and 6% regret."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
