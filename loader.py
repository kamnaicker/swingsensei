import json, re 
from pathlib import Path
from typing import Dict, List, Tuple

def loadIntents(path: str| Path) -> Tuple[Dict[re.Pattern, str], Dict[str, List[str]]]:
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    pat2intent, intent2resp = {}, {}
    for intent, blob in data.items():
        intent2resp[intent] = blob["responses"]
        for pattern in blob["patterns"]:
            pat2intent[re.compile(pattern)] = intent
    return pat2intent, intent2resp
            