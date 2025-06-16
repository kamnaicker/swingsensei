import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

ROOT = Path(__file__).resolve().parents[1]

from loader import loadIntents
from matcher import match_intent

pat2intent, _ = loadIntents(ROOT/"intents.json")

def test_greet_detection():
    assert match_intent("Hello there", pat2intent) == "greet"
