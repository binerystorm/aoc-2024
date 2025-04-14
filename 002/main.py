#! /bin/python3
def role_win(l):
    for i in range(len(l)-1):
        yield l[i:i+2]


def check_report(report: list[int]):
    prev_dir = None
    for a, b in role_win(report):
        diff = a - b
        abs_diff = abs(diff)
        if not (0 < abs_diff < 4):
            return False
        
        dir = diff/abs_diff
        if prev_dir is None:
            prev_dir = dir
        elif prev_dir != dir:
            return False
    return True

def check_report_with_err_loc(report: list[int]):
    prev_dir = None
    for i, (a, b) in enumerate(role_win(report)):
        diff = a - b
        abs_diff = abs(diff)
        if not (0 < abs_diff < 4):
            return False, i
        
        dir = diff/abs_diff
        if prev_dir is None:
            prev_dir = dir
        elif prev_dir != dir:
            return False, i
    return True, 0

def check_report_with_damp(report: list[int]):
    passed, err_loc = check_report_with_err_loc(report)
    if passed: return True
    new_report = report.copy()
    new_report.pop(err_loc)
    passed, _ = check_report_with_err_loc(new_report)
    if passed: return True
    new_report = report.copy()
    new_report.pop(err_loc+1)
    passed, _ = check_report_with_err_loc(new_report)
    if passed: return True
    return False

def check_report_with_damp_slow(report: list[int]):
    if check_report(report): return True
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if check_report(new_report): return True
    return False

def main():
    reports = []
    with open("./input", "r") as f:
        for report in f:
            reports.append(list(map(int, report.split())))

    total_fast = 0
    total_slow = 0
    for report in reports:
        passed_slow = check_report_with_damp_slow(report)
        passed_fast = check_report_with_damp(report)
        #print(passed_slow, passed_fast)
        if passed_fast: total_fast += 1
        if passed_slow: total_slow += 1
        if passed_slow != passed_fast:
            print(report)
            print(f"{passed_fast=}")
            print(f"{passed_slow=}")

    print(total_fast)
    print(total_slow)
if __name__ == "__main__":
    main()
