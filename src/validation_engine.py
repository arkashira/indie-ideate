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
        if idea.keyword is None:
            raise ValueError("Keyword cannot be None")

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
        trend_graph_data = self.simulate_api_call(idea.keyword, trend=True)
        return trend_graph_data

    def simulate_api_call(self, keyword: str, trend: bool = False) -> int or Dict[str, int]:
        # Simulate API call to Google Trends and Ahrefs
        # For demonstration purposes, return a fixed value
        if trend:
            return {'2022-01-01': 10, '2022-01-02': 20, '2022-01-03': 30}
        else:
            return 50

def main():
    engine = ValidationEngine()
    idea = Idea('test_keyword')
    demand_score = engine.get_demand_score(idea)
    trend_graph_data = engine.get_trend_graph_data(idea)
    print(f'Demand score: {demand_score}')
    print(f'Trend graph data: {trend_graph_data}')

if __name__ == '__main__':
    main()
