#! /bin/python3

def solve(input:list[str], r = 1):
    for _ in range(r):
        new = []
        while len(input) > 0:
            a = input.pop()
            if a == '0':
                new.append('1')
            elif len(a) % 2 == 0:
                new.append(str(int(a[0:len(a)//2])))
                new.append(str(int(a[len(a)//2:])))
            else:
                new.append(str(int(a) * 2024))
        input = new.copy()
    return new


def solve2(input, dig, B):
    if B == 1:
        return len(solve(input, 1))
    total = 0
    for n in input:
        if (n, B) in dig:
            total += dig[(n, B)]
        else:
            x = solve2(solve([n], 1), dig, B-1)
            dig[(n,B)] = x
            total += x
    return total



def main():
    with open("./input") as f:
        input = f.read().strip().split()
    total = 0
    total += solve2(input, {}, 75)
    print(total)
    #print(len(solve(input, 25)))
    #input = ["7"]
    

if __name__ == "__main__":
    main()
