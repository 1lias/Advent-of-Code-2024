import os
import sys

def read_input(day_dir, filename):
    """Read and return the input file."""
    file_path = os.path.join(day_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()

def run_solution(day_dir, solve_part1, solve_part2, expected_part1=None, expected_part2=None):
    """Run the solution with the specified solve functions and expected results."""
    if len(sys.argv) != 2 or sys.argv[1] not in ['part1', 'part2']:
        print("Usage: python3 solution.py [part1|part2]")
        sys.exit(1)

    part = sys.argv[1]
    
    if part == 'part1':
        test_data = read_input(day_dir, 'test_input.txt')
        print("Testing with example data:")
        test_result = solve_part1(test_data)
        print(f"Part 1 Test: {test_result}")
        
        if expected_part1 is not None and test_result == expected_part1:
            print("\nPart 1 test successful! Running with real input...")
            input_data = read_input(day_dir, 'input.txt')
            print("Part 1:")
            print(f"Solution: {solve_part1(input_data)}")
        else:
            print(f"\nPart 1 test failed! Expected {expected_part1}, got:", test_result)
            print("Please fix the solution before running with real input.")
    else:
        test_data = read_input(day_dir, 'test_input.txt')
        print("Testing with example data:")
        test_result = solve_part2(test_data)
        print(f"Part 2 Test: {test_result}")
        
        if expected_part2 is not None and test_result == expected_part2:
            print("\nPart 2 test successful! Running with real input...")
            input_data = read_input(day_dir, 'input.txt')
            print("Part 2:")
            print(f"Solution: {solve_part2(input_data)}")
        else:
            print(f"\nPart 2 test failed! Expected {expected_part2}, got:", test_result)
            print("Please fix the solution before running with real input.")