import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def solve_part1(data):
    """Solve part 1 of the puzzle."""
    # Split into lines and create two lists
    lines = data.split('\n')
    numbers1 = []
    numbers2 = []
    
    # Parse each line into two numbers
    for line in lines:
        num1, num2 = map(int, line.split())
        numbers1.append(num1)
        numbers2.append(num2)
    
    # Sort both lists
    sorted_numbers1 = sorted(numbers1)
    sorted_numbers2 = sorted(numbers2)

    summed_numbers = []

    for number1, number2 in zip(sorted_numbers1, sorted_numbers2):
        summed_numbers.append(abs(number1 - number2))
    
    # Print for debugging
    print("First list (sorted):", sorted_numbers1)
    print("Second list (sorted):", sorted_numbers2)
    print("Summed numbers:", summed_numbers)
    
    return sum(summed_numbers)

def solve_part2(data):
    lines = data.split('\n')
    numbers1 = []
    numbers2 = []

    for line in lines:
        num1, num2 = map(int, line.split())
        numbers1.append(num1)
        numbers2.append(num2)

    similarity_values = []

    for number1 in numbers1:
        count = numbers2.count(number1)
        similarity_values.append(count*number1)
        print(f"Count of {number1} in numbers2: {count} and similarity value: {count*number1}")

    return sum(similarity_values)

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=11,
        expected_part2=31
    ) 