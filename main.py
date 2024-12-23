def main():
    from gui.main_window import PomodoroApp
    import tkinter as tk

    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()