"""
Unit Tests to ensure that Configs are set properly
"""

import sys
sys.path.append('../')

from unittest import TestCase, main


class test_Configs(TestCase):
    """
    Tests for Configs.py

    These tests are to ensure that the configs are set properly

    The Following tests are included:
        - Ensuring API_KEY is usable
        - Ensuring SCREEN_RESOLUTION is imported
        - Ensuring STARTUP_POS is imported

    Note: The Configs package is impoted again and again to ensure that integrity is met when importing again and again
    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_API_KEY_Runtime(self):
        try:
            from Configs.config import API_KEY
        except FileNotFoundError:
            raise AssertionError('API_KEY not set in "API_KEY.txt"')

        assert isinstance(API_KEY, str)


    def test_Screen_Resolution(self):
        try:
            from Configs.config import SCREEN_RESOLUTION
        except ImportError:
            raise AssertionError('SCREEN_RESOLUTION Not Found, set in config.py')

        assert isinstance(SCREEN_RESOLUTION, (list, tuple))


    def test_Startup_pos(self):
        try:
            from Configs.config import STARTUP_POS
        except ImportError:
            raise AssertionError('STARTUP_POS Not Found, set in config.py')

        assert isinstance(STARTUP_POS, (list, tuple))


if __name__ == '__main__':
    main()
    # from os import getcwd
    # print(getcwd())
