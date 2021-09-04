"""Unit test module kb.

    Functions:
    test_display_content()
    test_add_kb_entry()
"""

import re
import os
from kb import kb


# Constants
DIR = os.path.expandvars("/home/$USER/kb/")
HOME = os.path.expandvars("/home/$USER")
TEMP_FILE = HOME + "/temp/search"


def test_display_content(capfd):
    """Test if help text is returned."""
    kb.display_content("--help", DIR)
    captured = capfd.readouterr()
    help_regex = re.compile(r"Find snippets")
    assert help_regex.match(captured.out)


def setup_function(function):
    """Dummy setup function."""
    print("setting up", function)


def test_func1():
    """Always pass"""
    assert True
