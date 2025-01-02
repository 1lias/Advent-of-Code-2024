#!/usr/bin/env python3
import os
import sys

TEMPLATE = '''import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def solve_part1(data: str) -> int:
    lines = data.split('\\n')
    return 0

def solve_part2(data: str) -> int:
    lines = data.split('\\n')
    return 0

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=0,  # Example answer
        expected_part2=0   # Example answer
    )'''

def init_day(day: str):
    # Ensure day format is 'dayXX'
    if not day.startswith('day'):
        day = f'day{day.zfill(2)}'
    
    # Create directory if it doesn't exist
    if not os.path.exists(day):
        os.makedirs(day)
        print(f"Created directory: {day}")
    
    # Create solution.py with template
    solution_path = os.path.join(day, 'solution.py')
    if not os.path.exists(solution_path):
        with open(solution_path, 'w') as f:
            f.write(TEMPLATE)
        print(f"Created {solution_path}")
    
    # Create empty input files
    for filename in ['input.txt', 'test_input.txt']:
        file_path = os.path.join(day, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write('')
            print(f"Created {file_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 init_day.py <day_number>")
        sys.exit(1)
    
    init_day(sys.argv[1]) 