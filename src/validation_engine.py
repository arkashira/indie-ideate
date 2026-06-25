import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class Idea:
    keyword: str
    demand_score: int = 0
    trend_graph_data: Dict[str, int] = None

class ValidationEngine:
    def __init__(self):
        self.cache = {}

    def get_demand_score(self, idea: Idea) -> int:
        if idea.keyword in self.cache:
            cache_entry = self.cache[idea.keyword]
            if cache_entry['expires'] > datetime.now():
                return cache_entry['demand_score']
        # Simulate API call to Google Trends and Ahrefs
        demand_score = self.simulate_api_call(idea.keyword)
        self.cache[idea.keyword] = {
            'demand_score': demand_score,
            'expires': datetime.now() + timedelta(hours=24)
        }
        return demand_score

    def get_trend_graph_data(self, idea: Idea) -> Dict[str, int]:
        # Simulate API call to Google Trends and Ahrefs
        trend_graph_data = self.simulate_api_call(idea.keyword)
        return {'data': trend_graph_data}

    def simulate_api_call(self, keyword: str) -> int:
        # Simulate API call to Google Trends and Ahrefs
        # For demonstration purposes, return a fixed value
        return 50

    def analyze_search_volume_and_keyword_trends(self, idea: Idea) -> Idea:
        idea.demand_score = self.get_demand_score(idea)
        idea.trend_graph_data = self.get_trend_graph_data(idea)
        return idea
