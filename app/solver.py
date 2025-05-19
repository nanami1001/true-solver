from utils import safe_eval
from collections import deque

ops = ['+', '-', '*', '/', '%', '//', '**']

def split_numbers(nums, start=0):
    if start == len(nums):
        return [[]]
    results = []
    for end in range(start+1, len(nums)+1):
        number = int(''.join(map(str, nums[start:end])))
        for rest in split_numbers(nums, end):
            results.append([number] + rest)
    return results

def find_expression(target, nums):
    splits = split_numbers(nums)
    splits = sorted(splits, key=lambda x: len(x))  # 優先少分割數

    for split in splits:
        if len(split) == 1:
            if abs(split[0] - target) < 1e-9:
                return str(split[0])
            continue

        queue = deque()
        queue.append((str(split[0]), 0, 1))  # (expr, op_count, idx)

        while queue:
            expr, op_count, idx = queue.popleft()

            if idx == len(split):
                try:
                    if abs(safe_eval(expr) - target) < 1e-9:
                        return expr
                except:
                    continue
            else:
                for op in ops:
                    new_expr = f"({expr}{op}{split[idx]})"
                    queue.append((new_expr, op_count + 1, idx + 1))

    return None
