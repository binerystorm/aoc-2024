#! /bin/python3
import numpy as np
from copy import deepcopy
def out_of_bounds(x, y, w, h):
    return x >= w or y >= h or x < 0 or y < 0

# def count_antinode(a, b, board, w, h):
#     offset = a - b
#     #b + offset = a
#     #b = a - offset
#     x, y = b - offset
#     if (offset == np.array([0, 0])).any():
#         print(offset)
#         return False
#     if not out_of_bounds(x, y, w, h) and not board[y][x]:
#         board[y][x] = True
#         return True

def solve(antena_set, antinodes, w, h):
    total = 0
    
    new_antinodes = deepcopy(antinodes)
    for a in antena_set:
        for b in antena_set:
            if (a == b).all():
                continue
            offset = a - b
            new_antinodes.add(tuple(a))
            new_antinodes.add(tuple(b))
            x, y = b - offset
            # if not out_of_bounds(x, y, w, h):
            while not out_of_bounds(x, y, w, h):
                new_antinodes.add((x, y)) 
                x, y = np.array([x, y]) - offset
            x, y = a + offset
            while not out_of_bounds(x, y, w, h):
                new_antinodes.add((x, y)) 
                x, y = np.array([x, y]) + offset

    return new_antinodes
# def solve(antena_set, board):
#     w, h = len(board[0]), len(board)
#     total = 0
#     for a in antena_set:
#         for b in antena_set:
#             if (a == b).all():
#                 continue
#             if count_antinode(a, b, board, w, h): total += 1
#     return total

def main():
    antenas = {}
    with open("./input", "r") as f:
        board = list(map(lambda x: [*x], f.read().split('\n')))
        board.pop()
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if not (col.isdigit() or col.isalpha()): continue
            if col in antenas:
                antenas[col].append(np.array([x, y]))
            else:
                antenas[col] = [np.array([x,y])]
    w, h = len(board[0]), len(board)

    print(w, h)
    test_board = []
    for _ in range(h):
        test_board.append([False] * w)
    total = 0
    antinodes = set()
    for val in antenas.values():
        if len(val) == 1: continue
        antinodes = solve(val, deepcopy(antinodes), w, h)
    print(len(antinodes))

if __name__ == "__main__":
    main()
