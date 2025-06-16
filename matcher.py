import re
from typing import Dict

def match_intent(text: str, pat2intent: Dict[re.Pattern,str], default="unknown") -> str:
    for rgx, intent in pat2intent.items():
        if rgx.search(text):
            return intent
    return default
