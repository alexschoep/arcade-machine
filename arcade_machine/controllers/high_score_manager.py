from json import load as json_load
from json import dump as json_dump

class HighScoreManager:
    SCORES_FILE_PATH = 'high_scores.json'

    def new_score(self, game: str, new_score: dict):
        # new score must have a "score" attribute
        with open(self.SCORES_FILE_PATH, 'r') as f:
            high_scores = json_load(f)

            game_high_scores = high_scores[game]
            persist_count = game_high_scores["persist_count"]
            scores = game_high_scores["scores"]
            scores.append(new_score)
            scores.sort(key=lambda score: score['score'], reverse=True)
            game_high_scores["scores"] = scores[:persist_count]

        with open(self.SCORES_FILE_PATH, 'w') as f:
            json_dump(high_scores, f, indent=2)

    def get_high_scores(self, game):
        with open(self.SCORES_FILE_PATH, 'r') as f:
            return json_load(f)[game]