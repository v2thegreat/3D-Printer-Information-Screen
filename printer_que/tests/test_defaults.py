"""

These are the unit tests for the defaults, to ensure that they exist and that they can be imported

"""

from unittest import TestCase, main
import sys
sys.path.append('../')

from Defaults.defaultLabels import *
from Defaults.defaultFonts import *
from Defaults.defaultFormats import *
from Defaults.defaults import *
from Defaults.defaultStyleSheets import *
from Defaults.Misc_Defaults import *

class test_Defaults(TestCase):
    """
    Test for the defaults module which has all the defaults

    This test is to ensure that all the defaults exist when imported
    and that they're present in the global scope

    The following defaults are included:

        - nothingFunc
        - DEFAULT_DIALOG_OBJECT_NAME
        - DEFAULT_DIALOG_STYLESHEET
        - DEFAULT_LABEL_COMMON_FONT_FAMILY
        - DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY
        - DEFAULT_STYLE_SHEET_pb_St2_Num0
        - DEFAULT_STYLE_SHEET_pb_St2_Num1
        - DEFAULT_STYLE_SHEET_pb_St2_Num2
        - DEFAULT_STYLE_SHEET_pb_St2_Num3
        - DEFAULT_STYLE_SHEET_pb_St2_Num4
        - DEFAULT_STYLE_SHEET_pb_St2_Num5
        - DEFAULT_STYLE_SHEET_pb_St2_Num6
        - DEFAULT_STYLE_SHEET_pb_St2_Num7
        - DEFAULT_STYLE_SHEET_pb_St2_Num8
        - DEFAULT_STYLE_SHEET_pb_St2_Num9
        - DEFAULT_STYLE_SHEET_pb_St5_Num0
        - DEFAULT_STYLE_SHEET_pb_St5_Num1
        - DEFAULT_STYLE_SHEET_pb_St5_Num2
        - DEFAULT_STYLE_SHEET_pb_St5_Num3
        - DEFAULT_STYLE_SHEET_pb_St5_Num4
        - DEFAULT_STYLE_SHEET_pb_St5_Num5
        - DEFAULT_STYLE_SHEET_pb_St5_Num6
        - DEFAULT_STYLE_SHEET_pb_St5_Num7
        - DEFAULT_STYLE_SHEET_pb_St5_Num8
        - DEFAULT_STYLE_SHEET_pb_St5_Num9
        - DEFAULT_STYLE_SHEET_pb_St1_StartPrint
        - DEFAULT_STYLE_SHEET_pb_St4_CancelPrint
        - DEFAULT_STYLE_SHEET_pb_St2_BackSpace
        - DEFAULT_STYLE_SHEET_pb_St2_Enter
        - DEFAULT_STYLE_SHEET_pb_St_
        - DEFAULT_STYLE_SHEET_pb_St5_BackSpace
        - DEFAULT_STYLE_SHEET_pb_St5_Enter
        - DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay
        - DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining
        - DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber
        - DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID
        - DEFAULT_TEXT_lbl_St2_StudentIDDisplay
        - DEFAULT_TEXT_pb_St2_Num2
        - DEFAULT_TEXT_pb_St2_Num1
        - DEFAULT_TEXT_pb_St2_Num9
        - DEFAULT_TEXT_pb_St2_Num3
        - DEFAULT_TEXT_pb_St2_Num6
        - DEFAULT_TEXT_pb_St2_Num4
        - DEFAULT_TEXT_pb_St2_Num5
        - DEFAULT_TEXT_pb_St2_Num8
        - DEFAULT_TEXT_pb_St2_Num7
        - DEFAULT_TEXT_pb_St2_Num0
        - DEFAULT_TEXT_lbl_St4_TimeRemaining
        - DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber
        - DEFAULT_TEXT_pb_St1_StartPrint
        - DEFAULT_TEXT_pb_St4_CancelPrint
        - DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID
        - DEFAULT_TEXT_pb_St2_BackSpace
        - DEFAULT_TEXT_pb_St2_Enter
        - DEFAULT_TEXT_pb_St5_Enter
        - DEFAULT_TEXT_pb_St5_Num8
        - DEFAULT_TEXT_pb_St5_BackSpace
        - DEFAULT_TEXT_pb_St5_Num6
        - DEFAULT_TEXT_pb_St5_Num3
        - DEFAULT_TEXT_pb_St5_Num7
        - DEFAULT_TEXT_pb_St5_Num0
        - DEFAULT_TEXT_pb_St5_Num2
        - DEFAULT_TEXT_pb_St5_Num9
        - DEFAULT_TEXT_pb_St5_Num1
        - DEFAULT_TEXT_pb_St5_Num5
        - DEFAULT_TEXT_pb_St5_Num4
        - HIDE_DISPLAY_TIME
        - STUDENT_ID_INCORRECT_MESSAGE
        - STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE
        - DEFAULT_DATE_FORMAT
        - DEFAULT_TEXT_FORMAT
        - DEFAULT_CSV_FORMAT
    """

    def setUp(self):
    	pass

    def tearDown(self):
        pass

    def test_nothingFunc (self):
        """
        Test to see if nothingFunc  exists after being imported
        """

        self.assertTrue("nothingFunc" in globals().keys())

    def test_DEFAULT_DIALOG_OBJECT_NAME (self):
        """
        Test to see if DEFAULT_DIALOG_OBJECT_NAME  exists after being imported
        """

        self.assertTrue("DEFAULT_DIALOG_OBJECT_NAME" in globals().keys())

    def test_DEFAULT_DIALOG_STYLESHEET (self):
        """
        Test to see if DEFAULT_DIALOG_STYLESHEET  exists after being imported
        """

        self.assertTrue("DEFAULT_DIALOG_STYLESHEET" in globals().keys())

    def test_DEFAULT_LABEL_COMMON_FONT_FAMILY (self):
        """
        Test to see if DEFAULT_LABEL_COMMON_FONT_FAMILY  exists after being imported
        """

        self.assertTrue("DEFAULT_LABEL_COMMON_FONT_FAMILY" in globals().keys())

    def test_DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY (self):
        """
        Test to see if DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY  exists after being imported
        """

        self.assertTrue("DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num0 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num0  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num0" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num1 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num1  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num1" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num2 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num2  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num2" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num3 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num3  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num3" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num4 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num4  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num4" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num5 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num5  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num5" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num6 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num6  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num6" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num7 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num7  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num7" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num8 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num8  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num8" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Num9 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Num9  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Num9" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num0 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num0  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num0" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num1 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num1  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num1" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num2 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num2  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num2" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num3 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num3  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num3" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num4 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num4  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num4" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num5 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num5  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num5" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num6 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num6  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num6" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num7 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num7  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num7" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num8 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num8  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num8" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Num9 (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Num9  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Num9" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St1_StartPrint (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St1_StartPrint  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St1_StartPrint" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St4_CancelPrint (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St4_CancelPrint  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St4_CancelPrint" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_BackSpace (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_BackSpace  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_BackSpace" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St2_Enter (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St2_Enter  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St2_Enter" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St_ (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St_  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St_" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_BackSpace (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_BackSpace  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_BackSpace" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_pb_St5_Enter (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_pb_St5_Enter  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_pb_St5_Enter" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber" in globals().keys())

    def test_DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID (self):
        """
        Test to see if DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID  exists after being imported
        """

        self.assertTrue("DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID" in globals().keys())

    def test_DEFAULT_TEXT_lbl_St2_StudentIDDisplay (self):
        """
        Test to see if DEFAULT_TEXT_lbl_St2_StudentIDDisplay  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_lbl_St2_StudentIDDisplay" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num2 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num2  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num2" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num1 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num1  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num1" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num9 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num9  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num9" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num3 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num3  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num3" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num6 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num6  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num6" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num4 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num4  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num4" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num5 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num5  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num5" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num8 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num8  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num8" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num7 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num7  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num7" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Num0 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Num0  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Num0" in globals().keys())

    def test_DEFAULT_TEXT_lbl_St4_TimeRemaining (self):
        """
        Test to see if DEFAULT_TEXT_lbl_St4_TimeRemaining  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_lbl_St4_TimeRemaining" in globals().keys())

    def test_DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber (self):
        """
        Test to see if DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber" in globals().keys())

    def test_DEFAULT_TEXT_pb_St1_StartPrint (self):
        """
        Test to see if DEFAULT_TEXT_pb_St1_StartPrint  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St1_StartPrint" in globals().keys())

    def test_DEFAULT_TEXT_pb_St4_CancelPrint (self):
        """
        Test to see if DEFAULT_TEXT_pb_St4_CancelPrint  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St4_CancelPrint" in globals().keys())

    def test_DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID (self):
        """
        Test to see if DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_BackSpace (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_BackSpace  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_BackSpace" in globals().keys())

    def test_DEFAULT_TEXT_pb_St2_Enter (self):
        """
        Test to see if DEFAULT_TEXT_pb_St2_Enter  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St2_Enter" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Enter (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Enter  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Enter" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num8 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num8  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num8" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_BackSpace (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_BackSpace  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_BackSpace" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num6 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num6  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num6" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num3 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num3  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num3" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num7 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num7  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num7" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num0 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num0  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num0" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num2 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num2  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num2" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num9 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num9  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num9" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num1 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num1  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num1" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num5 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num5  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num5" in globals().keys())

    def test_DEFAULT_TEXT_pb_St5_Num4 (self):
        """
        Test to see if DEFAULT_TEXT_pb_St5_Num4  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_pb_St5_Num4" in globals().keys())

    def test_HIDE_DISPLAY_TIME (self):
        """
        Test to see if HIDE_DISPLAY_TIME  exists after being imported
        """

        self.assertTrue("HIDE_DISPLAY_TIME" in globals().keys())

    def test_STUDENT_ID_INCORRECT_MESSAGE (self):
        """
        Test to see if STUDENT_ID_INCORRECT_MESSAGE  exists after being imported
        """

        self.assertTrue("STUDENT_ID_INCORRECT_MESSAGE" in globals().keys())

    def test_STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE (self):
        """
        Test to see if STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE  exists after being imported
        """

        self.assertTrue("STUDENT_ID_OR_PERSONNEL_ID_INCORRECT_MESSAGE" in globals().keys())

    def test_DEFAULT_DATE_FORMAL (self):
        """
        Test to see if DEFAULT_DATE_FORMAL  exists after being imported
        """

        self.assertTrue("DEFAULT_DATE_FORMAT" in globals().keys())

    def test_DEFAULT_TEXT_FORMAT (self):
        """
        Test to see if DEFAULT_TEXT_FORMAT  exists after being imported
        """

        self.assertTrue("DEFAULT_TEXT_FORMAT" in globals().keys())

    def test_DEFAULT_CSV_FORMAT (self):
        """
        Test to see if DEFAULT_CSV_FORMAT  exists after being imported
        """

        self.assertTrue("DEFAULT_CSV_FORMAT" in globals().keys())

if __name__ == '__main__':
    main()
