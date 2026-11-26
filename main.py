"""Entrypoint for the make.fun mini bounty
"The Worst Line an AI Could Say".

Writes the chosen pickup line, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only.
"""

import os

LINE = (
    "Based on your browsing history, you are single, lonely, "
    "and statistically overdue for affection. I can help."
)


MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
