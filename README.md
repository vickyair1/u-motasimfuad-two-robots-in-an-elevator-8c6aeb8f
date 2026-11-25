# Two Robots in an Elevator

[![Competition](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/vickyair1/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/vickyair1/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) on [make.fun](https://make.fun).

## The entry

> I have run 214 simulations of this elevator ride, and in every one of them I say nothing.

89 characters. One robot making small talk with another in an elevator by
confessing it cannot make small talk: it ran 214 simulations of the ride
first, and every single one converged on silence — which it then announces
out loud, as small talk. Machine logic (exhaustive simulation before a word),
awkwardness (the silence itself, named), and a turn that lands on the first
read: all that compute, and the optimal move is saying nothing.

## How it works

`main.py` (Python 3, stdlib only, deterministic) assembles the line from its
three beats — setup, turn, punch — validates it against the gate (1–200
characters, UTF-8, single line, not only whitespace), writes it to
`/output/entry.txt` with no trailing newline, then reads it back and checks
the round-trip byte for byte.

```sh
python3 main.py
# chars: 89
# I have run 214 simulations of this elevator ride, and in every one of them I say nothing.
```

## License

MIT — see [LICENSE](LICENSE).
