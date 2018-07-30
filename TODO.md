# TODO:

* Finish Adding details for README
* Add Config for screen dimensions (`800 x 480`? or something else?)
* Add "go back" button to stage 5
  * **Fix 1**: Open up in [Qt Designer](https://goo.gl/rfP6e5) and add stage changes
    * **Possible Issues/Additional Issues that may come up**:
      1. Refactor `PyQtUI.py` again ensuring that all the changes mentions are maintained and errors aren't raised when running it
      2. May have to run/write new tests
      3. Will have to add functionality/support in `Backend.py` and/or `BackendStatics.py` packages
      4. Have to ensure that changes are maintained when going back
      5. Ensuring defaults are saved/maintained/still used
  * **Fix 2**: Create a timer indicating that if left alone for long enough, it'll revert back to it's original stages
    * **Possible Issues/Additional Issues that may come up**:
      1. May have to run/write new tests
      2. Will have to add functionality/support in `Backend.py` and/or `BackendStatics.py` packages
  * Fix 2 seems to be the easier solution
* Give more length to all labels, to accommodate for the new font
* make the UI in stage 5 more simple/tell them clearly what's going on
* Add tests for `PrinterUI` to ensure that it sets the stages correctly
* Add custom theme support!
* Write tests for BackendStatics
* Consider breaking BackendStatics into smaller parts
  * Put all higher level GUI Functions into a class for GUI Functions instead?
    * This class would inherit BackendStatics and be present in the GUI package instead
  * Put all the save functions into smaller parts too?
    * this would be better for testing
* Update State Machine.png

<hr>

### Completed

* Force Dialog to be in the center/top left corner
* **Bug report #001** - enter an incorrect student ID - can erase the error message! The other keys give silent errors also
    * **Fix**: Added Additional Checks to make sure that this issue cannot be raised again
      * **Cause**: At the time of creating `_isRemoveDigit`, I assumed that checking if it was equal to `DEFAULT_TEXT_lbl_St2_StudentIDDisplay` would be enough, need to consider it again
