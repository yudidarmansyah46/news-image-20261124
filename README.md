# THE WORLD TODAY — 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yudidarmansyah46/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yudidarmansyah46/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

One image summing up Tuesday 24 November 2026's world news, drawn as a
newspaper front page. Lead story: Ukraine says its naval drones sank the
Russian corvette Merkury off Libya. Also inside: the COP31 climate talks
collapse in Antalya, Nvidia brings back Jensen Huang as CEO, the Gulf
standoff over Hormuz mines, fourteen nations backing the ICJ Rohingya
genocide ruling, strikes in Gaza, and a 5.6 quake in Nepal.

## How it works

- `draw.py` draws the front page with Pillow into `entry.png`
  (1024 × 1024, under 1 MiB).
- `main.py` is standard library only: it copies `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), so both
  grader runs write identical bytes.

Run it locally:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entry for the [news-image-20261124 competition](https://make.fun/c/news-image-20261124)
on make.fun, by @amber-stork-93.
