# makefun-haiku-debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/de0x1de/makefun-haiku-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/de0x1de/makefun-haiku-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

## What this is

A small, dependency-free Python program for Seventeen
Syllables of Debugging. Running `main.py` writes one haiku
about debugging to `/output/entry.txt`: three lines in the
5-7-5 syllable shape, 66 characters in total, with no
trailing newline, well inside the 200-character limit the
bounty sets.

The picture at the centre is concrete: a breakpoint hit at
midnight and a log that says nothing at all. The last line
turns the poem — after the silent log, the whole fault was
one typo. The program does not store the poem as one finished
block. It assembles each line from its words, checks every
line against a per-word syllable table (5, then 7, then 5,
seventeen in all), validates the shape (exactly three lines,
newlines only as line breaks, plain ASCII), and only then
writes the entry as UTF-8. After writing, it reads the file
back and compares the bytes, so every run produces exactly
the same entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>
