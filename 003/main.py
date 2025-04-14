#! /bin/python3
def role_win(l):
    for i in range(len(l)-3):
        yield l[i:i+4]

def parse_int(s:str, start_loc):
    num = []
    for d in s[start_loc:start_loc+3]:
        if d.isdigit():
            num.append(d)
        else: break
    if len(num) == 0: return 0, 0
    if start_loc + len(num) >= len(s) and s[start_loc + len(num)] not in (',', ')'): return 0, 0
    return int("".join(num)), start_loc + len(num)

def strneq(s1, s2, n):
    if len(s1) < n or len(s2) < n: return False
    for i in range(n):
        if s1[i] != s2[i]: return False
    return True

def lex(input: str) -> (str, int):
    i = 0
    cmd = []
    while i < len(input):
        if strneq(input[i:], "mul(", len("mul(")):
            yield "mul(", i + len("mul(")
        if strneq(input[i:], "do()", len("do()")): 
            yield "do()", i + len("do()")
        if strneq(input[i:], "don't()", len("don't()")):
            yield "don't()", i + len("don't()")
        i += 1



def parse(input: str) -> list[tuple[int, int]]:
    out = []
    do = True
    for s, i in lex(input):
        if s == "mul(" and do: 
            a, x = parse_int(input, i)
            if x == 0 or input[x] != ',': continue
            b, x = parse_int(input, x+1)
            if x == 0 or input[x] != ')': continue
            print(f"{a} * {b} = {a*b}")
            out.append((a,b))
        if s == "do()":
            do = True
        if s == "don't()":
            do = False
    return out

def main():
    with open("./input", "r") as f:
        input = "".join(f.readlines())
    print(sum(map(lambda x: x[0] * x[1], parse(input))))
    

if __name__ == "__main__":
    main()
