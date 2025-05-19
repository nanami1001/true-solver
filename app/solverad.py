from utils import safe_eval
from collections import deque

# 為了效能與安全性，先只用這三種運算符
ops = ['+', '-', '*']

def split_numbers(nums, start=0):
    if start == len(nums):
        return [[]]
    results = []
    for end in range(start + 1, len(nums) + 1):
        number = int(''.join(map(str, nums[start:end])))
        for rest in split_numbers(nums, end):
            results.append([number] + rest)
    return results

def find_expression(target, digits):
    MAX_SPLIT_LENGTH = 6        # 限制最大拆分長度
    MAX_TRIES = 100_000         # 限制最大嘗試次數
    tries = 0

    splits = split_numbers(digits)
    splits = [s for s in splits if len(s) <= MAX_SPLIT_LENGTH]
    splits.sort(key=lambda x: len(x))  # 優先簡短組合

    for split in splits:
        queue = deque()
        visited = set()
        queue.append((str(split[0]), 0, 1))  # (目前表達式, 運算符數量, 下個數字索引)

        while queue:
            if tries > MAX_TRIES:
                return None  # 安全退出，防止運算過久
            tries += 1

            expr, op_count, idx = queue.popleft()
            if (expr, idx) in visited:
                continue
            visited.add((expr, idx))

            if idx == len(split):
                try:
                    if abs(safe_eval(expr) - target) < 1e-9:
                        return expr
                except:
                    continue
            else:
                for op in ops:
                    next_expr = f"({expr}{op}{split[idx]})"
                    queue.append((next_expr, op_count + 1, idx + 1))
    return None
