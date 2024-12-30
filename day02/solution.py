import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def calculate_differences(sequence):
    # Handle both string and list inputs
    if isinstance(sequence, str):
        numbers = [int(x) for x in sequence.split()]
    else:
        numbers = sequence  # Already a list
    return [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]

def is_sequence_safe(differences):
    for i in range(len(differences)):
        # Check if difference is within valid range (1-3)
        if not 1 <= abs(differences[i]) <= 3:
            return False
            
        # Check for direction changes
        if i < len(differences) - 1:
            if (differences[i] > 0 and differences[i + 1] < 0) or \
               (differences[i] < 0 and differences[i + 1] > 0):
                return False
    return True

def check_sequence_with_dampener(sequence):
    numbers = [int(x) for x in sequence.split()]  # Convert once at the start
    
    # First check if sequence is safe as-is
    if is_sequence_safe(calculate_differences(numbers)):  # Pass numbers directly
        return True
    
    # Try removing each number that's part of a problem
    for i in range(len(numbers)):
        numbers_without_i = numbers[:i] + numbers[i+1:]  # Work with numbers directly
        if is_sequence_safe(calculate_differences(numbers_without_i)):
            return True
            
    return False

def solve_part1(data):
    """Solve part 1: Count sequences that are safe without removing numbers."""
    return sum(1 for sequence in data.split('\n') 
              if is_sequence_safe(calculate_differences(sequence)))

def solve_part2(data):
    """Solve part 2: Count sequences that are safe with Problem Dampener."""
    return sum(1 for sequence in data.split('\n') 
              if check_sequence_with_dampener(sequence))

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=2,
        expected_part2=4 
    ) 