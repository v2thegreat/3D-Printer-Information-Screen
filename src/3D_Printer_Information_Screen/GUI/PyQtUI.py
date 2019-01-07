# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Queing System -- Updated.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


"""
This is the output from the PyUIC script that converts the .ui file to Python Code

This code is imported in the PrinterUI module where the stages are sorted
"""
import sys
sys.path.append('..')
from Defaults.defaultStyleSheets import *
from Defaults.defaultLabels import *
from Defaults.defaultFonts import *
from Defaults.defaultSizePolicies import *
from Configs.config import SCREEN_RESOLUTION, STARTUP_POS
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QLabel, QPushButton


# TODO: Add more options to the "Cancel" Print screen, such as a mode to just make changes without canceling the print

class UI(object):

	lbl_St1_DisplayPrinterNumber: QLabel
	pb_St1_StartPrint: QPushButton

	lbl_St2_StudentIDDisplay: QLabel
	pb_St2_BackSpace: QPushButton
	pb_St2_Enter: QPushButton
	pb_St2_Go_Back: QPushButton
	pb_St2_Num0: QPushButton
	pb_St2_Num1: QPushButton
	pb_St2_Num2: QPushButton
	pb_St2_Num3: QPushButton
	pb_St2_Num4: QPushButton
	pb_St2_Num5: QPushButton
	pb_St2_Num6: QPushButton
	pb_St2_Num7: QPushButton
	pb_St2_Num8: QPushButton
	pb_St2_Num9: QPushButton

	lbl_St4_TimeRemaining: QLabel
	pb_St4_CancelPrint: QPushButton
	pb_St4_MakeChanges: QPushButton

	lbl_St5_StudentOrPersonnelID: QLabel
	pb_St5_BackSpace: QPushButton
	pb_St5_Enter: QPushButton
	pb_St5_Go_Back: QPushButton
	pb_St5_Num0: QPushButton
	pb_St5_Num1: QPushButton
	pb_St5_Num2: QPushButton
	pb_St5_Num3: QPushButton
	pb_St5_Num4: QPushButton
	pb_St5_Num5: QPushButton
	pb_St5_Num6: QPushButton
	pb_St5_Num7: QPushButton
	pb_St5_Num8: QPushButton
	pb_St5_Num9: QPushButton

	def setupUi(self, Dialog):
		Dialog.setObjectName(DEFAULT_DIALOG_OBJECT_NAME)

		Dialog.resize(SCREEN_RESOLUTION[0], SCREEN_RESOLUTION[1])
		Dialog.setFont(DEFAULT_DIALOG_FONT)
		Dialog.setWindowOpacity(1.0)
		Dialog.setStyleSheet(DEFAULT_DIALOG_STYLESHEET)
		Dialog.setGeometry(STARTUP_POS[0], STARTUP_POS[1], SCREEN_RESOLUTION[0], SCREEN_RESOLUTION[1])

		# GUI initializations for stage 1
		self.lbl_St1_DisplayPrinterNumber = QtWidgets.QLabel(Dialog)
		self.lbl_St1_DisplayPrinterNumber.setEnabled(True)
		self.lbl_St1_DisplayPrinterNumber.setGeometry(QtCore.QRect(0, 25, 800, 32))
		self.lbl_St1_DisplayPrinterNumber.setFont(DEFAULT_LABEL_FONT)
		self.lbl_St1_DisplayPrinterNumber.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber)
		self.lbl_St1_DisplayPrinterNumber.setAlignment(QtCore.Qt.AlignCenter)
		self.lbl_St1_DisplayPrinterNumber.setOpenExternalLinks(False)
		self.lbl_St1_DisplayPrinterNumber.setObjectName("lbl_St1_DisplayPrinterNumber")

		self.pb_St1_StartPrint = QtWidgets.QPushButton(Dialog)
		self.pb_St1_StartPrint.setEnabled(True)
		self.pb_St1_StartPrint.setGeometry(QtCore.QRect(200, 130, 360, 220))
		DEFAULT_SIZE_POLICY.setHeightForWidth(self.pb_St1_StartPrint.sizePolicy().hasHeightForWidth())
		self.pb_St1_StartPrint.setSizePolicy(DEFAULT_SIZE_POLICY)
		self.pb_St1_StartPrint.setFont(DEFAULT_PUSHBUTTON_FONT_EMPHASIS)
		self.pb_St1_StartPrint.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St1_StartPrint)
		self.pb_St1_StartPrint.setAutoFillBackground(False)
		self.pb_St1_StartPrint.setObjectName("pb_St1_StartPrint")

		# GUI initializations for stage 2
		self.lbl_St2_StudentIDDisplay = QtWidgets.QLabel(Dialog)
		self.lbl_St2_StudentIDDisplay.setEnabled(True)
		self.lbl_St2_StudentIDDisplay.setGeometry(QtCore.QRect(0, 100, 800, 32))
		self.lbl_St2_StudentIDDisplay.setFont(DEFAULT_LABEL_FONT)
		self.lbl_St2_StudentIDDisplay.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay)
		self.lbl_St2_StudentIDDisplay.setAlignment(QtCore.Qt.AlignCenter)
		self.lbl_St2_StudentIDDisplay.setOpenExternalLinks(False)
		self.lbl_St2_StudentIDDisplay.setObjectName("lbl_St2_StudentIDDisplay")

		self.pb_St2_Num1 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num1.setEnabled(True)
		self.pb_St2_Num1.setGeometry(QtCore.QRect(300, 150, 40, 40))
		self.pb_St2_Num1.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num1.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num1)
		self.pb_St2_Num1.setObjectName("pb_St2_Num1")

		self.pb_St2_Num2 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num2.setEnabled(True)
		self.pb_St2_Num2.setGeometry(QtCore.QRect(360, 150, 40, 40))
		self.pb_St2_Num2.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num2.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num0)
		self.pb_St2_Num2.setObjectName("pb_St2_Num2")

		self.pb_St2_Num3 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num3.setEnabled(True)
		self.pb_St2_Num3.setGeometry(QtCore.QRect(420, 150, 40, 40))
		self.pb_St2_Num3.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num3.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num3)
		self.pb_St2_Num3.setObjectName("pb_St2_Num3")

		self.pb_St2_Num4 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num4.setEnabled(True)
		self.pb_St2_Num4.setGeometry(QtCore.QRect(300, 210, 40, 40))
		self.pb_St2_Num4.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num4.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num5)
		self.pb_St2_Num4.setObjectName("pb_St2_Num4")

		self.pb_St2_Num5 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num5.setEnabled(True)
		self.pb_St2_Num5.setGeometry(QtCore.QRect(360, 210, 40, 40))
		self.pb_St2_Num5.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num5.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num6)
		self.pb_St2_Num5.setObjectName("pb_St2_Num5")

		self.pb_St2_Num6 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num6.setEnabled(True)
		self.pb_St2_Num6.setGeometry(QtCore.QRect(420, 210, 40, 40))
		self.pb_St2_Num6.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num6.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num4)
		self.pb_St2_Num6.setObjectName("pb_St2_Num6")

		self.pb_St2_Num7 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num7.setEnabled(True)
		self.pb_St2_Num7.setGeometry(QtCore.QRect(300, 270, 40, 40))
		self.pb_St2_Num7.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num7.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num8)
		self.pb_St2_Num7.setObjectName("pb_St2_Num7")

		self.pb_St2_Num8 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num8.setEnabled(True)
		self.pb_St2_Num8.setGeometry(QtCore.QRect(360, 270, 40, 40))
		self.pb_St2_Num8.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num8.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num7)
		self.pb_St2_Num8.setObjectName("pb_St2_Num8")

		self.pb_St2_Num9 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num9.setEnabled(True)
		self.pb_St2_Num9.setGeometry(QtCore.QRect(420, 270, 40, 40))
		self.pb_St2_Num9.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num9.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num2)
		self.pb_St2_Num9.setObjectName("pb_St2_Num9")

		self.pb_St2_Num0 = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Num0.setEnabled(True)
		self.pb_St2_Num0.setGeometry(QtCore.QRect(360, 330, 40, 40))
		self.pb_St2_Num0.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Num0.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num9)
		self.pb_St2_Num0.setObjectName("pb_St2_Num0")

		self.pb_St2_BackSpace = QtWidgets.QPushButton(Dialog)
		self.pb_St2_BackSpace.setEnabled(True)
		self.pb_St2_BackSpace.setGeometry(QtCore.QRect(620, 150, 71, 40))
		self.pb_St2_BackSpace.setFont(DEFAULT_PUSHBUTTON_STRONG_FONT)
		self.pb_St2_BackSpace.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_BackSpace)
		self.pb_St2_BackSpace.setObjectName("pb_St2_BackSpace")

		self.pb_St2_Enter = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Enter.setEnabled(True)
		self.pb_St2_Enter.setGeometry(QtCore.QRect(480, 330, 111, 40))
		self.pb_St2_Enter.setFont(DEFAULT_PUSHBUTTON_STRONG_EMPHASIS_FONT)
		self.pb_St2_Enter.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Enter)
		self.pb_St2_Enter.setObjectName("pb_St2_Enter")

		# 'Go Back' button for stage 2 is defined here
		# User Defined
		self.pb_St2_Go_Back = QtWidgets.QPushButton(Dialog)
		self.pb_St2_Go_Back.setEnabled(True)
		self.pb_St2_Go_Back.setGeometry(QtCore.QRect(0, 410, 240, 40))
		self.pb_St2_Go_Back.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St2_Go_Back.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num9)
		self.pb_St2_Go_Back.setObjectName("pb_St2_Go_Back")

		# GUI initializations for stage 4
		self.lbl_St4_TimeRemaining = QtWidgets.QLabel(Dialog)
		self.lbl_St4_TimeRemaining.setEnabled(True)
		self.lbl_St4_TimeRemaining.setGeometry(QtCore.QRect(0, 60, 800, 32))
		self.lbl_St4_TimeRemaining.setFont(DEFAULT_LABEL_FONT)
		self.lbl_St4_TimeRemaining.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining)
		self.lbl_St4_TimeRemaining.setLineWidth(1)
		self.lbl_St4_TimeRemaining.setAlignment(QtCore.Qt.AlignCenter)
		self.lbl_St4_TimeRemaining.setOpenExternalLinks(False)
		self.lbl_St4_TimeRemaining.setObjectName("lbl_St4_TimeRemaining")

		self.pb_St4_CancelPrint = QtWidgets.QPushButton(Dialog)
		self.pb_St4_CancelPrint.setEnabled(True)
		self.pb_St4_CancelPrint.setGeometry(QtCore.QRect(200, 130, 360, 100))
		DEFAULT_SIZE_POLICY.setHeightForWidth(self.pb_St4_CancelPrint.sizePolicy().hasHeightForWidth())
		self.pb_St4_CancelPrint.setSizePolicy(DEFAULT_SIZE_POLICY)
		self.pb_St4_CancelPrint.setFont(DEFAULT_PUSHBUTTON_FONT_EMPHASIS)
		self.pb_St4_CancelPrint.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St4_CancelPrint)
		self.pb_St4_CancelPrint.setAutoFillBackground(False)
		self.pb_St4_CancelPrint.setObjectName("pb_St4_CancelPrint")

		# 'Make Changes' button for stage 4
		# User Defined
		self.pb_St4_MakeChanges = QtWidgets.QPushButton(Dialog)
		self.pb_St4_MakeChanges.setEnabled(True)
		self.pb_St4_MakeChanges.setGeometry(QtCore.QRect(200, 240, 360, 100))
		self.pb_St4_MakeChanges.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St4_MakeChanges.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St4_MakeChanges)
		self.pb_St4_MakeChanges.setObjectName("pb_St4_MakeChanges")

		# GUI initializations for stage 5
		self.lbl_St5_StudentOrPersonnelID = QtWidgets.QLabel(Dialog)
		self.lbl_St5_StudentOrPersonnelID.setEnabled(True)
		self.lbl_St5_StudentOrPersonnelID.setGeometry(QtCore.QRect(0, 100, 800, 32))
		self.lbl_St5_StudentOrPersonnelID.setFont(DEFAULT_LABEL_FONT)
		self.lbl_St5_StudentOrPersonnelID.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID)
		self.lbl_St5_StudentOrPersonnelID.setAlignment(QtCore.Qt.AlignCenter)
		self.lbl_St5_StudentOrPersonnelID.setOpenExternalLinks(False)
		self.lbl_St5_StudentOrPersonnelID.setObjectName("lbl_St5_StudentOrPersonnelID")

		self.pb_St5_Enter = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Enter.setEnabled(True)
		self.pb_St5_Enter.setGeometry(QtCore.QRect(480, 330, 111, 40))
		self.pb_St5_Enter.setFont(DEFAULT_PUSHBUTTON_STRONG_EMPHASIS_FONT)
		self.pb_St5_Enter.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Enter)
		self.pb_St5_Enter.setObjectName("pb_St5_Enter")

		self.pb_St5_BackSpace = QtWidgets.QPushButton(Dialog)
		self.pb_St5_BackSpace.setEnabled(True)
		self.pb_St5_BackSpace.setGeometry(QtCore.QRect(520, 150, 71, 40))
		self.pb_St5_BackSpace.setFont(DEFAULT_PUSHBUTTON_STRONG_FONT)
		self.pb_St5_BackSpace.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_BackSpace)
		self.pb_St5_BackSpace.setObjectName("pb_St5_BackSpace")

		self.pb_St5_Num1 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num1.setEnabled(True)
		self.pb_St5_Num1.setGeometry(QtCore.QRect(300, 150, 40, 40))
		self.pb_St5_Num1.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num1.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num7)
		self.pb_St5_Num1.setObjectName("pb_St5_Num1")

		self.pb_St5_Num2 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num2.setEnabled(True)
		self.pb_St5_Num2.setGeometry(QtCore.QRect(360, 150, 40, 40))
		self.pb_St5_Num2.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num2.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num5)
		self.pb_St5_Num2.setObjectName("pb_St5_Num2")

		self.pb_St5_Num3 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num3.setEnabled(True)
		self.pb_St5_Num3.setGeometry(QtCore.QRect(420, 150, 40, 40))
		self.pb_St5_Num3.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num3.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num2)
		self.pb_St5_Num3.setObjectName("pb_St5_Num3")

		self.pb_St5_Num4 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num4.setEnabled(True)
		self.pb_St5_Num4.setGeometry(QtCore.QRect(300, 210, 40, 40))
		self.pb_St5_Num4.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num4.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num9)
		self.pb_St5_Num4.setObjectName("pb_St5_Num4")

		self.pb_St5_Num5 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num5.setEnabled(True)
		self.pb_St5_Num5.setGeometry(QtCore.QRect(360, 210, 40, 40))
		self.pb_St5_Num5.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num5.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num8)
		self.pb_St5_Num5.setObjectName("pb_St5_Num5")

		self.pb_St5_Num6 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num6.setEnabled(True)
		self.pb_St5_Num6.setGeometry(QtCore.QRect(420, 210, 40, 40))
		self.pb_St5_Num6.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num6.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num1)
		self.pb_St5_Num6.setObjectName("pb_St5_Num6")

		self.pb_St5_Num7 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num7.setEnabled(True)
		self.pb_St5_Num7.setGeometry(QtCore.QRect(300, 270, 40, 40))
		self.pb_St5_Num7.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num7.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num3)
		self.pb_St5_Num7.setObjectName("pb_St5_Num7")

		self.pb_St5_Num8 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num8.setEnabled(True)
		self.pb_St5_Num8.setGeometry(QtCore.QRect(360, 270, 40, 40))
		self.pb_St5_Num8.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num8.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num0)
		self.pb_St5_Num8.setObjectName("pb_St5_Num8")

		self.pb_St5_Num9 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num9.setEnabled(True)
		self.pb_St5_Num9.setGeometry(QtCore.QRect(420, 270, 40, 40))
		self.pb_St5_Num9.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num9.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num6)
		self.pb_St5_Num9.setObjectName("pb_St5_Num9")

		self.pb_St5_Num0 = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Num0.setEnabled(True)
		self.pb_St5_Num0.setGeometry(QtCore.QRect(360, 330, 40, 40))
		self.pb_St5_Num0.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Num0.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num4)
		self.pb_St5_Num0.setObjectName("pb_St5_Num0")

		# 'Go Back' button for stage 5 is defined here
		# User Defined
		self.pb_St5_Go_Back = QtWidgets.QPushButton(Dialog)
		self.pb_St5_Go_Back.setEnabled(True)
		self.pb_St5_Go_Back.setGeometry(QtCore.QRect(0, 410, 240, 40))
		self.pb_St5_Go_Back.setFont(DEFAULT_PUSHBUTTON_FONT)
		self.pb_St5_Go_Back.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num9)
		self.pb_St5_Go_Back.setObjectName("pb_St2_Go_Back")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate(DEFAULT_DIALOG_OBJECT_NAME, "Main"))

		self.lbl_St1_DisplayPrinterNumber.setText(
			_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber))
		self.pb_St1_StartPrint.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St1_StartPrint))

		self.lbl_St2_StudentIDDisplay.setText(
			_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St2_StudentIDDisplay))
		self.pb_St2_Num2.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num2))
		self.pb_St2_Num1.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num1))
		self.pb_St2_Num9.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num9))
		self.pb_St2_Num3.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num3))
		self.pb_St2_Num6.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num6))
		self.pb_St2_Num4.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num4))
		self.pb_St2_Num5.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num5))
		self.pb_St2_Num8.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num8))
		self.pb_St2_Num7.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num7))
		self.pb_St2_Num0.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num0))
		self.pb_St2_BackSpace.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_BackSpace))
		self.pb_St2_Enter.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Enter))
		self.pb_St2_Go_Back.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Go_Back))

		self.lbl_St4_TimeRemaining.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St4_TimeRemaining))
		self.pb_St4_CancelPrint.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St4_CancelPrint))
		self.pb_St4_MakeChanges.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St4_MakeChanges))

		self.lbl_St5_StudentOrPersonnelID.setText(
			_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID))
		self.pb_St5_Enter.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Enter))
		self.pb_St5_Num8.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num8))
		self.pb_St5_BackSpace.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_BackSpace))
		self.pb_St5_Num6.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num6))
		self.pb_St5_Num3.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num3))
		self.pb_St5_Num7.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num7))
		self.pb_St5_Num0.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num0))
		self.pb_St5_Num2.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num2))
		self.pb_St5_Num9.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num9))
		self.pb_St5_Num1.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num1))
		self.pb_St5_Num5.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num5))
		self.pb_St5_Num4.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num4))
		self.pb_St5_Go_Back.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Go_Back))


def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
	dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	ui = UI()
	ui.setupUi(dialog)
	dialog.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
