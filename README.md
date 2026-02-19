# PyQtTemplate

[![codecov](https://codecov.io/gh/KrusnikViers/PyQtTemplate/graph/badge.svg)](https://codecov.io/gh/KrusnikViers/PyQtTemplate)

Template for Python projects using Qt as GUI.  
Other files: [License file (MIT)](LICENSE), [Features tracker](FEATURES.md)

## Setting up the project

For badges to work correctly
1. Update badge link in the README
2. Add `CODECOV_TOKEN` from [codecov.io](https://codecov.io) to Repository Action secrets

### Suggested Workflows / Run Configurations
* `Gen UI`
  * Python script `$ProjectFileDir$/build_tools/qt_gen_ui_files.py`
  * Add this step as a pre-requisite for all the next steps
* `Run App`
  * Python script `$ProjectFileDir$/main.py`
* `Run Tests`
  * Unittests in project root directory, pattern `*_test.py`
* `Build Binary`
  * Python Module `PyInstaller`
  * Arguments: `$ProjectFileDir$/build_tools/pyinstaller/binary.spec`

### Adding Qt Designer in PyCharm

Settings ⇒ Tools ⇒ External Tools  
Program: `$ProjectFileDir$\.venv\Lib\site-packages\PySide6\designer.exe`  
Arguments: `$FilePath$`  
Directory: `$ProjectFileDir$`

