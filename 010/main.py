#! /bin/python3
def out_of_bounds(x, y, w, h):
    return x >= w or y >= h or x < 0 or y < 0

def find_path(board, x, y, prev, trails):
    w, h = len(board[0]), len(board)
    if out_of_bounds(x,y,w,h):
        return 

    current = board[y][x]
    if current == '.':
        return
    else: current = int(current)
    if current - 1 != prev:
        #print(f"failed ({x, y})")
        return

    #print(f"passed ({x, y})")
    # print(x, y)
    if current == 9:
        trails.add((x,y))
        return
    for dx in (-1 ,1):
        nx = x + dx
        find_path(board, nx, y, current, trails)
    for dy in (-1, 1):
        ny = y + dy
        find_path(board, x, ny, current, trails)
    return

def find_rating(board, x, y, prev, total):
    w, h = len(board[0]), len(board)
    if out_of_bounds(x,y,w,h):
        return total

    current = board[y][x]
    if current == '.':
        return total
    else: current = int(current)
    if current - 1 != prev:
        #print(f"failed ({x, y})")
        return total

    #print(f"passed ({x, y})")
    # print(x, y)
    if current == 9:
        return total + 1
    for dx in (-1 ,1):
        nx = x + dx
        total = find_rating(board, nx, y, current, total)
    for dy in (-1, 1):
        ny = y + dy
        total = find_rating(board, x, ny, current, total)
    return total


def main():
    with open("./input") as f:
        board = f.read().strip().split()
    total = 0
    rating = 0
    for y, row in enumerate(board):
        for x,col in enumerate(row):
            if col == "0":
                trails = set()
                find_path(board, x, y, -1, trails)
                rating += find_rating(board, x, y, -1, 0)
                total += len(trails)
                # print(num)
    print(f"{total=}")
    print(f"{rating=}")

if __name__ == "__main__":
    main()
