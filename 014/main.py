#! /bin/python3
import os
import re
import numpy as np
from dataclasses import dataclass
import time

@dataclass
class Robot:
    pos: np.array
    vel: np.array


def solve(input):
    board_size = np.array([101,103])
    cx, cy = board_size // 2
    robots = []
    while len(input) > 0:
        pos = np.array([input.pop(), input.pop()])
        vel = np.array([input.pop(), input.pop()])
        robots.append((pos + vel * 100) % board_size)
    q1, q2, q3, q4 = 0,0,0,0
    for x,y in  robots:
        if x < cx and y < cy:
            q1 += 1
        elif x > cx and y < cy:
            q2 += 1
        elif x < cx and y > cy:
            q3 += 1
        elif x > cx and y > cy:
            q4 += 1

    return q1*q2*q3*q4

def solve2(input):
    board_size = np.array([101,103])
    cx, cy = board_size // 2
    robots = []
    while len(input) > 0:
        pos = np.array([input.pop(), input.pop()])
        vel = np.array([input.pop(), input.pop()])
        robots.append(Robot(pos, vel))
    for i in range(1000,2001):
        os.system("clear")
        board = [["." for _ in range(board_size[0])] for _ in range(board_size[1])]
        print(i)
        for r in robots:
            x,y = (r.pos + r.vel*i) % board_size
            board[y][x] = "#"
        for row in board:
            print("".join(row))
        time.sleep(0.5)

def main():
    with open("./input") as f:
        input = list(map(int, reversed(re.findall("-*\\d+", f.read().strip()))))
        
    #board_size = np.array([11,7])
    board_size = np.array([101,103])
    cx, cy = board_size // 2

    print(solve2(input))
if __name__ == "__main__":
    main()
