# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: diable=c-extension-no-member

import warnings
from PyQt5 import QtCore, QtGui, QtWidgets
from Defaults.Misc_Defaults import nothingFunc

#Importing basefunctions
from BackendStatics import *

#Imoporting defaults
from Defaults.Misc_Defaults import STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE

#Importing GUI
from GUI.PrinterUI import PrinterUI


#NOTE: MOST DOCUMENTATION HAS BEEN TAKEN FROM MY OWN OLDER CODE, AND MAYBE INACCURATE. WHILE I AM DOING MY BEST TO ENSURE THAT IT IS ALL UPTO DATE, THE USER SHOULD STILL BE WEARY. FURTHER, THIS MAY ALSO HAVE BUGS


class Backend(PrinterUI, BackendStatics):

    def __init__(self):
        """
        Args:
            GUI_Controller: QtWidgets.QDialog
                This is the GUI Controller for the Dialog
                It is the object that has direct access to the Dialog and controls all of it's properties

                This means that any changes done to this can affect the UI and can change or control functionality
        """
        self._setGUI()
        self._setFlags()
        self.__setup()


    def _setFlags(self):    #setup
        print('Setting Flags')
        self.INCORRECT_STUDENT_ID_FLAG = False
        self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = False
        print('Flags Set')


    def __setup(self):  #setup
        print('Finished PyQt5 setup')
        print('Finished initializing backend')
        self._settingFunctionality()
        self._displayStage(0)


    def _setBlankScreen(self):  #GUI Function --Dependency: PrinterUI Class
        """
        Function to hide all the widgets, to enable a "blank screen"
            It does so by going into all the stages widgets and running their hide functions
        """
        print('Hid all widgets')
        for widgetLst in self.stages:
            for widget in widgetLst:
                widget.hide()


    def _settingFunctionality(self):    #setup GUI Button Function --Dependency: PrinterUI Class
        """
        Setting functionality
            This means that I'm assigning all the functions that each button and label press needs to call when I click on something
            Note: Stages are indexed, and start at 0, but (as mentioned here) start at 1.
                This applies to functions such as
                    - _displayStage
                    - _GoBack

                These functions work on the indexing rather than the the actual stages

        As a redundancy, I'll set up try catch blocks with all of the functions that're called so that they can be noted in the logs
        """
        print('Setting functionality')

        #Setting Stage 1 functionality
        """
        Stage 1:
            This is the starting screen, and features 'start' button

            Upon clicking the start button, stage 2 is displayed
        """
        self.pb_St1_StartPrint.clicked.connect(lambda: self._displayStage(1))
        self.lbl_St1_DisplayPrinterNumber.mousePressEvent = nothingFunc
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
        self.pb_St2_Num0.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num0))
        self.pb_St2_Num1.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num1))
        self.pb_St2_Num2.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num2))
        self.pb_St2_Num3.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num3))
        self.pb_St2_Num4.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num4))
        self.pb_St2_Num5.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num5))
        self.pb_St2_Num6.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num6))
        self.pb_St2_Num7.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num7))
        self.pb_St2_Num8.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num8))
        self.pb_St2_Num9.clicked.connect(lambda: self.addDigitForSt2(self.lbl_St2_StudentIDDisplay, self.pb_St2_Num9))
        self.pb_St2_BackSpace.clicked.connect(lambda: self.removeDigit(self.lbl_St2_StudentIDDisplay))
        self.pb_St2_Enter.clicked.connect(lambda: self.digitEntered(self.lbl_St2_StudentIDDisplay, self.Dialog))
        self.lbl_St2_StudentIDDisplay.mousePressEvent = nothingFunc
        self.pb_St2_Go_Back.clicked.connect(lambda: self._GoBack(2))
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
        self.pb_St4_CancelPrint.clicked.connect(lambda: self._displayStage(4))
        self.lbl_St4_TimeRemaining.mousePressEvent = nothingFunc
        print('Stage-4 functionality set')

        #Setting Stage 5 functionality
        """
        Stage 5:
            This is the stage where the user/personnel enter's the ID or pin to authorize the prints, and to view who enabled the print to be cancled (This information is recorded)
        """
        self.pb_St5_Num0.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num0))
        self.pb_St5_Num1.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num1))
        self.pb_St5_Num2.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num2))
        self.pb_St5_Num3.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num3))
        self.pb_St5_Num4.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num4))
        self.pb_St5_Num5.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num5))
        self.pb_St5_Num6.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num6))
        self.pb_St5_Num7.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num7))
        self.pb_St5_Num8.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num8))
        self.pb_St5_Num9.clicked.connect(lambda: self.addDigitForSt5(self.lbl_St5_StudentOrPersonnelID, self.pb_St5_Num9))
        self.pb_St5_BackSpace.clicked.connect(lambda: self.removeDigit(self.lbl_St5_StudentOrPersonnelID))
        self.pb_St5_Enter.clicked.connect(lambda: self.digitEnteredForPersonnel(self.lbl_St5_StudentOrPersonnelID, self.Dialog))
        self.lbl_St5_StudentOrPersonnelID.mousePressEvent = nothingFunc
        self.pb_St5_Go_Back.clicked.connect(lambda: self._GoBack(5))
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


    def _displayStage(self, stageNumber):   #GUI Function --Dependency: PrinterUI Class
        """
        Args:
            stageNumber (:int:): Index value used to tell which stage is to be made visible

        Hides all widgets that are on screen
        Loops through each widget in the stage given by self.stages[stageNumber] and makes it visible

        Note: For clarity; self.stages is a 2D array that contains the widgets of all the stages, which are set in order, and can be picked out via their indexes (which is what we do here)
        """
        self._setBlankScreen()
        print('Starting display for stage-{} widgets'.format(stageNumber+1))

        for widget in self.stages[stageNumber]:
            widget.show()

        print('Displaying stage-{} widgets'.format(stageNumber+1))


    def _GoBack(self, currentStage):    #GUI Function --Dependency: PrinterUI Class
        self._displayStage(currentStage-2)

    def addDigitForSt2(self, studentIDLabel, btn):    #GUI Button Function --Dependency: PrinterUI Class, Backend._setIncorrectLabelToDefault, Backend._isAddDigit, Backend._addText
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


    def addDigitForSt5(self, studentIDLabel, btn):
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to add text to it
            btn                 (:QPushButton:    QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
        function to add a digit to the lblStudentIDDisplay
        """
        self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG, DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID)

        if Backend._isAddDigit(studentIDLabel):
            Backend._addText(studentIDLabel, btn)


    def removeDigit(self, studentIDLabel):      #Higher Level GUI Function --Dependency: Backend._setIncorrectLabelToDefault, Backend._isRemoveDigit, Backend._removeDigit
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which needs to remove text

        Checks if we can remove digit from the student ID label, then removes it if possible
        """
        self.INCORRECT_STUDENT_ID_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_ID_FLAG, DEFAULT_TEXT_lbl_St2_StudentIDDisplay)

        if Backend._isRemoveDigit(studentIDLabel):
            Backend._removeDigit(studentIDLabel)


    def digitEntered(self, studentIDLabel, Dialog):     #Too Complex, save for later/leave for backend as too many dependencies
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to get the student ID from
            Dialog              (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back to use the octoprint screen with

        Sets the self.INCORRECT_STUDENT_ID_FLAG to return value of _setIncorrectLabelToDefault (False)


        Checks if the ID is in the correct format
            saves the ID into a text file
            sends the dialog back for some time
        else:
            raises an error
                The error is managed by setting
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


    def digitEnteredForPersonnel(self, studentIDLabel, Dialog):     #Too Complex, save for later/leave for backend as too many dependencies
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to get the student ID or personnel pin from
            Dialog              (:QDialog:    QtWidgets.QDialog): Dialog that we'll send to the back so that we can use the octoprint screen
        """
        print(self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG)
        self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = Backend._setIncorrectLabelToDefault(studentIDLabel,
            self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG, DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID)
        print(self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG)
        if self.isCorrectPersonnelIDorStdID(studentIDLabel):
            Backend.saveCancelRecord(studentIDLabel)
            Backend.sendDialogBack(Dialog)
            studentIDLabel.setText(DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID)
            self._displayStage(0)
            print('Displayed Stage 0')
        else:
            self.INCORRECT_STUDENT_OR_PERSONNEL_FLAG = Backend.setStudentIDLabelAsErrorLabel(
                studentIDLabel, STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE)


    def isSameID(self, studentIDLabel):     #Saving/Backend Function --Dependency:  Backend._getStdID
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need to use to check if the student's ID is the same as the one used to setup the print

        Function to check if the user is the user is the one who set the print
        This is done by checking self.lastIDUsed property, which returns the ID of the last person who used the printers
        """
        return self.lastIDUsed == Backend._getStdID(studentIDLabel)


    def isCorrectPersonnelIDorStdID(self, studentIDLabel):  #Saving/Backend Function --Dependency:  self.isSameID, Backend.isPersonnelPinCorrect, Backend._getStdID
        """
        Args:
            studentIDLabel      (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID or personnel pin that we need to verify the password
        Function to check if the ID or pin given is by the user or not
        """
        return self.isSameID(studentIDLabel) or Backend.isPersonnelPinCorrect(Backend._getStdID(studentIDLabel))


    def noteID(self, studentIDLabel):      #Backend Function    --Dependency:   Backend._getStdID
        """
        Args:
            studentIDLabel    (:QLabel:    QtWidgets.QLabel): A QLabel object which has the student ID that we need

        Function to "note" the last ID used
        The property lastIDUsed is used to verify that the user is the one who set the print
        """
        self.lastIDUsed = Backend._getStdID(studentIDLabel)


def main():
    Backend().show()


if __name__ == '__main__':
    main()
