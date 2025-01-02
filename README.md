# Advent of Code 2024

Hi there! 👋 This is my attempt at solving the [Advent of Code 2024](https://adventofcode.com/2024) puzzles. I'm using Python this year because I think it provides enough functionality to solve the puzzles without getting too complex.

I've set up this repository to keep track of my solutions and make it easy to start each new day's challenge. The structure might seem a bit over-engineered, but it helps me focus on solving the puzzles rather than dealing with boilerplate code every day.

## Creating New Days

```bash
# Initialize a new day (creates directory and template files)
./advent init day04    # Format: dayXX
# or
./advent init 4       # Just the number works too
```

This will create:
- `dayXX/solution.py` with template code
- `dayXX/input.txt` for puzzle input
- `dayXX/test_input.txt` for example input

## Running Solutions

```bash
# Run part 1 or 2 of any day
python3 dayXX/solution.py part1
python3 dayXX/solution.py part2
```

## Template for New Days
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def solve_part1(data: str) -> int:
    lines = data.split('\n')
    return 0

def solve_part2(data: str) -> int:
    lines = data.split('\n')
    return 0

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=0,  # Example answer
        expected_part2=0   # Example answer
    )
``` 