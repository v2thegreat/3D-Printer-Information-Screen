#Possibly Depreciated

# from .QueingSystem import GUI

# class StudentIDLabel(GUI):
#     """docstring for StudentIDLabel"""
#     def __init__(self):
#         super(StudentIDLabel, self).__init__()

#     def _removeDigitLblStudentID(self):
#         if self.__isOKRemoveDigit():
#             return self.lblStudentIDDisplay.text()[:-1]

#         else:
#             return self.lblStudentIDDisplay.text()

#     def __isOKRemoveDigit(self):
#         return self.lblStudentIDDisplay.text() != "STUDENT ID: "

#     def _addDigitToStudentID(self, digit):
#         if self.__isOKAddDigit():
#             self.setStdntLblText(self.getStudentIDText() + digit)

#     def _getDigit(self, val):
#         if self.__isOKAddDigit():
#             print(val)
#             return self.lblStudentIDDisplay.text() + val.text()

#         else:
#             return self.lblStudentIDDisplay.text()

#     def __isOKAddDigit(self):
#         print("Ran")
#         if self.getLenStdntID() < 8:
#             return True
#         else:
#             return False

#     def setStdntLblText(self, val):
#         self.lblStudentIDDisplay.setText(val)

#     def getStudentIDText(self):
#         return self.lblStudentIDDisplay.text()

#     def getID(self):
#         text = self.getStudentIDText()
#         return text.split(':')[1].strip()

#     def getLenStdntID(self):
#         return len(self.getID())
