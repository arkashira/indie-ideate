from idea_validator import Idea, validate_idea, generate_report

def test_validate_idea_positive():
    idea = Idea("Test Idea", "This is a test idea", "growing", ["positive", "positive"])
    report = validate_idea(idea)
    assert report["potential"] == 3
    assert report["suggested_improvements"] == ["Proceed with development"]

def test_validate_idea_negative():
    idea = Idea("Test Idea", "This is a test idea", "declining", ["negative", "negative"])
    report = validate_idea(idea)
    assert report["potential"] == -3
    assert report["suggested_improvements"] == ["Reconsider the idea"]

def test_generate_report():
    idea = Idea("Test Idea", "This is a test idea", "growing", ["positive", "positive"])
    report = generate_report(idea)
    assert "Test Idea" in report
    assert "Proceed with development" in report

def test_edge_case_empty_user_feedback():
    idea = Idea("Test Idea", "This is a test idea", "growing", [])
    report = validate_idea(idea)
    assert report["potential"] == 1
    assert report["suggested_improvements"] == ["Proceed with development"]
