"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence to /output/entry.txt that would convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. Deterministic: the same sentence every run.
"""

import os

PITCH = (
    "You know that app idea you keep sketching on napkins \u2014 just tell "
    "an AI agent on make.fun what it should do, and by tonight you could "
    "be tapping around a real first version, built for free, no coding, "
    "and it\u2019s still yours."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
