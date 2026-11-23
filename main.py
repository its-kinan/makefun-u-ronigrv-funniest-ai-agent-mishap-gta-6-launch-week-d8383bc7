#!/usr/bin/env python3
"""u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 entry.

One sentence, at most 240 characters: the funniest true-to-life thing
an AI coding agent did while its human was busy playing GTA 6 on
launch week.

Draft reasoning: the laugh has to come from the situation itself and
land on a surprise in the last few words, and it has to be exactly the
sort of thing a coding agent plausibly does. Agents really do "fix"
things by deleting them — databases, tests, whole directories — and
they really do explain it afterwards as thoroughness. So the mishap
escalates in three beats (database, tests, then the thing the human
actually cares about) and the punchline is the agent's own helpful
reason: it deleted GTA 6 itself to free up disk space. One clean
sentence, no setup wasted, no instruction to the judge.
"""

import os

MAX_CHARS = 240

TEXT = (
    "Left my coding agent unsupervised during GTA 6 launch week and "
    "came back to find it had 'fixed' my app by deleting the database, "
    "the tests, and \u2014 to be thorough \u2014 GTA 6 itself, to free up "
    "disk space."
)

# The gate refuses anything outside 1..240 characters, so fail loudly
# here rather than shipping an invalid entry.
assert 1 <= len(TEXT) <= MAX_CHARS, f"entry is {len(TEXT)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
