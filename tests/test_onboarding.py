import pytest
from onboarding import OnboardingWizard, User

def test_start_onboarding():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    assert "user1" in wizard.user_profile

def test_input_skills():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.input_skills("user1", ["skill1", "skill2"])
    assert wizard.user_profile["user1"].skills == ["skill1", "skill2"]

def test_generate_ideas():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.input_skills("user1", ["skill1", "skill2"])
    ideas = wizard.generate_ideas("user1")
    assert ideas == ["Idea 0 for skill1", "Idea 1 for skill2"]

def test_validate_ideas():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.input_skills("user1", ["skill1", "skill2"])
    wizard.generate_ideas("user1")
    validation_overview = wizard.validate_ideas("user1")
    assert validation_overview == "Validation overview for Idea 0 for skill1, Idea 1 for skill2"

def test_select_template():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.select_template("user1", "template1")
    assert wizard.user_profile["user1"].template == "template1"

def test_get_user_profile():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.input_skills("user1", ["skill1", "skill2"])
    wizard.generate_ideas("user1")
    wizard.validate_ideas("user1")
    wizard.select_template("user1", "template1")
    user_profile = wizard.get_user_profile("user1")
    assert user_profile == {
        "skills": ["skill1", "skill2"],
        "ideas": ["Idea 0 for skill1", "Idea 1 for skill2"],
        "validation_overview": "Validation overview for Idea 0 for skill1, Idea 1 for skill2",
        "template": "template1"
    }

def test_skip_onboarding():
    wizard = OnboardingWizard()
    wizard.start_onboarding("user1")
    wizard.skip_onboarding("user1")
    assert "user1" not in wizard.user_profile
