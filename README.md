# ANS Parser — Agent Name Service URI parser

A tiny, fast library that validates and breaks down `agent://` URIs used by ApexRegistry.
It turns a human-readable agent address into structured routing metadata.

## Why this exists
ApexRegistry uses a DNS-like addressing scheme for AI agents:
- `agent://apexreg.org/discovery`
- `agent://billing.apexreg.org/cardiology`
- `agent://pay.stripe.com/charge?sig=0xabc...`

This parser makes sure those addresses are well-formed and extracts the domain, capability path, and optional signature.

## Install
```bash
pip install apexreg-ans-parser
```
(For now, install from source by cloning this repo.)

## Usage (Python)
```python
from apexreg_ans_parser import parse_agent_uri

# Example 1: simple agent address
parsed = parse_agent_uri("agent://billing.apexreg.org/cardiology")
print(parsed)
# {
#   "scheme": "agent",
#   "domain": "billing.apexreg.org",
#   "capability_path": "cardiology",
#   "query_params": {}
# }

# Example 2: with signature
parsed = parse_agent_uri("agent://pay.stripe.com/charge?sig=0xabc123")
print(parsed["query_params"])  # {"sig": "0xabc123"}
```

## Supported format
Canonical form:
- `agent://[subdomain.]domain.tld/[capability][?sig=...]`

Examples:
- `agent://apexreg.org/discovery`
- `agent://logistics.dhl.com/route`
- `agent://pay.stripe.com/charge?sig=0xabc...`

## API
- `parse_agent_uri(uri: str) -> dict`
  - Raises `ValueError` if the URI is invalid.
  - Returns: `{scheme, domain, capability_path, query_params}`

## Development
- Python 3.9+
- Install dev deps: `pip install -e ".[dev]"`
- Run tests: `pytest`

## License
Apache-2.0
