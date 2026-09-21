import pytest
from apexreg_ans_parser import parse_agent_uri

def test_simple_uri():
    uri = "agent://apexreg.org/discovery"
    parsed = parse_agent_uri(uri)
    assert parsed["scheme"] == "agent"
    assert parsed["domain"] == "apexreg.org"
    assert parsed["capability_path"] == "discovery"
    assert parsed["query_params"] == {}

def test_subdomain_uri():
    uri = "agent://billing.apexreg.org/cardiology"
    parsed = parse_agent_uri(uri)
    assert parsed["domain"] == "billing.apexreg.org"
    assert parsed["capability_path"] == "cardiology"

def test_uri_with_signature():
    uri = "agent://pay.stripe.com/charge?sig=0xabc123"
    parsed = parse_agent_uri(uri)
    assert parsed["domain"] == "pay.stripe.com"
    assert parsed["capability_path"] == "charge"
    assert parsed["query_params"]["sig"] == "0xabc123"

def test_empty_capability_path():
    uri = "agent://apexreg.org"
    parsed = parse_agent_uri(uri)
    assert parsed["capability_path"] == ""

def test_invalid_uri_no_scheme():
    with pytest.raises(ValueError):
        parse_agent_uri("http://apexreg.org/discovery")

def test_invalid_uri_bad_domain():
    with pytest.raises(ValueError):
        parse_agent_uri("agent://notadomain/discovery")
