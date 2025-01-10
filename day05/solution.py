import os, sys, time
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.utils import run_solution

def parse_input(data: str):
    lines = data.split('\n')
    ordering_rules = []
    page_updates = []
    found_separator = False

    for line in lines:
        if line == '':
            found_separator = True
        elif not found_separator:
            ordering_rules.append(line)
        else:
            page_updates.append(line)

    return ordering_rules, page_updates

def build_graph(rules: list[str]):
    graph = defaultdict(list)
    for rule in rules:
        x,y = map(int, rule.split('|'))
        graph[x].append(y)
    return graph

def find_middle_page(update):
    return int(update[len(update) // 2])


def is_correct_order(update, rules):
    index_map = {page: i for i, page in enumerate(update)}
    for page in update:
        for target in rules[page]:
            if target in index_map and index_map[page] > index_map[target]:
                return False
    return True

def solve_part1(data: str) -> int:
    ordering_rules, updates = parse_input(data)
    rules = build_graph(ordering_rules)
    
    totalsum = 0
    for update in updates:
        update = list(map(int, update.split(',')))
        if is_correct_order(update, rules):
            totalsum += find_middle_page(update)
    
    return totalsum

def resolve_order(update,rules):
    sorted_update = update[:]

    for i in range(len(update)):
        for j in range(0, len(update)-i-1): # adding -i in order to not check any of the items more than needed.
            if sorted_update[j] in rules and sorted_update[j+1] in rules[sorted_update[j]]:
                sorted_update[j], sorted_update[j+1] = sorted_update[j+1], sorted_update[j]

    return sorted_update

def solve_part2(data: str) -> int:
    start_time = time.time()
    ordering_rules, updates = parse_input(data)
    rules = build_graph(ordering_rules)

    totalsum = 0
    for update in updates:
        update = list(map(int, update.split(',')))
        if not is_correct_order(update, rules):
            ordered_update = resolve_order(update,rules)
            totalsum += find_middle_page(ordered_update)

    end_time = time.time()
    print(end_time - start_time)

    return totalsum

if __name__ == '__main__':
    run_solution(
        day_dir=os.path.dirname(__file__),
        solve_part1=solve_part1,
        solve_part2=solve_part2,
        expected_part1=143,  # Example answer
        expected_part2=123   # Example answer
    )