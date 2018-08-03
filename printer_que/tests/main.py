from test_Config import test_Configs
from test_Defaults import test_Defaults
from test_BackendStatics import test_BackendStatics
from test_Personnel import test_Personnel

from sys import path
path.append('../')
from Personnel import Personnel

"""
This is main test file where all other tests are imported and run.
This can be as simple as running it from the consoleself.

Developers Note:
    Personnel is imported here because of it's reliance on pickle
        This is a dirty solution but the only one
"""

if __name__ == '__main__':
    from unittest import main
    main()
