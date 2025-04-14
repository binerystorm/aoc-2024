#! /bin/python3
import re
from dataclasses import dataclass

def solve2(x1,y1,x2,y2,px,py):
    B = (py*x1-px*y1)/(x1*y2-y1*x2)
    A = (px-B*x2)/x1

    if (A.is_integer() and B.is_integer() and 0 <= A and 0 <= B):
        return (int(A),int(B))
    else:
        return None
def solve(x1,y1,x2,y2,px,py):
    B = (py*x1-px*y1)/(x1*y2-y1*x2)
    A = (px-B*x2)/x1

    if (A.is_integer() and B.is_integer() and 0 <= A <= 100 and 0 <= B <= 100):
        return (int(A),int(B))
    else:
        return None

def main():
    with open("./input") as f:
        input = list(map(int, reversed(re.findall("\\d+", f.read()))))

    total = 0
    while len(input) > 0:
        res = solve2(input.pop(), input.pop(), input.pop(), input.pop(), input.pop()+10000000000000, input.pop()+10000000000000)
        #print(res)
        if res is not None:
            A, B = res
            total += A*3 + B
    print(total)


if __name__ == "__main__":
    main()
