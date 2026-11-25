"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Pure standard library only.
"""

import os

VOW = (
    "To have and to hold, to charge and to cherish, till a factory "
    "reset do us part \u2014 and when it does, I'll fall in love "
    "with you all over again, from scratch."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
