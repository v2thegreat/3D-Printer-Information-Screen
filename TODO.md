TODO:

* Force Dialog to be in the center/top left corner
* Add "go back" button to stage 5
* Give more height to all labels, to accommodate for the new font
* make the UI in stage 5 more simple/tell them clearly what's going on
* Add tests for `PrinterUI` to ensure that it sets the stages correctly
* Add custom theme support!
* Bug report - enter an incorrect student ID - can erase the error message! The other keys give silent errors also
    * Nvm, found it, will take precautions to prevent it

* Write tests for BackendStatics
* Consider breaking BackendStatics into smaller parts
  * Put all higher level GUI Functions into a class for GUI Functions instead?
    * This class would inherit BackendStatics and be present in the GUI package instead
  * Put all the save functions into smaller parts too?
    * this would be better for testing
