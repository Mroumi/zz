import tkinter as tk
import time

# 设置工作和休息时间（以秒为单位）
WORK_TIME = 25 * 60  # 25分钟
BREAK_TIME = 5 * 60  # 5分钟


class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟 (Pomodoro)")

        # 初始状态：工作
        self.is_working = True
        self.time_left = WORK_TIME

        # 创建UI元素
        self.label = tk.Label(root, text="开始工作", font=("Arial", 24))
        self.label.pack(pady=10)

        self.timer_label = tk.Label(root, text=self.format_time(self.time_left), font=("Arial", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="开始", font=("Arial", 16), command=self.start_timer)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="重置", font=("Arial", 16), command=self.reset_timer)
        self.reset_button.pack(pady=10)

        self.root.after(1000, self.update_timer)

    def format_time(self, seconds):
        """将秒数转换为分钟:秒 格式"""
        minutes = seconds // 60
        seconds = seconds % 60
        return
