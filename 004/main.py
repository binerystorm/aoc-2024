#! /bin/python3
def fini(input, x, y, dx, dy):
    rest = "AS"
    x_len = len(input[0])
    y_len = len(input)
    for i in range(1, len(rest)+1):
        nx = x+dx*i
        ny = y+dy*i
        if(nx >= x_len): return False
        if(ny >= y_len): return False
        if(nx < 0): return False
        if(ny < 0): return False
        if input[ny][nx] != rest[i-1]: return False

    return True

def foo(input, x, y):
    total = 0
    for dy, line in enumerate(input[max(y-1, 0) : y+2]):
        for dx, c in enumerate(line[max(x-1, 0) : x+2]):
            if x > 0:
                offx = dx - 1
            else:
                offx = dx
            if y > 0:
                offy = dy - 1
            else:
                offy = dy
            nx = x + offx
            ny = y + offy
            if (offx < -1) or (offx > 1) or (offy < -1) or (offy > 1): print(f"({x}, {y}):({dx}, {dy})")
            # if x == 0 and y == 3:
            #     print(dx, dy)
            #     print(offx, offy)
            #     print()
            if input[ny][nx] == "M":
                if fini(input, nx, ny, offx, offy): total += 1
    return total

def XMAS(input):
    total = 0
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "X":
                n = foo(input, x, y)
                total +=  n

    print(total)

def X(input, x, y):
    dix = {
        "M": "S",
        "S": "M"
    }
    total = 0
    c = input[y-1][x-1]
    if(c in ("M", "S")):
        if input[y+1][x+1] == dix[c]: total += 1
    c = input[y-1][x+1]
    if(c in ("M", "S")):
        if input[y+1][x-1] == dix[c]: total += 1
    if total == 2: return 1
    else: return 0


def X_MAS(input):
    total = 0
    for y, line in enumerate(input):
        if y == 0 or y == len(input)-1: continue
        for x, c in enumerate(line):
            if x == 0 or x == len(input[0])-1: continue
            if c == "A":
                total += X(input, x, y)

    print(total)

def main():
    with open("./input", "r") as f:
        input = f.readlines()
        input = list(map(lambda x: x[:-1], input))

    X_MAS(input)

if __name__ == "__main__":
    main()
