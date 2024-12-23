import tkinter as tk

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack()

    def start_timer(self):
        print("Timer started!")

    def pause_timer(self):
        print("Timer paused!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
