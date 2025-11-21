
class Logger():
    def __init__(self):
        self.logs = []
    def log(self, message):
        self.logs.append(message)
    def save(self):
        with open("log.txt", "w", encoding="utf-8") as f:
            for log in self.logs:
                f.write(log+'\n')