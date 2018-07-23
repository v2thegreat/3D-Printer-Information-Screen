# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=c-extension-no-member

from datetime import datetime
from time import time, sleep

# Import Personnel files
from Personnel import Personnel

# Import defaults
from Defaults.defaultFormats import DEFAULT_DATE_FORMAT, DEFAULT_TEXT_FORMAT, DEFAULT_CSV_FORMAT
from Defaults.defaultLabels import *
from Defaults.Misc_Defaults import HIDE_DISPLAY_TIME, STUDENT_ID_INCORRECT_MESSAGE


class BackendStatics(object):
    @staticmethod
    def _setIncorrectLabelToDefault(student_id_label, FLAG, DEFAULT_TEXT):  #Higher Level GUI Function --Dependency: None
        """
        Args:
            studentIDLabel      (:QLabel:   QtWidgets.QLabel): A QLabel object which needs to be reset)
            FLAG                (:bool:     This is the flag that indicates if the given label needs to be reset or not)
            DEFAULT_TEXT        (:str:      This is the default text that needs to be set to the studentIDLabel above)

        It returns False to set the FLAG back to false when it is called
        This is a function to reset the studentIDLabel whenever it sees that the FLAG is set to true.

        This function is usually present in all the functions that in anyway change the functionality
        """
        if FLAG:
            student_id_label.setText(DEFAULT_TEXT)

        return False


    @staticmethod
    def setStudentIDLabelAsErrorLabel(studentIDLabel, INCORRECT_MESSAGE=None):  #Higher Level GUI Function --Dependency: None
        """
        Args:
            studentIDLabel      (:QLabel:   QtWidgets.QLabel): A QLabel object which needs to be have it's text set to INCORRECT_MESSAGE)
            INCORRECT_MESSAGE   (:str:): This is the string has the incorrect message. If no incorrect message is found, the default one is used)


        """
        INCORRECT_MESSAGE = STUDENT_ID_INCORRECT_MESSAGE if INCORRECT_MESSAGE is None else INCORRECT_MESSAGE

        studentIDLabel.setText(INCORRECT_MESSAGE)
        return True


    @staticmethod
    def _isAddDigit(studentIDLabel):    #Higher Level GUI Function --Dependency: BackendStatics._getStdID
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it

        Checks if the length of the student ID is less than 8 characters
        """
        return len(BackendStatics._getStdID(studentIDLabel)) < 8


    @staticmethod
    def _getStdID(studentIDLabel):  #Higher Level GUI Function --Dependency: None
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
        returns the student ID from the student ID label

        Also has an exception for when the label is incorrect
        """
        if len(studentIDLabel.text().split(':')) > 1:
            return studentIDLabel.text().split(':')[1].strip()
        return ""


    @staticmethod
    def _addText(studentIDLabel, btn):  #Higher Level GUI Function  --Dependency: BackendStatics._getAddDigit
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
            btn             (:QPushButton:    QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
        Adds the digit of the button to the end of the student ID label
        """
        studentIDLabel.setText(BackendStatics._getAddDigit(studentIDLabel, btn))


    @staticmethod
    def _getAddDigit(*pram):    #Higher Level GUI Function --Dependency: None
        """
        Args:
            *pram    (:Collection: QtWidgets.QPushButton): List of Buttons
        returns a string joining all the texts from the buttons
        """
        string = ""
        for x in pram:
            string += x.text()
        return string


    @staticmethod
    def _isRemoveDigit(studentIDLabel): #Higher Level GUI Function --Dependency: DEFAULT_TEXT_lbl_St2_StudentIDDisplay
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Checks if the studentIDLabel is the same as the default text for the same label
        """

        return studentIDLabel.text() != DEFAULT_TEXT_lbl_St2_StudentIDDisplay


    @staticmethod
    def _removeDigit(studentIDLabel):   #Higher Level GUI Function --Dependency: BackendStatics.getRemoveDigit
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Sets the studentIDLabel to the one that we get from getRemoveDigit
        """
        studentIDLabel.setText(BackendStatics.getRemoveDigit(studentIDLabel))


    @staticmethod
    def getRemoveDigit(studentIDLabel): #Higher Level GUI Function --Dependency: DEFAULT_TEXT_lbl_St2_StudentIDDisplay
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        turns the studentIDLabel with the last digit removed if it's not the same as the DEFAULT_TEXT_lbl_St2_StudentIDDisplay
        else, it returns the same text without any changes
        """

        return studentIDLabel.text()[:-1] if studentIDLabel.text() != DEFAULT_TEXT_lbl_St2_StudentIDDisplay else studentIDLabel.text()


    @staticmethod
    def saveCancelRecord(studentIDLabel):   #Saving/BackendStatics.Function --Dependency:  BackendStatics._getSavingTextFormat
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to use to save the user's ID or the personnel pin from
        """
        open('Save Cancel Records.txt', 'a').write(BackendStatics._getSavingTextFormat(studentIDLabel))


    @staticmethod
    def isPersonnelPinCorrect(pin): #BackendStatics.Function --Dependency: Personnel.isPinPresent --Possible Change: Inherit Personnel Class
        """
        Args:
            pin     (int/str):    pin that system needs to check against

        function returns Personnel.isPinPresent return value to check if the pin is correct or not

        if a FileNotFoundError is raised, it returns False as well as prints an error message
            In this situation, ensure that there are personnel present
        """
        try:
            return Personnel.isPinPresent(pin)
        except FileNotFoundError:
            print('Personnel File is not present, returning False')
            return False


    @staticmethod
    def sendDialogBack(Dialog): #GUI Function --Dependency: time.sleep  --Possible Change: change from Dialog to self.Dialog
        """
        Args:
            Dialog      (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back until we have to load it back again

        Hides the dialog for HIDE_DISPLAY_TIME, then modifies the dialog to show that it's locked
        """
        Dialog.hide()
        sleep(HIDE_DISPLAY_TIME)
        Dialog.show()


    @staticmethod
    def isCorrectStdID(studentIDLabel): #BackendStatics.Function --Dependency: BackendStatics._getStdID
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        We check if the student ID is exactly 8 digits long or not
            This is done according to the minimum requirements given
        """
        return len(BackendStatics._getStdID(studentIDLabel)) == 8


    @staticmethod
    def saveID(studentIDLabel): #BackendStatics.Function --Dependency: BackendStatics._saveAsCsv, BackendStatics._saveAsText
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Saves as a CVS and a text file
            This is done as a redundancy, and to prevent malicious altering, and to keep a backup
        """
        BackendStatics._saveAsCsv(studentIDLabel)
        BackendStatics._saveAsText(studentIDLabel)


    @staticmethod
    def _saveAsText(studentIDLabel):    #BackendStatics.Function --Dependency: BackendStatics._getSavingTextFormat, savingFormat
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Gets the saving format and then saves it into "Print Records.txt"
        """
        savingFormat = BackendStatics._getSavingTextFormat(studentIDLabel)
        open("Print Records.txt", 'a').write(savingFormat)


    @staticmethod
    def _getSavingTextFormat(studentIDLabel):   #BackendStatics.Function --Dependency: DEFAULT_TEXT_FORMAT, BackendStatics._getStdID, datetime.now().strftime, DEFAULT_DATE_FORMAT, time
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Returns the Student ID with the timestamp of when it was saved
        """
        return DEFAULT_TEXT_FORMAT.format(BackendStatics._getStdID(studentIDLabel),
                                          datetime.now().strftime(DEFAULT_DATE_FORMAT), time())


    @staticmethod
    def _saveAsCsv(studentIDLabel): #BackendStatics.Function --Dependency: BackendStatics._getSavingCSVFormat, savingFormat
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Gets the saving format and then saves it into Print Records.txt
        """
        savingFormat = BackendStatics._getSavingCSVFormat(studentIDLabel)
        open('User Log.csv', 'a').write(savingFormat)


    @staticmethod
    def _getSavingCSVFormat(studentIDLabel):    #BackendStatics.Function --Dependency:DEFAULT_CSV_FORMAT, BackendStatics._getStdID, datetime.now().strftime, DEFAULT_DATE_FORMAT, time
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Returns the Student ID with the timestamp of when it was saved
        """
        return DEFAULT_CSV_FORMAT.format(BackendStatics._getStdID(studentIDLabel),
                                         datetime.now().strftime(DEFAULT_DATE_FORMAT), time())
