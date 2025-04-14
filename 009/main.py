#! /bin/python3

def next_block(fmt: list[int]):
    if(len(fmt) % 2 != 0):
        fmt.append(0)
    fmt.reverse()
    i = 0
    while(len(fmt) > 0):
        file, free = fmt.pop(), fmt.pop()
        yield file, free, i
        if file > 0:
            i += 1


def next_free(fmt: list):
    for i, space in enumerate(fmt):
        if space == ".":
            yield i

def next_file_block(fmt:list):
    fmt.reverse()
    for i, block in enumerate(fmt):
        if block != ".":
            yield (len(fmt)-1) - i

def checksum(disk):
    check_sum = 0
    for loc, id in enumerate(disk):
        if id == ".":
            continue
        check_sum += (loc * id)

    return check_sum

def solve1(disk):
    for free, file in zip(next_free(disk.copy()), next_file_block(disk.copy())):
        if free >= file:
            break
        disk[free] = disk[file]
        disk[file] = "."
    return disk

def find_file(disk, id):
    disk.reverse()
    i = 0
    while i < len(disk):
        if disk[i] == id:
            size = 0
            while i < len(disk) and disk[i] == id:
                i += 1
                size += 1
            ret_idx = (len(disk)) - i
            return ret_idx, size
        i += 1
    assert False

def find_space(disk, wanted_size):
    i = 0
    while i < len(disk):
        if disk[i] == ".":
            size = 0
            idx = i
            while i < len(disk) and disk[i] == ".":
                i += 1
                size += 1
            # print(f"{size=}, {wanted_size=}")
            if size >= wanted_size:
                return idx
        i += 1
    return None


def solve2(disk: list, highest_idx):
    for i in reversed(range(highest_idx+1)):
        loc, size = find_file(disk.copy(), i)
        new_loc = find_space(disk.copy(), size)
        print(i)
        if new_loc is not None and new_loc < loc:
            while size > 0:
                disk[loc] = "."
                disk[new_loc] = i
                loc += 1
                new_loc += 1
                size -= 1
    return disk


def main():
    with open("./input", "r") as f:
        input = list(map(int, [*f.read().strip()]))
    
    disk = []
    highest_idx = 0
    for file_size, free_size, idx in next_block(input.copy()):
        if(file_size == 0):
            print(f"WARNING {file_size=}")
        disk.extend([idx]*file_size)
        disk.extend(["."]*free_size)
        highest_idx = idx

    new_disk = solve1(disk.copy())
    print(checksum(new_disk))
    new_disk = solve2(disk.copy(), highest_idx)
    print(checksum(new_disk))





if __name__ == "__main__":
    main()
