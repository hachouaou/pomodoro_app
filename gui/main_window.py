import tkinter as tk
import threading
from core.timer import PomodoroTimer

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        
        self.timer = PomodoroTimer(work_duration=50*60)
        
        self.timer_label = tk.Label(root, text=self.timer.format(), font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=10)

        self.reset_button = tk.Button(root, test='Reset', command=self.reset_timer)

    def update_ui(self):
        self.timer_label.config(text=self.timer.format_time())
        if not self.timer.running and self.timer.time_left == 0:
            self.timer_label.config(text="Time's Up!")

    def start_timer(self):
        if not self.timer.running:
            threading.Thread(target=self.timer.start, args=(self.update_ui,)).start()

    def pause_timer(self):
        self.timer.pause()

    def reset_timer(self):
        self.timer.pause()
        self.update_ui()