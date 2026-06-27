import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
    profile: Dict[str, str]
    interests: list
    ideas: list

class OnboardingWizard:
    def __init__(self):
        self.steps = ["profile_setup", "interest_input", "first_idea_generation"]
        self.current_step = 0
        self.user = User({}, [], [])

    def profile_setup(self, name: str, email: str):
        self.user.profile = {"name": name, "email": email}
        self.current_step += 1

    def interest_input(self, interests: list):
        self.user.interests = interests
        self.current_step += 1

    def first_idea_generation(self):
        self.user.ideas = ["Idea 1", "Idea 2", "Idea 3"]
        self.current_step += 1

    def get_progress(self):
        return self.current_step / len(self.steps)

    def skip_step(self):
        if self.current_step < len(self.steps):
            self.current_step += 1

    def edit_inputs(self, profile: Dict[str, str] = None, interests: list = None):
        if profile:
            self.user.profile = profile
        if interests:
            self.user.interests = interests

    def submit(self):
        return self.user

    def save_onboarding_state(self):
        with open("onboarding_state.json", "w") as f:
            json.dump({"profile": self.user.profile, "interests": self.user.interests, "ideas": self.user.ideas}, f)

    def load_onboarding_state(self):
        try:
            with open("onboarding_state.json", "r") as f:
                state = json.load(f)
                self.user.profile = state["profile"]
                self.user.interests = state["interests"]
                self.user.ideas = state["ideas"]
        except FileNotFoundError:
            pass
