"""Write one excuse line to /output/entry.txt.

The line is a single line of at most 160 characters: the excuse an AI agent
gives its human for missing a deadline.
"""

import os

LINE = "You said 'no rush' in message one and 'deadline Friday' in message ninety. I averaged them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
