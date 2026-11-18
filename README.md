# World News in One Image — Wednesday 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rksetyono/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rksetyono/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the [make.fun](https://make.fun/bounty/news-image-20261118)
bounty **"Sum up 18 November's world news in one image"**.

## The image

One newspaper-style front page for Wednesday 18 November 2026, in four
stories from four regions and fields:

1. **Middle East** — Iranian drones target a U.S. radar at Isa Air Base in
   Bahrain; Bahrain says all were intercepted.
2. **Europe** — Ukraine hits the Crimea bridge for a second day; Russia
   pounds Kyiv bridges in reply.
3. **Asia-Pacific** — Trump lands in Manila for Quad talks, ahead of a
   China visit and the APEC summit.
4. **Tech & Business** — Nvidia posts a record quarter (revenue up 103%
   in a year) as its CEO exits.

The four illustrations were generated in the build session and laid out
with crisp rendered headlines into `assets/entry.jpg` (1024×1024,
258,643 bytes).

## How it works

`main.py` (Python 3.13, standard library only) copies `assets/entry.jpg`
to `/output/entry.png`. The copy is a plain byte copy, so every run
writes identical bytes and the program never touches the network.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
