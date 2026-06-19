from idea_validator import Idea, validate_idea, generate_report

def test_validate_idea():
    idea = Idea("Test Idea", "This is a test idea", "growing", ["positive", "positive"])
    report = validate_idea(idea)
    assert report["potential"] == 3
    assert "Build and monetize the idea" in report["suggested_improvements"]

def test_validate_idea_declining_market():
    idea = Idea("Test Idea", "This is a test idea", "declining", ["positive", "positive"])
    report = validate_idea(idea)
    assert report["potential"] == 1
    assert "Build and monetize the idea" in report["suggested_improvements"]

def test_validate_idea_negative_feedback():
    idea = Idea("Test Idea", "This is a test idea", "growing", ["negative", "negative"])
    report = validate_idea(idea)
    assert report["potential"] == -1
    assert "Improve the idea based on user feedback" in report["suggested_improvements"]

def test_generate_report():
    idea = Idea("Test Idea", "This is a test idea", "growing", ["positive", "positive"])
    report = generate_report(idea)
    assert "Test Idea" in report
    assert "potential" in report
    assert "suggested_improvements" in report
