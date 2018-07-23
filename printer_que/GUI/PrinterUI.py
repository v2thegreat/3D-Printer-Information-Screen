import sys

try:
    from PyQtUI import UI

except ImportError:
    from GUI.PyQtUI import UI

from PyQt5 import QtCore, QtWidgets


class PrinterUI(UI):
    """Functionality Wrapper for PyQtUI

    This class is to be imported and to be used instead of PyQtUI as it is an extenstion of that class

    This class has automated setups for the PyQt as well as the different stages in the application"""

    def __init__(self):
        """
        Constructor for PrinterUI
        """
        super(PrinterUI, self).__init__()
        self._setGUI()
        self._setStageWidgets()


    def _setGUI(self):
        """
        Function used to run setupUi from the parent class and to simplify Dialog operations
        """
        from PyQt5 import QtWidgets
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(Dialog=self.Dialog)


    def _setStageWidgets(self):
        """
        Function to simplify the different stages widgets
        """
        try:
            self.stage1Widgets = [
                self.pb_St1_StartPrint,
                self.lbl_St1_DisplayPrinterNumber
            ]

            self.stage2Widgets = [
                self.pb_St2_Num0,
                self.pb_St2_Num1,
                self.pb_St2_Num2,
                self.pb_St2_Num3,
                self.pb_St2_Num4,
                self.pb_St2_Num5,
                self.pb_St2_Num6,
                self.pb_St2_Num7,
                self.pb_St2_Num8,
                self.pb_St2_Num9,
                self.pb_St2_BackSpace,
                self.pb_St2_Enter,
                self.lbl_St2_StudentIDDisplay
            ]

            self.stage3Widgets = []

            self.stage4Widgets = [
                self.pb_St4_CancelPrint,
                self.lbl_St4_TimeRemaining
            ]

            self.stage5Widgets = [
                self.pb_St5_Num0,
                self.pb_St5_Num1,
                self.pb_St5_Num2,
                self.pb_St5_Num3,
                self.pb_St5_Num4,
                self.pb_St5_Num5,
                self.pb_St5_Num6,
                self.pb_St5_Num7,
                self.pb_St5_Num8,
                self.pb_St5_Num9,
                self.pb_St5_BackSpace,
                self.pb_St5_Enter,
                self.lbl_St5_StudentOrPersonnelID
            ]

            self.stage6Widgets = []

        except AttributeError:
            self._setGUI()
            self._setStageWidgets()


    @property
    def stages(self):
        """
        Property to return all the stages and their widgets

        If self._setStageWidgets has not been run, it is run before returning the widgets
        """
        try:
            return (self.stage1Widgets, self.stage2Widgets, self.stage3Widgets, self.stage4Widgets, self.stage5Widgets, self.stage6Widgets)

        except AttributeError:
            self._setStageWidgets()
            return self.stages


    def show(self):
        """
        Function to display the main dialog
        """
        try:
            self.Dialog.show()
            sys.exit(self.app.exec_())

        except AttributeError:
            self._setGUI()
            self.show()


if __name__ == '__main__':
    help(PrinterUI)
    PrinterUI().show()
