from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Step:
    tool_name: Optional[str]
    tool_input: Optional[dict]
    tool_output: Optional[Any]
