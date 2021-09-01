"""Unit test module kb.

    Functions:
    test_display_contents()
    test_add_kb_entry()
"""

import re
import kb.kb as kb


def test_display_content(capfd):
    """Test if help text is returned."""
    kb.display_content("--help", "/home/$USER/kb/")
    captured = capfd.readouterr()
    help_regex = re.compile(r'Find snippets')
    assert help_regex.match(captured.out)

def setup_function(function):
    print("setting up", function)

def test_func1():
    """Always pass"""
    assert True
