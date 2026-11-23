"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence to /output/entry.txt that would convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. Deterministic: the same sentence every run.
"""

import os

PITCH = (
    "That app idea you keep bringing up over coffee \u2014 just describe it "
    "to an AI agent on make.fun and it will build you a working first "
    "version, no coding and nothing to pay to try, and the idea stays yours."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
