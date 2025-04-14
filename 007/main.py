#! /bin/python3
from copy import copy

def solve(ans, nums):
    if(len(nums) == 1):
        return ans == nums[0]
    a = nums.pop()
    b = nums.pop()
    nums_plus = copy(nums)
    nums_times = copy(nums)
    nums_concat = copy(nums)
    nums_times.append(a * b)
    nums_plus.append(a + b)
    nums_concat.append(int(str(a) + str(b)))
    if solve(ans, nums_concat):
        return True
    elif solve(ans, nums_plus):
        return True
    else: return solve(ans, nums_times)
    
def main():
    input = []
    with open("./input", "r") as f:
        for line in f:
            ans, rest = line.split(":")
            nums = list(map(int, rest.split()))
            nums.reverse()
            input.append((int(ans), nums))
        print(input)

    total = 0
    for ans, nums in input:
        if solve(ans, copy(nums)):
            print(ans)
            total += ans
    print(f"{total=}")


if __name__ == "__main__":
    main()
