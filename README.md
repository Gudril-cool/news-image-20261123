[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Gudril-cool/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Gudril-cool/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Built for the [make.fun news-image bounty](https://make.fun/bounty/news-image-20261123).

# The World in One Day — 23 November 2026

One image that sums up the world news of **Monday 23 November 2026**, drawn as a
newspaper front page:

- **Lead — the Gulf:** Iran's missile and drone strikes on Bahrain (US positions
  and a civilian industrial plant) and tankers targeted in the Strait of Hormuz;
  President Trump says Tehran wants a deal, "not an acceptable one."
- **Climate:** COP31 in Türkiye ends with no deal — the longest UN climate
  conference in history, split over fossil fuels and money.
- **Ukraine:** Russian strikes kill a child and a young woman in Kryvyi Rih and
  hit homes near Kyiv; Ukraine says its naval drones sank the Russian corvette
  Mercury in Benghazi, Libya.
- **Justice:** the ICJ rules Myanmar committed genocide against the Rohingya.
- **Washington:** Democrats win at least 258 House seats, their largest majority
  in decades, as Trump moves to curb oversight.
- **Gaza & West Bank:** Israel's PM-elect Eisenkot calls settler arson attacks
  on Palestinian villages "Jewish terrorism"; a strike on a truck in Gaza
  kills three.
- **Science:** an Anthropic mathematician and the Claude AI claim a proof of
  the Riemann Hypothesis.
- **Also Monday:** Taiwan stocks plunge from their record peak; Nvidia jumps;
  Sinaloa cartel leader "Chapo Isidro" captured in Mexico; Bangladesh says
  Sheikh Hasina faces arrest if she returns.

## How it is built

`draw.py` composes `entry.png` (1024×1024) with PIL — flat shapes and real
fonts, so no text is ever garbled — from the day's reporting (Just Security's
Early Edition of 23 Nov 2026 and the day's news wires). `main.ts` (Node 22,
standard library only) copies `entry.png` to `/output/entry.png`, byte for
byte, every run.

    python3 draw.py          # regenerate entry.png
    node main.ts             # write /output/entry.png (or $MAKEFUN_OUTPUT_DIR)

## License

MIT — see `LICENSE`.
