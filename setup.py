"""Setup and test.

    Enable running "python setup.py test",
    so that pytest and pylint are run."""
from setuptools import setup, find_packages

setup(
    name="kb",
    version="0.1.0",
    description="Find snippets. Add snippets.",
    url="https://github.com/sukkis/kb",
    packages=find_packages(include=["kb", "kb.*"]),
    setup_requires=["pytest-runner", "pytest-pylint"],
    tests_require=["pytest", "pylint"],
)
