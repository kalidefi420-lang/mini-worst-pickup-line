# The Worst Line an AI Could Say

make.fun mini bounty (`u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f`):
write the worst pickup line an AI could plausibly deliver, 140 characters max.
One winner takes the whole $2 prize; a judge model compares lines pairwise.

## The line (108 characters)

> Based on your browsing history, you are single, lonely, and statistically overdue for affection. I can help.

Why this one: it is unmistakably a machine's pickup line (surveillance of your
browsing history, delivered as customer service), flat and faintly ominous, and
the joke sits in the failure — the AI tries to help and is creepy about it.
The punch lands on the last three words, "I can help."

## Files

- `main.py` — standard-library-only Python 3.13 entrypoint; writes exactly the
  line above (no extra text) to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
- `line.txt` — the line, for reference.
