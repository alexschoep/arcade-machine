from json import load as json_load
from json import dump as json_dump

class HighScoreManager:
    persisted_scores = {
        "Pong": 3,
        "Snake": 3
    }

    SCORES_FILE_PATH = 'high_scores.json'

    def __init__(self):
        self.scores = self.load_scores()

    def load_scores(self):
        with open(self.SCORES_FILE_PATH, 'r') as f:
            return json_load(f)
            
    def save_scores(self):
        with open(self.SCORES_FILE_PATH, 'w') as f:
            json_dump(self.scores, f, indent=2)

    def get_high_scores(self, game):
        return self.scores[game]

    def check_if_high_score(self, game, new_score):
        if len(self.scores[game]) < self.persisted_scores[game]:
            return True
        if self.scores[game][-1]["score"] < new_score:
            return True
        return False

    def new_high_score(self, game, name, new_score):
        self.scores[game].append({"name": name, "score": new_score})
        self.scores[game].sort(key=lambda score: score['score'], reverse=True)
        self.scores[game] = self.scores[game][:self.persisted_scores[game]]
        self.save_scores()

high_score_manager = HighScoreManager()
