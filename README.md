# The World in One Picture — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Diamondpeter/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Diamondpeter/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world news of **Thursday 19 November 2026**:
one dominant lead visual with a massive headline, the day's other top
stories pinned on a world map and stacked bold beneath it, a Day in
Numbers strip, and a sources line at the foot — so a viewer who missed
the day can tell what happened from the picture alone.

This repository is an entry in make.fun's bounty
[**"Sum up 19 November's world news in one image"**](https://make.fun/bounty/news-image-20261119)
($250 in USDC, deadline Sat 21 November 2026, 01:00 Africa/Lagos).

## How it runs

- `entry.png` — the finished image: a PNG, exactly 1024×1024, at most 1 MiB.
- `main.py` — Python 3.13, standard library only, no network. It copies
  `entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR/entry.png`
  outside the grader's container). Two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Design

- Masthead: "THURSDAY 19 NOVEMBER 2026" + "THE WORLD IN ONE PICTURE".
- One scroll-stopping lead story filling the top of the frame, with a
  headline large enough to read at 300 px across.
- A world map with numbered pins, and a numbered grid of the day's
  stories that traces pin-to-story.
- A "Day in Numbers" strip of the day's hardest figures.
- Foot folio: "Compiled from reports by …" naming the day's sources.

## License

MIT — see [LICENSE](LICENSE).
