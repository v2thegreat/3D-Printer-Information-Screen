from test_Config import test_Configs
from test_Defaults import test_Defaults
from test_Personnel import test_Personnel
try:
    from test_BackendStatics import test_BackendStatics
except:
    print('Issue with importing test_BackendStatics, not running tests')
    pass

from sys import path
path.append('../')
from Personnel import Personnel


"""
This is main test file where all other tests are imported and run.
This can be as simple as running it from the console it self.

Further, this one tests makes sure the following are working as expected:

    - Packages:
        - Configs
        - Defaults

    - Classes:
        - BackendStatics
        - Personnel

    - Tests:
        - test_Config
        - test_Defaults
        - test_BackendStatics
        - test_Personnel


Developers Note:
    Personnel is imported here because of it's reliance on the pickle module
        This is a dirty solution to import the original Personnel class, but
        it's the most reliable one.

        It most likely does this because it needs to ensure that there haven't
        been any modifications to the original class, but this is just a theory
"""

if __name__ == '__main__':
    from unittest import main
    main()
