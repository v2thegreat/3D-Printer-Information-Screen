from PyQt5 import QtCore, QtGui, QtWidgets
from Backend import Backend


class GUI(object):
	def setupUi(self, Dialog):
		"""
		Args: 
			Dialog 			(:QDialog:	QtWidgets.QDialog): Dialog that we need to set up
		"""
		Dialog.setObjectName("Dialog")
		Dialog.resize(800, 400)
		font = QtGui.QFont()
		font.setBold(False)
		font.setWeight(50)
		Dialog.setFont(font)
		Dialog.setWindowOpacity(1.0)
		Dialog.setStyleSheet("background: rgb(255, 255, 255)")

		self.lblStudentIDDisplay = QtWidgets.QLabel(Dialog)
		self.lblStudentIDDisplay.setGeometry(QtCore.QRect(200, 100, 360, 32))

		font = QtGui.QFont()
		font.setFamily("Dubai")
		font.setPointSize(15)

		self.lblStudentIDDisplay.setFont(font)
		self.lblStudentIDDisplay.setAlignment(QtCore.Qt.AlignCenter)
		self.lblStudentIDDisplay.setOpenExternalLinks(False)
		self.lblStudentIDDisplay.setObjectName("lblStudentIDDisplay")

		self.pbNum2 = QtWidgets.QPushButton(Dialog)
		self.pbNum2.setGeometry(QtCore.QRect(360, 150, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum2.setFont(font)
		self.pbNum2.setObjectName("pbNum2")

		self.pbNum1 = QtWidgets.QPushButton(Dialog)
		self.pbNum1.setGeometry(QtCore.QRect(300, 150, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum1.setFont(font)
		self.pbNum1.setStyleSheet("background: rgb(228, 228, 228)")
		self.pbNum1.setObjectName("pbNum1")

		self.pbNum9 = QtWidgets.QPushButton(Dialog)
		self.pbNum9.setGeometry(QtCore.QRect(420, 270, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum9.setFont(font)
		self.pbNum9.setObjectName("pbNum9")

		self.pbNum3 = QtWidgets.QPushButton(Dialog)
		self.pbNum3.setGeometry(QtCore.QRect(420, 150, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum3.setFont(font)
		self.pbNum3.setObjectName("pbNum3")

		self.pbNum6 = QtWidgets.QPushButton(Dialog)
		self.pbNum6.setGeometry(QtCore.QRect(420, 210, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum6.setFont(font)
		self.pbNum6.setObjectName("pbNum6")

		self.pbNum4 = QtWidgets.QPushButton(Dialog)
		self.pbNum4.setGeometry(QtCore.QRect(300, 210, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum4.setFont(font)
		self.pbNum4.setObjectName("pbNum4")

		self.pbNum5 = QtWidgets.QPushButton(Dialog)
		self.pbNum5.setGeometry(QtCore.QRect(360, 210, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum5.setFont(font)
		self.pbNum5.setStyleSheet("background rgb(228, 228, 228)")
		self.pbNum5.setObjectName("pbNum5")

		self.pbNum8 = QtWidgets.QPushButton(Dialog)

		self.pbNum8.setGeometry(QtCore.QRect(360, 270, 40, 40))
		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum8.setFont(font)
		self.pbNum8.setObjectName("pbNum8")

		self.pbNum7 = QtWidgets.QPushButton(Dialog)
		self.pbNum7.setGeometry(QtCore.QRect(300, 270, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum7.setFont(font)
		self.pbNum7.setObjectName("pbNum7")

		self.pbNum0 = QtWidgets.QPushButton(Dialog)
		self.pbNum0.setGeometry(QtCore.QRect(360, 330, 40, 40))

		font = QtGui.QFont()
		font.setPointSize(12)

		self.pbNum0.setFont(font)
		self.pbNum0.setObjectName("pbNum0")

		self.lblTimeRemaining = QtWidgets.QLabel(Dialog)
		self.lblTimeRemaining.setGeometry(QtCore.QRect(200, 60, 360, 32))

		font = QtGui.QFont()
		font.setFamily("Dubai")
		font.setPointSize(15)

		self.lblTimeRemaining.setFont(font)
		self.lblTimeRemaining.setLineWidth(1)
		self.lblTimeRemaining.setAlignment(QtCore.Qt.AlignCenter)
		self.lblTimeRemaining.setOpenExternalLinks(False)
		self.lblTimeRemaining.setObjectName("lblTimeRemaining")

		self.lblDisplayPrinterNumber = QtWidgets.QLabel(Dialog)
		self.lblDisplayPrinterNumber.setGeometry(QtCore.QRect(200, 25, 360, 32))

		font = QtGui.QFont()
		font.setFamily("Dubai")
		font.setPointSize(15)

		self.lblDisplayPrinterNumber.setFont(font)
		self.lblDisplayPrinterNumber.setAlignment(QtCore.Qt.AlignCenter)
		self.lblDisplayPrinterNumber.setOpenExternalLinks(False)
		self.lblDisplayPrinterNumber.setObjectName("lblDisplayPrinterNumber")

		self.pbBackSpaceDigit = QtWidgets.QPushButton(Dialog)
		self.pbBackSpaceDigit.setGeometry(QtCore.QRect(560, 95, 40, 40))
		self.pbBackSpaceDigit.setFont(font)
		self.pbBackSpaceDigit.setObjectName("pbBackSpaceDigit")

		self.pbEnterBtn = QtWidgets.QPushButton(Dialog)
		self.pbEnterBtn.setGeometry(QtCore.QRect(500, 330, 100, 40))
		self.pbEnterBtn.setFont(font)
		self.pbEnterBtn.setObjectName("pbEnterBtn")


		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

		self.DigitButtonLstSetup()
		self.Backend = Backend(self.DigitButtons)
		self.buttonCheck(Dialog)

	def buttonCheck(self, Dialog):
		"""
		Checks if any of the buttons have been pressed and what to do when they are
		"""
		self.pbNum0.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum0))
		self.pbNum1.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum1))
		self.pbNum2.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum2))
		self.pbNum3.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum3))
		self.pbNum4.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum4))
		self.pbNum5.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum5))
		self.pbNum6.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum6))
		self.pbNum7.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum7))
		self.pbNum8.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum8))
		self.pbNum9.clicked.connect(lambda: self.Backend.addDigit(self.lblStudentIDDisplay, self.pbNum9))
		
		self.pbBackSpaceDigit.clicked.connect(lambda: self.Backend.removeDigit(self.lblStudentIDDisplay))
		self.pbEnterBtn.clicked.connect(lambda: self.Backend.digitEntered(self.pbEnterBtn, self.lblStudentIDDisplay, Dialog))

	def DigitButtonLstSetup(self):
		"""
		Creates a list for the pushbutton digits
		"""
		self.DigitButtons = [
						self.pbNum0,
						self.pbNum1,
						self.pbNum2,
						self.pbNum3,
						self.pbNum4,
						self.pbNum5,
						self.pbNum6,
						self.pbNum7,
						self.pbNum8,
						self.pbNum9
						]

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Main"))
		self.lblStudentIDDisplay.setText(_translate("Dialog", "STUDENT ID: "))
		self.pbNum2.setText(_translate("Dialog", "2"))
		self.pbNum1.setText(_translate("Dialog", "1"))
		self.pbNum9.setText(_translate("Dialog", "9"))
		self.pbNum3.setText(_translate("Dialog", "3"))
		self.pbNum6.setText(_translate("Dialog", "6"))
		self.pbNum4.setText(_translate("Dialog", "4"))
		self.pbNum5.setText(_translate("Dialog", "5"))
		self.pbNum8.setText(_translate("Dialog", "8"))
		self.pbNum7.setText(_translate("Dialog", "7"))
		self.pbNum0.setText(_translate("Dialog", "0"))
		self.lblTimeRemaining.setText("")																#_translate("Dialog", "Time Remaining"))
		self.lblDisplayPrinterNumber.setText(_translate("Dialog", "Printer Number"))
		self.pbBackSpaceDigit.setText(_translate("Dialog", "<-"))
		self.pbEnterBtn.setText(_translate("Dialog", "Enter"))

def run():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	ui = GUI()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	run()
