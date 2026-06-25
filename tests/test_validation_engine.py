from datetime import datetime, timedelta
from validation_engine import Idea, ValidationEngine

def test_get_demand_score():
    engine = ValidationEngine()
    idea = Idea(keyword='test')
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50

def test_get_trend_graph_data():
    engine = ValidationEngine()
    idea = Idea(keyword='test')
    trend_graph_data = engine.get_trend_graph_data(idea)
    assert trend_graph_data == {'data': 50}

def test_analyze_search_volume_and_keyword_trends():
    engine = ValidationEngine()
    idea = Idea(keyword='test')
    analyzed_idea = engine.analyze_search_volume_and_keyword_trends(idea)
    assert analyzed_idea.demand_score == 50
    assert analyzed_idea.trend_graph_data == {'data': 50}

def test_cache_expiration():
    engine = ValidationEngine()
    idea = Idea(keyword='test')
    engine.cache[idea.keyword] = {
        'demand_score': 50,
        'expires': datetime.now() - timedelta(hours=1)
    }
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50
    assert idea.keyword in engine.cache

def test_cache_hit():
    engine = ValidationEngine()
    idea = Idea(keyword='test')
    engine.cache[idea.keyword] = {
        'demand_score': 50,
        'expires': datetime.now() + timedelta(hours=1)
    }
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50
