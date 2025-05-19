def safe_eval(expr):
    """
    簡易安全計算函式，只允許數字與 + - * / % // ** () 運算符。
    避免使用 eval 造成安全問題。
    """
    allowed_chars = "0123456789+-*/%() //.**"
    # 其實要精準判斷運算子，這裡簡化為判斷字元
    for c in expr:
        if c not in "0123456789+-*/%() .":
            raise ValueError("含有不允許的字元")
    try:
        return eval(expr)
    except Exception as e:
        raise ValueError(f"無效表達式: {expr}") from e
