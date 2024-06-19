from collections import deque
from datetime import datetime


class StatusLogger:
    def __init__(self, max_size=100):
        self.log_queue = deque(maxlen=max_size)

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        self.log_queue.append(formatted_message)

    def get_logs(self):
        logs = list(self.log_queue)
        self.log_queue.clear()
        return logs


status_logger = StatusLogger()
