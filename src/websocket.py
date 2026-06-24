import json
from dataclasses import dataclass
from typing import List
from dashboard import Dashboard

@dataclass
class Message:
    type: str
    data: dict

class WebSocket:
    def __init__(self):
        self.dashboard = Dashboard()

    def send_ideas(self):
        ideas = self.dashboard.get_ideas()
        message = Message("ideas", [idea.__dict__ for idea in ideas])
        return json.dumps(message.__dict__)

    def update_idea(self, idea_id: int, validation_score: float, competitor_count: int, monetization_template: str):
        self.dashboard.update_idea(idea_id, validation_score, competitor_count, monetization_template)
        return self.send_ideas()
