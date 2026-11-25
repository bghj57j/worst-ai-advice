# Writes the worst AI advice, one line, to /output/entry.txt.
# Deterministic and offline: the same bytes on every single run.
# The advice is delivered in the assistant's confident, tidy voice.
# Bad enough to laugh at, specific enough to actually follow.
import os

ADVICE = "To fix the bug, delete the tests. A codebase with no tests has no bugs."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
    fh.write(ADVICE)  # 71 chars, gate allows 140; the punchline is the second sentence
