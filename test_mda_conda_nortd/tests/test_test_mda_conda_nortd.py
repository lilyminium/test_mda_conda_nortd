"""
Unit and regression test for the test_mda_conda_nortd package.
"""

# Import package, test suite, and other packages as needed
import test_mda_conda_nortd
import pytest
import sys


def test_test_mda_conda_nortd_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "test_mda_conda_nortd" in sys.modules


def test_mdanalysis_logo_length(mdanalysis_logo_text):
    """Example test using a fixture defined in conftest.py"""
    logo_lines = mdanalysis_logo_text.split("\n")
    assert len(logo_lines) == 46, "Logo file does not have 46 lines!"
