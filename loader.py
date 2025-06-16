import json, re 
from pathlib import Path
from typing import Dict, List, Tuple

HERE = Path(__file__).resolve().parent 

def loadIntents(path: str| Path=HERE/"intents.json") -> Tuple[Dict[re.Pattern, str], Dict[str, List[str]]]:
    path = Path(path).expanduser().resolve()
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    pat2intent, intent2resp = {}, {}
    for intent, blob in data.items():
        intent2resp[intent] = blob["responses"]
        for pattern in blob["patterns"]:
            pat2intent[re.compile(pattern)] = intent
    return pat2intent, intent2resp
            