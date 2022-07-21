"""
Test Project with Anaconda and no ReadTheDocs
A short description of the project.
"""

# Add imports here
from .test_mda_conda_nortd import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
