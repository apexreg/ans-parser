from __future__ import annotations
import re
from urllib.parse import parse_qs

# Pattern for agent://[subdomain.]domain.tld/[capability][?query]
# Domain must have at least one dot and a TLD of 2+ letters.
AGENT_URI_PATTERN = re.compile(
    r"^agent://"
    r"(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    r"(?:/(?P<path>[a-zA-Z0-9._/-]*))?"
    r"(?:\?(?P<query>.*))?$"
)

def parse_agent_uri(uri: str) -> dict:
    """
    Parse an agent:// URI into structured routing metadata.

    Returns:
        {
          "scheme": "agent",
          "domain": str,
          "capability_path": str,
          "query_params": dict
        }

    Raises:
        ValueError: If the URI is invalid.
    """
    if not isinstance(uri, str):
        raise ValueError("URI must be a string")

    match = AGENT_URI_PATTERN.match(uri)
    if not match:
        raise ValueError(f"Invalid agent URI: {uri}")

    domain = match.group("domain")
    path = match.group("path") or ""
    query_str = match.group("query") or ""

    # Parse query string into dict
    query_params = {}
    if query_str:
        for key, values in parse_qs(query_str).items():
            # parse_qs returns lists; take first value for simplicity
            query_params[key] = values[0] if values else ""

    return {
        "scheme": "agent",
        "domain": domain,
        "capability_path": path,
        "query_params": query_params,
    }
