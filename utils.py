import json
from typing import Any, List

def extract_json_values(s: str) -> List[Any]:
    """
    Scan through s and decode all JSON values (objects, arrays, numbers, etc.)
    Returns a list of Python objects in the order they appear.
    """
    decoder = json.JSONDecoder()
    idx = 0
    results: List[Any] = []
    length = len(s)
    while idx < length:
        # skip whitespace until next possible JSON start
        if s[idx].isspace():
            idx += 1
            continue
        try:
            obj, end = decoder.raw_decode(s, idx)
            results.append(obj)
            idx = end
        except json.JSONDecodeError:
            # not a JSON at this position, skip one char and retry
            idx += 1
    return results