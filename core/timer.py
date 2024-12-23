import time

class PomodoroTimer:
    def __init__(self, work_duration):
        self.work_duration = work_duration
        self.time_left = work_duration
        self.running = False

    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02}:{seconds:02}"
    
    def start(self, update_callback):
        self.running = True
        while self.running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            update_callback()
        self.running = False

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.current_time = self.work_duration
