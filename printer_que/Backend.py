from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from time import time, sleep
import warnings
HIDEDISPLAYTIME = 5

class Backend:
	__DEFAULT_STUDENT_ID_TEXT__ = "STUDENT ID: "
	__STUDENT_ID_INCORRECT_MESSAGE__ = "INCORRECT ID"
	__INCORRECT_STUDENT_ID_FLAG__ = False

	def __init__(self, digitButtons):
		"""
		Class to run backend applications for the Queing System Class
		Args:
			digitButtons	(:Collection: QtWidgets.QPushButton): A list of all the pushbuttons in the QueingSystemClass
		"""
		super(Backend, self).__init__()
		self.digitButtons = digitButtons
		#self._setPandasInstalled()

	def _setPandasInstalled(self):
		"""
		NOTE: THIS FUNCTION IS DEPRECIATED

		Checks if pandas is installed
		Sets the flag to True if so
		Throws a warning and sets the flag to false
		"""
		try:
			from pandas import DataFrame
			self.isPandasInstalled=True
		except ImportError:
			self.isPandasInstalled=False
			warnings.ImportWarning("Pandas not installed")

	def __buttonPressSetup(self, studentIDLabel):
		if Backend.__INCORRECT_STUDENT_ID_FLAG__:
			studentIDLabel.setText(Backend.__DEFAULT_STUDENT_ID_TEXT__)
			Backend.__INCORRECT_STUDENT_ID_FLAG__ = False

	def setStudentIDasErrorID(self, studentIDLabel):
		studentIDLabel.setText(Backend.__STUDENT_ID_INCORRECT_MESSAGE__)
		Backend.__INCORRECT_STUDENT_ID_FLAG__ = True

	def addDigit(self, studentIDLabel, btn):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to add text to it
			btn 			(:QPushButton:	QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
		function to add a digit to the lblStudentIDDisplay
		"""
		self.__buttonPressSetup(studentIDLabel)

		if self._isAddDigit(studentIDLabel):
			self._addText(studentIDLabel, btn)

	def _isAddDigit(self, studentIDLabel) -> bool:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to add text to it
		Checks if the length of the student ID is less than 8
		"""
		return len(self._getStdID(studentIDLabel)) < 8

	def _getStdID(self, studentIDLabel):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to add text to it
		returns the student ID from the student ID
		"""
		return studentIDLabel.text().split(':')[1].strip()

	def _addText(self, studentIDLabel, btn):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to add text to it
			btn 			(:QPushButton:	QtWidgets.QPushButton): A btn who's digits are supposed to be added to the QLabel
		Adds the digit of the button to the end of the student ID label
		"""
		studentIDLabel.setText(self._getAddDigit(studentIDLabel, btn))

	def _getAddDigit(self, *pram) -> str:
		"""
		Args:
			*pram	(:Collection: QtWidgets.QPushButton): List of Buttons
		returns a string joining all the texts from the buttons
		"""
		string = ""
		for x in pram:
			string += x.text()
		return string

	def removeDigit(self, studentIDLabel) -> None:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to remove text

		Checks if we can remove digit from the student ID label, then removes it if possible
		"""
		self.__buttonPressSetup(studentIDLabel)

		if self._isRemoveDigit(studentIDLabel):
			self._removeDigit(studentIDLabel)

	def _isRemoveDigit(self, studentIDLabel):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to remove text

		Checks if the studentIDLabel is the same as the default text for the same label
		"""
		return studentIDLabel.text() != Backend.__DEFAULT_STUDENT_ID_TEXT__

	def _removeDigit(self, studentIDLabel):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to remove text

		Sets the studentIDLabel to the one that we get from getRemoveDigit
		"""
		studentIDLabel.setText(self.getRemoveDigit(studentIDLabel))

	def getRemoveDigit(self, studentIDLabel):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which needs to remove text

		returns the studentIDLabel with the last digit removed if it's not the same as the Backend.__DEFAULT_STUDENT_ID_TEXT__
		else, it returns the same text without any changes
		"""
		return studentIDLabel.text()[:-1] if studentIDLabel.text() != Backend.__DEFAULT_STUDENT_ID_TEXT__ else studentIDLabel.text()

	def digitEntered(self, EnterButton, studentIDLabel, Dialog):
		"""
		Args:
			EnterButton		(:QPushButton: QtWidgets.QPushButton): ##No clue
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need
			Dialog 			(:QDialog:	QtWidgets.QDialog): Dialog that we'll send to the back until we have to load it back again

		Checks if the ID is in the correct format
			saves the ID into a text file
			sends the dialog back for some time
		else:
			raises an error
		"""
		self.__buttonPressSetup(studentIDLabel)

		if self.isCorrectID(studentIDLabel):
			self.saveID(studentIDLabel)
			self.sendDialogBack(Dialog)
			studentIDLabel.setText(Backend.__DEFAULT_STUDENT_ID_TEXT__)
		else:
			self.setStudentIDasErrorID(studentIDLabel)

	def sendDialogBack(self, Dialog):
		"""
		Args:
			Dialog 			(:QDialog:	QtWidgets.QDialog): Dialog that we'll send to the back until we have to load it back again

		Hides the dialog for HIDEDISPLAYTIME, then modifies the dialog to show that it's locked
		"""
		Dialog.hide()
		sleep(HIDEDISPLAYTIME)
		#TurnDialogLockModeOn(Dialog)
		Dialog.show()

	def isCorrectID(self, studentIDLabel) -> bool:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need

		We check if the student ID is exactly 8 digits long or not
		"""
		return len(self._getStdID(studentIDLabel)) == 8

	def saveID(self, studentIDLabel):
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need

		check if pandas is installed by the isPandasInstalled label
			tries to save as Csv
			if it fails, then it saves as a text file
		else:
			saves as a text file
		"""
		if self.isPandasInstalled:
			try:
				self._saveAsCsv(studentIDLabel)

			except pd.errors.EmptyDataError:
				self._saveAsText(studentIDLabel)
		else:
			self._saveAsText(studentIDLabel)

	def _saveAsText(self, studentIDLabel) -> None:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need

		Gets the saving format and then saves it into Print Records.txt
		"""
		savingFormat = self._getSavingTextFormat(studentIDLabel)
		open("Print Records.txt", 'a').write(savingFormat)

	def _getSavingTextFormat(self, studentIDLabel) -> str:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need
		Returns the Student ID with the timestamp of when it was saved
		"""
		return '{0}\t{1}\t{2}\n'.format(self._getStdID(studentIDLabel), datetime.now().strftime('%dth %B, %Y'), time())

	def _saveAsCsv(self, studentIDLabel):
		savingFormat = self._getSavingCSVFormat(studentIDLabel)
		open('User Log.csv', 'a').write(savingFormat)

	def _getSavingCSVFormat(self, studentIDLabel) -> str:
		"""
		Args:
			studentIDLabel	(:QLabel:	QtWidgets.QLabel): A QLabel object which has the student ID that we need
		Returns the Student ID with the timestamp of when it was saved
		"""
		return '{0},{1},{2}\n'.format(self._getStdID(studentIDLabel), datetime.now().strftime('%dth %B, %Y'), time())

if __name__ == '__main__':
	pass