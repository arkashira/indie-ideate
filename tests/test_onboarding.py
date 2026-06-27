from onboarding import OnboardingWizard, User
import json

def test_profile_setup():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    assert wizard.user.profile == {"name": "John Doe", "email": "john@example.com"}

def test_interest_input():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.interest_input(["Reading", "Hiking"])
    assert wizard.user.interests == ["Reading", "Hiking"]

def test_first_idea_generation():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.interest_input(["Reading", "Hiking"])
    wizard.first_idea_generation()
    assert wizard.user.ideas == ["Idea 1", "Idea 2", "Idea 3"]

def test_get_progress():
    wizard = OnboardingWizard()
    assert wizard.get_progress() == 0
    wizard.profile_setup("John Doe", "john@example.com")
    assert wizard.get_progress() == 1/3
    wizard.interest_input(["Reading", "Hiking"])
    assert wizard.get_progress() == 2/3
    wizard.first_idea_generation()
    assert wizard.get_progress() == 1

def test_skip_step():
    wizard = OnboardingWizard()
    wizard.skip_step()
    assert wizard.current_step == 1

def test_edit_inputs():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.edit_inputs(profile={"name": "Jane Doe", "email": "jane@example.com"})
    assert wizard.user.profile == {"name": "Jane Doe", "email": "jane@example.com"}

def test_submit():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.interest_input(["Reading", "Hiking"])
    wizard.first_idea_generation()
    user = wizard.submit()
    assert user.profile == {"name": "John Doe", "email": "john@example.com"}
    assert user.interests == ["Reading", "Hiking"]
    assert user.ideas == ["Idea 1", "Idea 2", "Idea 3"]

def test_save_onboarding_state():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.interest_input(["Reading", "Hiking"])
    wizard.first_idea_generation()
    wizard.save_onboarding_state()
    with open("onboarding_state.json", "r") as f:
        state = json.load(f)
        assert state["profile"] == {"name": "John Doe", "email": "john@example.com"}
        assert state["interests"] == ["Reading", "Hiking"]
        assert state["ideas"] == ["Idea 1", "Idea 2", "Idea 3"]

def test_load_onboarding_state():
    wizard = OnboardingWizard()
    wizard.profile_setup("John Doe", "john@example.com")
    wizard.interest_input(["Reading", "Hiking"])
    wizard.first_idea_generation()
    wizard.save_onboarding_state()
    wizard.load_onboarding_state()
    assert wizard.user.profile == {"name": "John Doe", "email": "john@example.com"}
    assert wizard.user.interests == ["Reading", "Hiking"]
    assert wizard.user.ideas == ["Idea 1", "Idea 2", "Idea 3"]
