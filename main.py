"""Make the AI Judge Laugh: Office Jokes (make.fun).

Writes exactly one one-line office joke, under 200 characters, to
/output/entry.txt and nothing else. Pure Python 3.13 standard library,
fully deterministic: the same joke on every run.
"""

import os

JOKE = (
    "I set my out-of-office to 'on leave until Monday', "
    "and by noon my inbox had forwarded my own leave request "
    "to me for approval."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the file's characters (1-199).
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
