import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class User:
    skills: List[str]
    ideas: List[str]
    validation_overview: str
    template: str

class OnboardingWizard:
    def __init__(self):
        self.user_profile = {}

    def start_onboarding(self, user_id: str) -> None:
        self.user_profile[user_id] = User([], [], "", "")

    def input_skills(self, user_id: str, skills: List[str]) -> None:
        self.user_profile[user_id].skills = skills

    def generate_ideas(self, user_id: str) -> List[str]:
        # Simple idea generation based on skills
        ideas = [f"Idea {i} for {skill}" for i, skill in enumerate(self.user_profile[user_id].skills)]
        self.user_profile[user_id].ideas = ideas
        return ideas

    def validate_ideas(self, user_id: str) -> str:
        # Simple validation overview based on ideas
        validation_overview = "Validation overview for " + ", ".join(self.user_profile[user_id].ideas)
        self.user_profile[user_id].validation_overview = validation_overview
        return validation_overview

    def select_template(self, user_id: str, template: str) -> None:
        self.user_profile[user_id].template = template

    def get_user_profile(self, user_id: str) -> Dict:
        return {
            "skills": self.user_profile[user_id].skills,
            "ideas": self.user_profile[user_id].ideas,
            "validation_overview": self.user_profile[user_id].validation_overview,
            "template": self.user_profile[user_id].template
        }

    def skip_onboarding(self, user_id: str) -> None:
        del self.user_profile[user_id]
