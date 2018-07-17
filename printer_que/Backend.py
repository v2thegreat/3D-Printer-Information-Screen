# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: diable=c-extension-no-member

import warnings
from datetime import datetime
from time import time, sleep
from PyQt5 import QtCore, QtGui, QtWidgets

#Importing default values
from Personnel import *
from Defaults.defaultLabels import *
from Defaults.Misc_Defaults import nothingFunc

#NOTE: MOST DOCUMENTATION HAS BEEN TAKEN FROM MY OWN OLDER CODE, AND MAYBE INACCURATE. WHILE I AM DOING MY BEST TO ENSURE THAT IT IS ALL UPTO DATE, THE USER SHOULD STILL BE WEARY. FURTHER, THIS MAY ALSO HAVE BUGS


class Backend:
    def __init__(self, GUI_Controller, Dialog):
        """
        Args:
            GUI_Controller: QtWidgets.QDialog
                This is the GUI Controller for the Dialog
                It is the object that has direct access to the Dialog and controls all of it's properties

                This means that any changes done to this can affect the UI and can change or control functionality
        """
        print('Finished PyQt5 setup')
        self.INCORRECT_STUDENT_ID_FLAG = False
        self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = False
        self.GUI_Controller = GUI_Controller
        self.GUI_Dialog = Dialog
        print('Finished initializing backend')
        self._settingFunctionality()
        self._displayStage(0)

    def _setBlankScreen(self):
        """
        Function to hide all the widgets, to enable a "blank screen"
            It does so by going into all the stages widgets and running their hide functions
        """
        print('Hid all widgets')
        for widgetLst in self.GUI_Controller.stages:
            for widget in widgetLst:
                widget.hide()

    def _settingFunctionality(self):
        """
        Setting functionality
            This means that I'm assigning all the functions that each button and label press needs to call when I click on something

        As a redundancy, I'll set up try catch blocks with all of the functions that're called so that they can be noted in the logs
        """
        print('Setting functionality')

        #Setting Stage 1 functionality
        """
        Stage 1:
            This is the starting screen, and features 'start' button

            Upon clicking the start button, stage 2 is displayed
        """
        self.GUI_Controller.pb_St1_StartPrint.clicked.connect(lambda: self._displayStage(1))
        self.GUI_Controller.lbl_St1_DisplayPrinterNumber.mousePressEvent = nothingFunc
        print('Stage-1 functionality set')

        #Setting Stage 2 functionality
        """
        Stage 2:
            This is the screen where the user enter's his student or personnel ID.
            This means that user's will have to enter an ID to start using these printers

            They then will press the enter button to continue, or press backspace to delete a character in the ID

            Usage of this would be better at explaining than this would

            Note: Each user's ID is saved into the machine for logs and keeping track of which programs tend to use it more
        """
        self.GUI_Controller.pb_St2_Num0.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num0))
        self.GUI_Controller.pb_St2_Num1.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num1))
        self.GUI_Controller.pb_St2_Num2.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num2))
        self.GUI_Controller.pb_St2_Num3.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num3))
        self.GUI_Controller.pb_St2_Num4.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num4))
        self.GUI_Controller.pb_St2_Num5.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num5))
        self.GUI_Controller.pb_St2_Num6.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num6))
        self.GUI_Controller.pb_St2_Num7.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num7))
        self.GUI_Controller.pb_St2_Num8.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num8))
        self.GUI_Controller.pb_St2_Num9.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Controller.pb_St2_Num9))
        self.GUI_Controller.pb_St2_BackSpace.clicked.connect(lambda: self.removeDigit(self.GUI_Controller.lbl_St2_StudentIDDisplay))
        self.GUI_Controller.pb_St2_Enter.clicked.connect(lambda: self.digitEntered(self.GUI_Controller.lbl_St2_StudentIDDisplay, self.GUI_Dialog))
        self.GUI_Controller.lbl_St2_StudentIDDisplay.mousePressEvent = nothingFunc
        print('Stage-2 functionality set')

        #Setting Stage 3 functionality
        """
        Stage 3:
            This is the stage where the user uses the octoprint workstation to upload and start their prints. While the time is for 5 mins, this time can be changed easily by changing the HIDE_DISPLAY_TIME parameter, and even be switched to running the next stage by checking the display screen instead and using it when the screen goes blank
        """
        #No functions defined, so leaving it empty for later
        print('Stage-3 functionality set')

        #Setting Stage 4 functionality
        """
        Stage 4:
            This is the stage where the original user or any personnel can choose to cancel the print
            This information is again logged as to who canceled the print
        """
        self.GUI_Controller.pb_St4_CancelPrint.clicked.connect(lambda: self._displayStage(4))
        self.GUI_Controller.lbl_St4_TimeRemaining.mousePressEvent = nothingFunc
        print('Stage-4 functionality set')

        #Setting Stage 5 functionality
        """
        Stage 5:
            This is the stage where the user/personnel enter's the ID or pin to authorize the prints, and to view who enabled the print to be cancled (This information is recorded)
        """
        self.GUI_Controller.pb_St5_Num0.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num0))
        self.GUI_Controller.pb_St5_Num1.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num1))
        self.GUI_Controller.pb_St5_Num2.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num2))
        self.GUI_Controller.pb_St5_Num3.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num3))
        self.GUI_Controller.pb_St5_Num4.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num4))
        self.GUI_Controller.pb_St5_Num5.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num5))
        self.GUI_Controller.pb_St5_Num6.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num6))
        self.GUI_Controller.pb_St5_Num7.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num7))
        self.GUI_Controller.pb_St5_Num8.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num8))
        self.GUI_Controller.pb_St5_Num9.clicked.connect(lambda: self.addDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Controller.pb_St5_Num9))
        self.GUI_Controller.pb_St5_BackSpace.clicked.connect(lambda: self.removeDigit(self.GUI_Controller.lbl_St5_StudentOrPersonnelID))
        self.GUI_Controller.pb_St5_Enter.clicked.connect(lambda: self.digitEnteredForPersonnel(self.GUI_Controller.lbl_St5_StudentOrPersonnelID, self.GUI_Dialog))
        self.GUI_Controller.lbl_St5_StudentOrPersonnelID.mousePressEvent = nothingFunc
        print('Stage-5 functionality set')

        #Setting Stage 6 functionality
        """
        Stage 6:

            This stage is also empty, and is the stage when the print is over and can be started again
            Even the functions include the
        """
        #No functions defined, so leaving it empty for later
        print('Stage-6 functionality set')
        print('Functionality of all widgets set')

    def _displayStage(self, stageNumber):
        """
        Args:
            stageNumber (:int:): Index value used to tell which stage is to be made visible

        Hides all widgets that are on screen
        Loops through each widget in the stage given by self.GUI_Controller.stages[stageNumber] and makes it visible

        Note: For clarity; self.GUI_Controller.stages is a 2D array that contains the widgets of all the stages, which are set in order, and can be picked out via their indexes (which is what we do here)
        """
        self._setBlankScreen()
        print('Starting display for stage-{} widgets'.format(stageNumber+1))

        for widget in self.GUI_Controller.stages[stageNumber]:
            widget.show()

        print('Displaying stage-{} widgets'.format(stageNumber+1))

    @staticmethod
    def _setIncorrectLabelToDefault(studentIDLabel, FLAG, DEFAULT_TEXT):
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
            studentIDLabel.setText(DEFAULT_TEXT)
        return False

    @staticmethod
    def setStudentIDLabelAsErrorLabel(studentIDLabel, INCORRECT_MESSAGE = None):
        """
        Args:
            studentIDLabel      (:QLabel:   QtWidgets.QLabel): A QLabel object which needs to be have it's text set to INCORRECT_MESSAGE)
            INCORRECT_MESSAGE   (:str:      This is the string has the incorrect message. If no incorrect message is found, the default one is used)
        """
        INCORRECT_MESSAGE = STUDENT_ID_INCORRECT_MESSAGE if INCORRECT_MESSAGE == None else INCORRECT_MESSAGE

        studentIDLabel.setText(INCORRECT_MESSAGE)
        return True

    def addDigit(self, studentIDLabel, btn):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
            btn                 (:QPushButton:    QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
        function to add a digit to the lblStudentIDDisplay
        """
        self.INCORRECT_STUDENT_ID_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_ID_FLAG, DEFAULT_TEXT_lbl_St2_StudentIDDisplay)

        if Backend._isAddDigit(studentIDLabel):
            Backend._addText(studentIDLabel, btn)

    @staticmethod
    def _isAddDigit(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
        Checks if the length of the student ID is less than 8 characters
        """
        return len(Backend._getStdID(studentIDLabel)) < 8

    @staticmethod
    def _getStdID(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
        returns the student ID from the student ID

        Also has an exception for when the label is incorrect
        """
        return studentIDLabel.text().split(':')[1].strip()

    @staticmethod
    def _addText(studentIDLabel, btn):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
            btn             (:QPushButton:    QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
        Adds the digit of the button to the end of the student ID label
        """
        studentIDLabel.setText(Backend._getAddDigit(studentIDLabel, btn))

    @staticmethod
    def _getAddDigit(*pram):
        """
        Args:
            *pram    (:Collection: QtWidgets.QPushButton): List of Buttons
        returns a string joining all the texts from the buttons
        """
        string = ""
        for x in pram:
            string += x.text()
        return string

    def removeDigit(self, studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Checks if we can remove digit from the student ID label, then removes it if possible
        """
        self.INCORRECT_STUDENT_ID_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_ID_FLAG, DEFAULT_TEXT_lbl_St2_StudentIDDisplay)

        if Backend._isRemoveDigit(studentIDLabel):
            Backend._removeDigit(studentIDLabel)

    @staticmethod
    def _isRemoveDigit(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Checks if the studentIDLabel is the same as the default text for the same label
        """

        return studentIDLabel.text() != DEFAULT_TEXT_lbl_St2_StudentIDDisplay

    @staticmethod
    def _removeDigit(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Sets the studentIDLabel to the one that we get from getRemoveDigit
        """
        studentIDLabel.setText(Backend.getRemoveDigit(studentIDLabel))

    @staticmethod
    def getRemoveDigit(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        turns the studentIDLabel with the last digit removed if it's not the same as the DEFAULT_TEXT_lbl_St2_StudentIDDisplay
        else, it returns the same text without any changes
        """

        return studentIDLabel.text()[:-1] if studentIDLabel.text() != DEFAULT_TEXT_lbl_St2_StudentIDDisplay else studentIDLabel.text()

    def digitEntered(self, studentIDLabel, Dialog):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to get the student ID from
            Dialog              (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back to use the octoprint screen with

        Checks if the ID is in the correct format
            saves the ID into a text file
            sends the dialog back for some time
        else:
            raises an error
        """
        self.INCORRECT_STUDENT_ID_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_ID_FLAG, DEFAULT_TEXT_lbl_St2_StudentIDDisplay)

        if Backend.isCorrectStdID(studentIDLabel):
            Backend.saveID(studentIDLabel)
            self.noteID(studentIDLabel)
            Backend.sendDialogBack(Dialog)
            studentIDLabel.setText(DEFAULT_TEXT_lbl_St2_StudentIDDisplay)
            self._displayStage(3)
            print('Displayed Stage 3')
        else:
            self.INCORRECT_STUDENT_ID_FLAG = Backend.setStudentIDLabelAsErrorLabel(studentIDLabel)

    def digitEnteredForPersonnel(self, studentIDLabel, Dialog):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to get the student ID or personnel pin from
            Dialog              (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back so that we can use the octoprint screen
        """
        self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG, DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID)

        if self.isCorrectPersonnelIDorStdID(studentIDLabel):
            Backend.saveCancelRecord(studentIDLabel)
            Backend.sendDialogBack(Dialog)
            studentIDLabel.setText(DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID)
            self._displayStage(0)
            print('Displayed Stage 0')
        else:
            self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = Backend.setStudentIDLabelAsErrorLabel(
                studentIDLabel, STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE)

    @staticmethod
    def saveCancelRecord(studentIDLabel):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to use to save the user's ID or the personnel pin from
        """
        open('Save Cancel Records.txt', 'a').write(Backend._getSavingTextFormat(studentIDLabel))

    def isSameID(self, studentIDLabel):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to use to check if the student's ID is the same as the one used to setup the print

        Function to check if the user is the user is the one who set the print
        This is done by checking self.lastIDUsed property, which returns the ID of the last person who used the printers
        """
        return self.lastIDUsed == Backend._getStdID(studentIDLabel)

    def isCorrectPersonnelIDorStdID(self, studentIDLabel):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID or personnel pin that we need to verify the password
        Function to check if the ID or pin given is by the user or not
        """
        return self.isSameID(studentIDLabel) or Backend.isPersonnelPinCorrect(Backend._getStdID(studentIDLabel))

    @staticmethod
    def isPersonnelPinCorrect(pin):
        try:
            return Personnel.isPinPresent(pin)
        except FileNotFoundError:
            return False

    def noteID(self, studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Function to "note" the last ID used
        The property lastIDUsed is used to verify that the user is the one who set the print
        """
        self.lastIDUsed = Backend._getStdID(studentIDLabel)

    @staticmethod
    def sendDialogBack(Dialog):
        """
        Args:
            Dialog      (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back until we have to load it back again

        Hides the dialog for HIDE_DISPLAY_TIME, then modifies the dialog to show that it's locked
        """
        Dialog.hide()
        sleep(HIDE_DISPLAY_TIME)
        Dialog.show()

    @staticmethod
    def isCorrectStdID(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        We check if the student ID is exactly 8 digits long or not
            This is done according to the minimum requirements given
        """
        return len(Backend._getStdID(studentIDLabel)) == 8

    @staticmethod
    def saveID(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Saves as a CVS and a text file
            This is done as a redundancy, and to prevent malicious altering, and to keep a backup
        """
        Backend._saveAsCsv(studentIDLabel)
        Backend._saveAsText(studentIDLabel)

    @staticmethod
    def _saveAsText(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Gets the saving format and then saves it into "Print Records.txt"
        """
        savingFormat = Backend._getSavingTextFormat(studentIDLabel)
        open("Print Records.txt", 'a').write(savingFormat)

    @staticmethod
    def _getSavingTextFormat(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Returns the Student ID with the timestamp of when it was saved
        """
        return DEFAULT_TEXT_FORMAT.format(Backend._getStdID(studentIDLabel),
                            datetime.now().strftime(DEFAULT_DATE_FORMAL), time())

    @staticmethod
    def _saveAsCsv(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Gets the saving format and then saves it into Print Records.txt
        """
        savingFormat = Backend._getSavingCSVFormat(studentIDLabel)
        open('User Log.csv', 'a').write(savingFormat)

    @staticmethod
    def _getSavingCSVFormat(studentIDLabel):
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Returns the Student ID with the timestamp of when it was saved
        """
        return DEFAULT_CSV_FORMAT.format(Backend._getStdID(studentIDLabel),
                            datetime.now().strftime(DEFAULT_DATE_FORMAL), time())

def main():
    from UI import PrinterUI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = PrinterUI()
    ui.setupUi(Dialog)
    backend_obj = Backend(ui, Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
