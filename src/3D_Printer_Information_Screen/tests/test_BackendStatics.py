"""
These are unit tests for the BackendStatics
"""

from unittest import TestCase, main
from PyQt5 import QtWidgets
from random import choice
from itertools import product
from os import listdir, remove
import sys
sys.path.append('../')

from BackendStatics import BackendStatics


class test_BackendStatics(TestCase):
    """
    Tests for the BackendStatics Class

    This test is to ensure that all static functions are working as expected
    To save time, when testing functions that call other (smaller) functions,
    the other functions need not have specific tests unless absolutely nessesary

    These functions are marked with 'subtest'along with their parent functions

    The following functions are included:

    - _setIncorrectLabelToDefault       (done)
    - setStudentIDLabelAsErrorLabel     (done)
    - _isAddDigit                       (done)
    - _addText                          (done)
    - _isRemoveDigit                    (done)
    - _removeDigit                      (done)
    - saveCancelRecord                  (done)
    - isCorrectStdID                    (done)
    - saveID                            (done)
    - _getStdID                         (subtest, _isAddDigit+)
    - _getAddDigit                      (subtest, _addText)
    - getRemoveDigit                    (subtest, _removeDigit)
    - _saveAsText                       (subtest, saveID)
    - _getSavingTextFormat              (subtest, saveCancelRecord+)
    - _saveAsCsv                        (subtest, saveID)
    - _getSavingCSVFormat               (subtest, _saveAsCsv)
    - sendDialogBack                    (skipping, visually checkable)
    - isPersonnelPinCorrect             (skipped, wrapper for Personnel.isPinPresent(pin))
    """

    def setUp(self):
        self.test_Obj = BackendStatics()    #This is a test
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()


    def setUpTestlabel(self):
        self.testLabel = QtWidgets.QLabel(self.Dialog)
        self.testLabel_text = 'Test Label'
        self.testLabel.setText(self.testLabel_text)


    def resetTestLabel(self, otherLabel = None):
        if otherLabel == None:
            self.testLabel.setText(self.testLabel_text)

        else:
            self.testLabel.setText(otherLabel)


    def tearDown(self):
        if 'Save Cancel Records.txt' in listdir():
            remove('Save Cancel Records.txt')

        if "Print Records.txt" in listdir():
            remove("Print Records.txt")

        if 'User Log.csv' in listdir():
            remove('User Log.csv')

        "Print Records.txt"
        'User Log.csv'


    def test_setIncorrectLabelToDefault(self):
        self.setUpTestlabel()
        DEFAULT_TEXT = "DEFAULT TEXT"
        FLAG_OPTIONS = (choice((True, False)) for x in range(10**4))

        for FLAG in FLAG_OPTIONS:
            result = self.test_Obj._setIncorrectLabelToDefault(self.testLabel, FLAG, DEFAULT_TEXT)
            assert False == result
            assert self.testLabel.text() == DEFAULT_TEXT if FLAG else 'Test Label'
            self.resetTestLabel()


    def test_setStudentIDLabelAsErrorLabel(self):
        self.setUpTestlabel()
        from Defaults.Misc_Defaults import STUDENT_ID_INCORRECT_MESSAGE
        INCORRECT_MESSAGE_options = (choice(('INCORRECT_MESSAGE', None)) for x in range(10**4))

        for INCORRECT_MESSAGE in INCORRECT_MESSAGE_options:
            assert True == self.test_Obj.setStudentIDLabelAsErrorLabel(self.testLabel, INCORRECT_MESSAGE)
            assert self.testLabel.text() == STUDENT_ID_INCORRECT_MESSAGE if INCORRECT_MESSAGE is None else INCORRECT_MESSAGE
            self.resetTestLabel()


    def test__isAddDigit(self):
          from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
          self.setUpTestlabel()
          for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
              self.resetTestLabel(newLabel)
              assert BackendStatics._isAddDigit(self.testLabel) == (len(stdID) < 8)


    def test__addText(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, genNumPushButtons
        self.setUpTestlabel()
        for newLabel, testBtn in product(possibleStudentIDLabels, genNumPushButtons(self.Dialog)):
            self.resetTestLabel(newLabel)
            BackendStatics._addText(self.testLabel, testBtn)
            assert self.testLabel.text() == newLabel + testBtn.text()


    def test__isRemoveDigit(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
        self.setUpTestlabel()
        for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
            self.resetTestLabel(newLabel)
            assert BackendStatics._isRemoveDigit(self.testLabel) == (len(stdID) != 0)


    def test__removeDigit(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
        self.setUpTestlabel()
        for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
            self.resetTestLabel(newLabel)
            if BackendStatics._isRemoveDigit(self.testLabel):
                BackendStatics._removeDigit(self.testLabel)
                assert self.testLabel.text() == newLabel[:-1]


    def test_saveCancelRecord(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
        self.setUpTestlabel()
        for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
            if len(stdID) != 0:
                self.resetTestLabel(newLabel)
                BackendStatics.saveCancelRecord(self.testLabel)

                with open('Save Cancel Records.txt') as fileObject:
                    lastRecord = fileObject.readlines()[-1]

                assert stdID in lastRecord


    def test_isCorrectStdID(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
        self.setUpTestlabel()
        for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
            self.resetTestLabel(newLabel)
            assert BackendStatics.isCorrectStdID(self.testLabel) == (len(stdID) == 8)


    def test_saveID(self):
        from test_BackendStatics_TestingPrams.genLabels import possibleStudentIDLabels, possibleStudentID
        self.setUpTestlabel()
        for newLabel, stdID in zip(possibleStudentIDLabels, possibleStudentID):
            if len(stdID) != 0:
                self.resetTestLabel(newLabel)
                BackendStatics.saveID(self.testLabel)

                with open("Print Records.txt") as fileObjectTxt:
                    lastTextRecord = fileObjectTxt.readlines()[-1]

                with open('User Log.csv') as fileObjectCsv:
                    lastCsvRecord = fileObjectCsv.readlines()[-1]

                assert stdID in lastTextRecord
                assert stdID in lastCsvRecord



if __name__ == '__main__':
    # t = test_BackendStatics()
    # t.setUp()
    # t.test__setIncorrectLabelToDefault()
    main()
