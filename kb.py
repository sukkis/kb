"""Find snippets. Add snippets.

kb is a Python3 script for searching through little snippets,
stored under /home/$USER/kb. For easy use, add alias "kb" to run "/path/to/your/python/ kb.py".

Synopsis
    kb [OPTION] [SEARCH WORD]

    E.g. if you have added "kb" as an alias like above, search with "kb vpn" for kb article
    "how-to-access-work-vpn" under your /home/$USER/kb directory.

Options:
    --help        Show help text.
    --add         Prompt user for input, add snippet with title and content.
    Help text is also shown if you do not give any arguments.
"""

import os
import sys


# Constants
DIR = os.path.expandvars("/home/$USER/kb/")
HOME = os.path.expandvars("/home/$USER")
TEMP_FILE = HOME + "/temp/search"

# If no arguments given, help page is displayed.
if len(sys.argv) > 1:
    SEARCH_STRING = sys.argv[1]
else:
    SEARCH_STRING = "--help"


def display_content(search_string, directory):
    """Show contents of matching files.

    Displays content if name of file matches search string.
    Help page "man-kb" is just another kb article snippet,
    accessed with "--help" or without arguments.
    """
    if SEARCH_STRING == "--help" or SEARCH_STRING == "":
        return print(__doc__)

    cmd = (
        "cd "
        + directory
        + "; ls "
        + directory
        + " | grep "
        + search_string
        + " | xargs cat > "
        + TEMP_FILE
    )
    os.system(cmd)
    fetch_content_from_file = "cat " + TEMP_FILE
    return print(os.system(fetch_content_from_file))


def add_kb_entry(directory):
    """Place the user provided snippet as a file.

    The temporary file can be later used in searches.
    """

    title = input("Provide a title for the snippet, without spaces: ")
    if len(title) > 1:
        lines = []
        print("Provide content. Empty line stops this.")

        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        content = "\n".join(lines)
        filename = directory + title.lower()
        with open(filename, "w") as file_object:
            file_object.write(content)
    else:
        print("Cannot add a snippet without a valid name.")


def main():
    """Select functions based on command line arguments (search string)."""
    if SEARCH_STRING == "--add":
        add_kb_entry(DIR)
    else:
        display_content(SEARCH_STRING, DIR)


main()
