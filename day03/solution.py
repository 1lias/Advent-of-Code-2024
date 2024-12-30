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