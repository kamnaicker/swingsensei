import random
from typing import Dict, List

def respond(intent: str, text: str,
            intent2resp: Dict[str,List[str]],
            memory: Dict[str,str]) -> str:
    if intent not in intent2resp:
        return "Sorry, I didn’t get that 🤔"
    template = random.choice(intent2resp[intent])
    return template.format(**memory)
