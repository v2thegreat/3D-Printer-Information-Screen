"""
These are unit tests for the BackendStatics
"""

from unittest import TestCase, main
from PyQt5 import QtWidgets
from random import choice
import sys
sys.path.append('../')

from BackendStatics import BackendStatics


class test_BackendStatics(TestCase):
    """
    Tests for the BackendStatics Class

    This test is to ensure that all static functions are working as expected

    The following Functions are included:

        - _setIncorrectLabelToDefault
        - setStudentIDLabelAsErrorLabel
        - _isAddDigit
        - _getStdID
        - _addText
        - _getAddDigit
        - _isRemoveDigit
        - _removeDigit
        - getRemoveDigit
        - saveCancelRecord
        - isPersonnelPinCorrect
        - sendDialogBack
        - isCorrectStdID
        - saveID
        - _saveAsText
        - _getSavingTextFormat
        - _saveAsCsv
        - _getSavingCSVFormat
    """

    def setUp(self):
        self.test_Obj = BackendStatics()    #This is a test
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()

    def setUp_Test_Label(self):
        self.test_label = QtWidgets.QLabel(self.Dialog)
        self.test_label_text = 'Test Label'
        self.test_label.setText(self.test_label_text)

    def reset_Label(self, otherLabel = None):
        if otherLabel == None:
            self.test_label.setText(self.test_label_text)

        else:
            self.test_label.setText(otherLabel)

    def tearDown(self):
        pass

    def test_setIncorrectLabelToDefault(self):
        self.setUp_Test_Label()
        DEFAULT_TEXT = "DEFAULT TEXT"
        FLAG_OPTIONS = (choice((True, False)) for x in range(10**4))

        for FLAG in FLAG_OPTIONS:
            result = self.test_Obj._setIncorrectLabelToDefault(self.test_label, FLAG, DEFAULT_TEXT)
            assert False == result
            assert self.test_label.text() == DEFAULT_TEXT if FLAG else 'Test Label'
            self.reset_Label()

    def test_setStudentIDLabelAsErrorLabel(self):
        self.setUp_Test_Label()
        from Defaults.Misc_Defaults import STUDENT_ID_INCORRECT_MESSAGE
        INCORRECT_MESSAGE_options = (choice(('INCORRECT_MESSAGE', None)) for x in range(10**4))

        for INCORRECT_MESSAGE in INCORRECT_MESSAGE_options:
            assert True == self.test_Obj.setStudentIDLabelAsErrorLabel(self.test_label, INCORRECT_MESSAGE)
            assert self.test_label.text() == STUDENT_ID_INCORRECT_MESSAGE if INCORRECT_MESSAGE is None else INCORRECT_MESSAGE
            self.reset_Label()


    def test__getStdID(self):
        pass


if __name__ == '__main__':
    # t = test_BackendStatics()
    # t.setUp()
    # t.test__setIncorrectLabelToDefault()
    main()
