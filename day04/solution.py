import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def find_xmas(grid: list[str], row: int, column: int) -> int:
    # First check if we're at a valid position
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
        return 0
    
    # If this position isn't 'X', no need to check further
    if grid[row][column] != 'X':
        return 0
    
    count = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    # (-1,-1) (-1,0) (-1,1)     ↖  ↑  ↗
    # (0,-1)   (X)   (0,1)      ←  X  →
    # (1,-1)  (1,0)  (1,1)      ↙  ↓  ↘

    # For each direction, try to find 'MAS'
    for dx, dy in directions:
        # Check if we can fit 'XMAS' in this direction
        if (0 <= row + 3*dx < len(grid)) and (0 <= column + 3*dy < len(grid[0])):
            # Try to make the word
            word = ""
            for i in range(4):
                word += grid[row + i*dx][column + i*dy]
            if word == "XMAS":
                count += 1
            
    return count

def solve_part1(data: str) -> int:
    
    grid = data.strip().split('\n')
    total = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            total += find_xmas(grid, row, column)

    return total

def check_xmas_pattern(grid: list[str], row: int, col: int) -> bool:
    # Check if we have enough space around center
    if (row < 1 or row >= len(grid)-1 or col < 1 or col >= len(grid[0])-1):
        return False
    
    # Check if center is 'A' (the center of X-MAS is always an 'A')
    if grid[row][col] != 'A':
        return False
    
    # Check all possible combinations of MAS in diagonals (We are allowed to have SAM or MAS in the diagonals)
    patterns = [
        ('M', 'S', 'M', 'S'),  # MAS + MAS
        ('M', 'S', 'S', 'M'),  # MAS + SAM
        ('S', 'M', 'M', 'S'),  # SAM + MAS
        ('S', 'M', 'S', 'M'),  # SAM + SAM
    ]
    
    # Get the letters in each diagonal
    ul = grid[row-1][col-1]
    ur = grid[row-1][col+1]
    ll = grid[row+1][col-1]
    lr = grid[row+1][col+1]
    
    # Check if any pattern matches
    return (ul, lr, ur, ll) in patterns

def solve_part2(data: str) -> int:
    grid = data.strip().split('\n')
    total = 0
    
    # For each position that could be center of an X-MAS pattern
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if check_xmas_pattern(grid, row, col):
                total += 1
    
    return total

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=18,  # Example answer
        expected_part2=9    # Example answer for part 2
    )