#! /bin/python3
import numpy as np
from copy import deepcopy, copy
def out_of_bounds(x, y, w, h):
    return x >= w or y >= h or x < 0 or y < 0

def crazy_in(l, loc, dir):
    for p_loc, p_dir in l:
        if (loc == p_loc).all() and (dir == p_dir).all():
            return True
    return False

def s1(loc, board, dir):
    w, h = len(board[0]), len(board)
    mat_right = np.array([[0, -1],
                          [1, 0]])
    total = 0
    i = 0
    while(True):
        nx, ny = loc + dir
        x, y = loc
        if out_of_bounds(nx, ny, w, h):
            board[y][x] = "X"
            total += 1
            break
        if board[ny][nx] == "#":
            dir = mat_right @ dir
            continue
        if board[y][x] != "X":
            board[y][x] = "X"
            total += 1

        loc += dir
        i += 1

    print(f"{total=}")
    print(f"{i=}")

def foo(loc, board, dir):
    old_loc = deepcopy(loc)
    old_dir = deepcopy(dir)
    w, h = len(board[0]), len(board)
    mat_right = np.array([[0, -1],
                          [1, 0]])
    dir = mat_right @ dir 
    locs = set()
    dirs = set()

    #while(i < 100000):
    while(True):
        nx, ny = loc + dir
        
        # if(np.any(np.all([loc, dir] == np.array(locs), axis = 2))):
            #if (old_loc == loc).all() and (old_dir == dir).all():
        if out_of_bounds(nx, ny, w, h):
            return False
        if board[ny][nx] == "#" or ((dir == old_dir).all() and (loc == old_loc).all()):
            if ((dir == old_dir).all() and (loc == old_loc).all()) or (tuple(deepcopy(loc)), tuple(deepcopy(dir))) in locs: return True
            locs.add((tuple(deepcopy(loc)), tuple(deepcopy(dir))))

            dir = mat_right @ dir
            continue

        loc += dir
    return True


def s2(loc, board, dir):
    w, h = len(board[0]), len(board)
    mat_right = np.array([[0, -1],
                          [1, 0]])
    start_loc = deepcopy(loc)
    total = 0
    i = 0
    locs = set()
    while(True):
        nx, ny = loc + dir
        #print(i)
        if(i % 56) ==0:
            print(i//56)
        if out_of_bounds(nx, ny, w, h):
            break
        if board[ny][nx] == "#":
            dir = mat_right @ dir
            continue
        if foo(deepcopy(loc), board, deepcopy(dir)) and not (loc + dir == start_loc).all():
            locs.add((nx, ny))
            total += 1
        loc += dir
        i += 1
    print(f"{len(locs)}")

def main():
    loc = np.array([0, 0])
    mat_right = np.array([[0, -1],
                          [1, 0]])
    dir = np.array([0, -1])
    with open("./input", "r") as f:
        board = f.read().split("\n")
        board.pop()
        board = list(map(lambda x: [*x], board))
        for y, row in enumerate(board):
            for x, col in enumerate(row):

                if col in ("^", "<", ">", "v"):
                    print(col)
                    loc = np.array((x, y))
                    break
    s1(deepcopy(loc), deepcopy(board), deepcopy(dir))
    s2(deepcopy(loc), board, deepcopy(dir))
    
        
        

if __name__ == "__main__":
    main()
