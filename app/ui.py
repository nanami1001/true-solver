import tkinter as tk
from tkinter import ttk, messagebox
from solver import find_expression as find_basic_expression
from solverad import find_expression as find_advanced_expression

class App:
    def __init__(self, root):  # <== 修正這裡
        self.root = root
        root.title("迫真計算器")
        root.geometry("400x400")
        root.resizable(False, False)

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        ttk.Label(self.root, text="迫真計算器", font=("Arial", 20)).pack(pady=30)
        ttk.Button(self.root, text="進入初階功能", command=self.basic_mode, width=25).pack(pady=10)
        ttk.Button(self.root, text="進入進階功能", command=self.advanced_mode, width=25).pack(pady=10)

    def basic_mode(self):
        self.show_solver_ui(mode="初階", digits=[int(c) for c in "114514"], is_advanced=False)

    def advanced_mode(self):
        self.show_solver_ui(mode="進階", digits=[int(c) for c in "1145141919810"], is_advanced=True)

    def show_solver_ui(self, mode, digits, is_advanced):
        self.clear_window()
        self.current_digits = digits
        self.is_advanced = is_advanced

        ttk.Label(self.root, text=f"{mode} 模式", font=("Arial", 16)).pack(pady=10)

        ttk.Label(self.root, text="請輸入整數目標值：").pack()
        self.input_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.input_var, width=20).pack(pady=5)

        ttk.Label(self.root, text=f"使用數字：{''.join(map(str, digits))}").pack(pady=5)

        ttk.Button(self.root, text="計算", command=self.calculate).pack(pady=5)

        ttk.Label(self.root, text="算式結果：").pack(pady=5)
        self.output_box = tk.Text(self.root, height=6, width=45, wrap="word")
        self.output_box.pack(pady=5)

        ttk.Button(self.root, text="回主選單", command=self.main_menu).pack(pady=10)

    def calculate(self):
        try:
            target = int(self.input_var.get())
            digits = self.current_digits
            if self.is_advanced:
                result = find_advanced_expression(target, digits)
            else:
                result = find_basic_expression(target, digits)

            self.output_box.delete("1.0", tk.END)
            if result:
                self.output_box.insert(tk.END, f"{result} = {target}")
            else:
                self.output_box.insert(tk.END, "找不到符合的表達式。")
        except ValueError:
            messagebox.showerror("錯誤", "請輸入正確的整數")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ✅ 加入主程式啟動 GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
