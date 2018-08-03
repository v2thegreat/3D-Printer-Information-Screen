# TODO:

* **Bug Report #002** - Any issue with incorrect personnel pin on stage 5 messes up the message and doesn't change it

  * **Cause**: button action was set to the `addDigit` function for stage 5. This meant that both buttons for stage 2 and stage 5 were calling the same function to handle different functions

  * **Fix**: The fix applied was to create another function: `addDigitForSt5` and rename the original function to `addDigitForSt2`. The difference in the newer function is that it accounts for the changes needed to run it for the different stage

  * **Future Changes**: The functions `addDigitForSt2` and `addDigitForSt5` will be renamed to `addDigit`, with an additional parameter taking an object which tells it the relevant details needed to make it modular and extremely flexible for future use with several hundred pushbuttons

    The necessary additional parameters at this time are:
      * Incorrect flag
      * Default Label Text

    For clarity, these observations can be seen by looking at the two functions (`addDigitForSt2` and `addDigitForSt5`)

    Additional Note: There will have to be some way to modify the flag.
      Flags can be changed in a modular function by adding them to a list and modifying the list values. For more information, [read this](https://stackoverflow.com/questions/22338671/python-functions-to-change-values-in-place)


* Finish Adding details for README

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

* Use smaller font size for all labels, to accommodate for the new font

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

    * **Cause**: At the time of creating `_isRemoveDigit`, I assumed that checking if it was equal to `DEFAULT_TEXT_lbl_St2_StudentIDDisplay` would be enough, need to consider it again

    * **Fix**: Added Additional Checks to make sure that this issue cannot be raised again

* Add Config for screen dimensions (`800 x 480`? or something else?)
