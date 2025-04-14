#! /bin/python3

def distance_between(left, right):
    left.sort()
    right.sort()
    return sum(map(lambda x: abs(x[0]-x[1]), zip(left, right)))

def sim_score(left, right):
    return sum(map(lambda x: x * right.count(x), left))

def main():
    left = []
    right = []
    with open("./input", "r") as f:
        for l in f:
            left_id, right_id = l.split()
            left.append(int(left_id.strip()))
            right.append(int(right_id.strip()))
    print(distance_between(left, right))
    print(sim_score(left, right))

if __name__ == "__main__":
    main()
