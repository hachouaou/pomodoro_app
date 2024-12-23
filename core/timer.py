import time

class Pomodoro_timer():
    def __init__(self, work_duration=50*60, break_duration=10*60):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.current_time = work_duration
        self.running = False

    def start(self):
        self.running = True
        while self.running and self.work_duration > 0:
            print(f'Time left {self.current_time//60}:{self.current_time % 60}')
            time.sleep(1)
            self.current_time =-1

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.current_time = self.work_duration
