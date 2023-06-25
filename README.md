# DaVinci Resolve automatic benchmark

__The documentation is not yet completed!__

This script is used to simulate editing in DaVinci Resolve with this short benchmark, which uses the built-in Python macro features of Resolve and also Python libraries like [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) and [PyGetWindow](https://pypi.org/project/PyGetWindow/). It is combination of using macro scripts and also keyboard and mouse programming.

The main script is locate int he `resolve_test.py` file. You can expand and modify the functionality.

## Prerequisities 

1. Install required modules
```sh
pip install pyautogui
pip install pygetwindow
```
2. Enable external macros in Resolve if you have it disabled (_it is usually enabled by default_)
3. Also define all of the PATH variables needed to use Resolve Python macros. It is well described in [here](https://pypi.org/project/PyGetWindow/)
4. Download the test project
5. Import the project into you Resolve, open edit page and make the layout as in the pictures. 

__TBD__: The test project and reference layout are going to be added!

## How to use

Run the script from terminal using 
```sh
python resolve_test.py
```
When you want to stop it, just open the terminal and <kbd>Ctrl</kbd> + <kbd>C</kbd> it.