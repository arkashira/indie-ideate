import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    name: str
    description: str
    market_trend: str
    user_feedback: List[str]

def validate_idea(idea: Idea) -> dict:
    """
    Validate an idea using market trends and user feedback.
    
    Args:
    idea (Idea): The idea to be validated.
    
    Returns:
    dict: A report outlining the idea's potential and suggested improvements.
    """
    report = {
        "idea_name": idea.name,
        "potential": 0,
        "suggested_improvements": []
    }
    
    if idea.market_trend == "growing":
        report["potential"] += 1
    elif idea.market_trend == "declining":
        report["potential"] -= 1
    
    for feedback in idea.user_feedback:
        if feedback == "positive":
            report["potential"] += 1
        elif feedback == "negative":
            report["potential"] -= 1
    
    if report["potential"] > 0:
        report["suggested_improvements"].append("Build and monetize the idea")
    else:
        report["suggested_improvements"].append("Improve the idea based on user feedback")
    
    return report

def generate_report(idea: Idea) -> str:
    """
    Generate a report outlining the idea's potential and suggested improvements.
    
    Args:
    idea (Idea): The idea to be validated.
    
    Returns:
    str: A JSON string representing the report.
    """
    report = validate_idea(idea)
    return json.dumps(report, indent=4)
