import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    id: int
    name: str
    validation_score: float
    competitor_count: int
    monetization_template: str

class Dashboard:
    def __init__(self):
        self.ideas = []

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def get_ideas(self):
        return self.ideas

    def update_idea(self, idea_id: int, validation_score: float, competitor_count: int, monetization_template: str):
        for idea in self.ideas:
            if idea.id == idea_id:
                idea.validation_score = validation_score
                idea.competitor_count = competitor_count
                idea.monetization_template = monetization_template
                break

    def get_idea(self, idea_id: int):
        for idea in self.ideas:
            if idea.id == idea_id:
                return idea
        return None
