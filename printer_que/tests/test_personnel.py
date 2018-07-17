# pylint: disable=line-too-long
# pylint: disable=no-self-use
# pylint: disable=protected-access
# pylint: disable=invalid-name

"""
These is the unittests for the Personnel Class

It is designed to ensure safety and reliability from the personnel module
"""

from unittest import TestCase, main
import sys
sys.path.append('../')

from Personnel import Personnel, PERSONNEL_INFO_CSV, PERSONNEL_INFO_TXT
from defaults import *

class test_Personnel(TestCase):
    """
    This is the Unit tests class for the Personnel Class

    These tests run tests for each individual function and static functions in the Personnel Class

    The following functions/concepts are being tested here:
        - _getHash: staticmethod
        - isPinPresent: staticmethod
        - constructor (__init__)
        - different_pin
        - equal_magic_function (__eq__)
        - str_magic_function (__str__)
        - repr_magic_function (__repr__)
        - object_save
        - check_pin
        - add_new_personnel: staticmethod

    """


    def setUp(self):
        """
        Setting up the new classes
        """
        self.personnel1 = Personnel('John Wick', '1300135')        #Yes, it's immature, but growing up is for old people
        self.personnel2 = Personnel('Alan Wolf', '1300134')
        self.PERSONNEL_INFO_TXT = 'Test Personnel Info.txt'

    def tearDown(self):
        """
        Deletes the saved information
        """
        from os import remove
        remove(PERSONNEL_INFO_TXT)
        remove(PERSONNEL_INFO_CSV)


    def test__getHash(self):
        """
        Test to check if _getHash function is working as expected
            Expected :=
                Check if the hash returns something
                Check if the hash does not change with time
                Check if the hash can be repeated with any other pin of eight digits
        """
        assert Personnel._getHash('1300135')
        assert Personnel._getHash('1300135') == Personnel._getHash('1300135')
        assert Personnel._getHash('1300135') != Personnel._getHash('1300134')


    def test_isPinPresent(self):
        """
        Test to check if isPinPresent is working as expected
            Expected :=
                Check if all pins are present in the file
                Check if any pins that are not present are in the file or not
        """
        assert Personnel.isPinPresent('1300135', personnel_list_file=self.PERSONNEL_INFO_TXT)
        assert Personnel.isPinPresent('1300134', personnel_list_file=self.PERSONNEL_INFO_TXT)
        assert not Personnel.isPinPresent('1300133', personnel_list_file=self.PERSONNEL_INFO_TXT)


    def test_constructor(self):
        """
        Test to check if the constructor is working properly
        """

        assert self.personnel1.name == 'John Wick'
        assert self.personnel2.name == 'Alan Wolf'

        assert self.personnel1.pin == Personnel._getHash('1300135')
        assert self.personnel2.pin == Personnel._getHash('1300134')


    def test_different_pin(self):
        """
        Test to check if different pins will be accepted
        """
        assert self.personnel1.pin != self.personnel2.pin


    def test_equal_magic_function(self):
        """
        Test to check if the __eq__ magic function works or not
        """
        assert self.personnel1.__eq__('1300135')
        assert self.personnel2.__eq__('1300134')


    def test_str_magic_function(self):
        """
        Test to check if str magic function is working as expected
        """
        assert self.personnel1.__str__() == '{0}, {1}'.format(self.personnel1.name, self.personnel1.pin)
        assert self.personnel2.__str__() == '{0}, {1}'.format(self.personnel2.name, self.personnel2.pin)



    def test_repr_magic_function(self):
        """
        Test to check if repr magic function is working as expected
        """
        assert self.personnel1.__repr__() == '{0}, {1}'.format(self.personnel1.name, self.personnel1.pin)
        assert self.personnel2.__repr__() == '{0}, {1}'.format(self.personnel2.name, self.personnel2.pin)


    def test_object_save(self):
        """
        Test to check if the save function works properly
        """
        import pickle
        with open(PERSONNEL_INFO_TXT, 'rb') as file_object:
            user = pickle.load(file_object)
            assert user.name == self.personnel1.name
            assert user.pin == self.personnel1.pin


    def test_check_pin(self):
        """
        Test to check if Personnel.isPinPresent works properly
        """
        from random import choice
        input_pin = choice(('1300135', '1300134'))
        assert Personnel.isPinPresent(input_pin)
        assert not Personnel.isPinPresent('1300133')


    def test_add_new_personnel(self):
        """
        Test to check if adding new personnel is working properly
        """

if __name__ == '__main__':
    main()
