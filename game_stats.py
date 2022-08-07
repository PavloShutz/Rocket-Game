class GameStats:
    def __init__(self):
        self.save_file = "score.txt"
        try:
            with open(self.save_file, "r") as f:
                self.score = int(f.read())
        except (FileNotFoundError, ValueError):
            with open(self.save_file, "w") as f:
                f.write('0')
                self.score = 0

    def save_current_score(self, score):
        with open(self.save_file, "w") as f:
            f.write(str(score))
