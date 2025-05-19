# app.py
# CLI 介面：輸入一個數字，列出可能的運算式

from solver import find_expression

def main():
    target = int(input("請輸入目標數字："))
    result = find_expression(target)
    if result:
        print(f"找到表達式：{result} = {target}")
    else:
        print("找不到符合的表達式。")

if __name__ == "__main__":
    main()