import sys

# The pyyaml offical dropped support for Python < 3.6 in its latest version.
# To make our program still available in earlier versions of Python,
# we select an older version of pyyaml manually. (Not Recommend)

PYYAML_VERSION = 'pyyaml' if sys.version_info >= (3, 6, 0) else 'pyyaml==5.3'
