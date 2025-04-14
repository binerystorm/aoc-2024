#! /bin/python3
def main():
    ord_map = {}
    input = []
    with open("./input", "r") as f:
        for l in f:
            if l.find('|') == -1:
                break
            a, b = map(lambda x: int(x.strip()), l.split('|'))
            if a not in ord_map:
                ord_map[a] = [[],[b]]
            else:
                ord_map[a][1].append(b)

            if b not in ord_map:
                ord_map[b] = [[a],[]]
            else:
                ord_map[b][0].append(a)

        for l in f:
            input.append(
                    list(map(lambda x: int(x.strip()), l.split(',')))
            )

    correct = 0
    fixed = 0
    for l in input:
        out = [0] * len(l)
        for x in l:
            out[len(set(l).intersection(ord_map[x][0]))] = x

        if(out == l):
            correct += out[(len(out)//2)]
        else:
            fixed += out[(len(out)//2)]
    print(f"{correct=}")
    print(f"{fixed=}")


if __name__ == "__main__":
    main()
