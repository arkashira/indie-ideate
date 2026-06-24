from src.websocket import WebSocket
from src.dashboard import Idea
import json

def test_send_ideas():
    websocket = WebSocket()
    idea = Idea(1, "Test Idea", 0.5, 10, "template")
    websocket.dashboard.add_idea(idea)
    message = websocket.send_ideas()
    assert json.loads(message)["type"] == "ideas"
    assert len(json.loads(message)["data"]) == 1

def test_update_idea():
    websocket = WebSocket()
    idea = Idea(1, "Test Idea", 0.5, 10, "template")
    websocket.dashboard.add_idea(idea)
    updated_message = websocket.update_idea(1, 0.7, 20, "new template")
    assert json.loads(updated_message)["type"] == "ideas"
    assert len(json.loads(updated_message)["data"]) == 1
    assert json.loads(updated_message)["data"][0]["validation_score"] == 0.7
