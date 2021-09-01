"""Unit test module kb.

    Functions:
    test_display_contents()
    test_add_kb_entry()
"""

import re
import kb.kb as kb


def test_display_content():
    """Test if help text is returned."""
    help_contents = str(kb.display_content("--help", "/home/$USER/kb/"))
    help_regex = re.compile(r'Find snippets')
    assert help_regex.match(help_contents)
