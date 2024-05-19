import pytest


def test_hav_api_key():
    """
    test api file is present
    """
    try:
        from expert_advisor.apikey import key
    except ImportError:
        raise Exception("api key not present read readme.md")
    
