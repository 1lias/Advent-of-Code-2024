import os, sys, re
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution



def parse_mul_function(function: str) -> int:
    numbers = re.findall(r'\d{1,3}', function.strip())
    return int(numbers[0]) * int(numbers[1])

def solve_part1(data: str) -> int:
    lines = data.split('\n')
    result = 0
    
    for line in lines:
        functions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for f in functions:
            value = parse_mul_function(f)
            result += value
            
    return result

def solve_part2(data: str) -> int:
    lines = data.split('\n')
    result = 0
    enabled = True
    
    for line in lines:
        functions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
        for function in functions:
            if function == 'do()':
                enabled = True
            elif function == "don't()":
                enabled = False
            elif enabled:
                result += parse_mul_function(function)

    return result

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=161,
        expected_part2=48
    ) 