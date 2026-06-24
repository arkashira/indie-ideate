import datetime
from validation_engine import ValidationEngine, Idea

def test_get_demand_score():
    engine = ValidationEngine()
    idea = Idea('test_keyword')
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50

def test_get_trend_graph_data():
    engine = ValidationEngine()
    idea = Idea('test_keyword')
    trend_graph_data = engine.get_trend_graph_data(idea)
    assert trend_graph_data == {'2022-01-01': 10, '2022-01-02': 20, '2022-01-03': 30}

def test_cache():
    engine = ValidationEngine()
    idea = Idea('test_keyword')
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50
    # Simulate cache expiration
    engine.cache[idea.keyword]['expires'] = datetime.datetime(2022, 1, 1)
    demand_score = engine.get_demand_score(idea)
    assert demand_score == 50

def test_edge_case():
    engine = ValidationEngine()
    idea = Idea(None)
    try:
        demand_score = engine.get_demand_score(idea)
    except ValueError:
        assert True
    else:
        assert False, 'Expected ValueError'
