from src.dashboard import Dashboard, Idea

def test_add_idea():
    dashboard = Dashboard()
    idea = Idea(1, "Test Idea", 0.5, 10, "template")
    dashboard.add_idea(idea)
    assert len(dashboard.get_ideas()) == 1

def test_get_ideas():
    dashboard = Dashboard()
    idea1 = Idea(1, "Test Idea 1", 0.5, 10, "template")
    idea2 = Idea(2, "Test Idea 2", 0.7, 20, "template")
    dashboard.add_idea(idea1)
    dashboard.add_idea(idea2)
    ideas = dashboard.get_ideas()
    assert len(ideas) == 2
    assert ideas[0].id == 1
    assert ideas[1].id == 2

def test_update_idea():
    dashboard = Dashboard()
    idea = Idea(1, "Test Idea", 0.5, 10, "template")
    dashboard.add_idea(idea)
    dashboard.update_idea(1, 0.7, 20, "new template")
    updated_idea = dashboard.get_idea(1)
    assert updated_idea.validation_score == 0.7
    assert updated_idea.competitor_count == 20
    assert updated_idea.monetization_template == "new template"

def test_get_idea():
    dashboard = Dashboard()
    idea = Idea(1, "Test Idea", 0.5, 10, "template")
    dashboard.add_idea(idea)
    retrieved_idea = dashboard.get_idea(1)
    assert retrieved_idea.id == 1
    assert retrieved_idea.name == "Test Idea"
