# PyQtTemplate

Template for Python projects using Qt as GUI. Python compatibility version: 3.11+

Other files: [license file (MIT)](LICENSE), [features tracker](FEATURES.md)

## Setting up the project

* If you are using Qt Designer: add a build step with `build_tools/qt_gen_ui_files.py` script.  
  Make sure it executes during builds as well, to have the latest version of generated files.
* Add a Python build target for `main.py` in the project root directory.
  UI generator should be a dependency for this step.
* Add a Unittests build target for all scripts in the directory, using `*_test.py` target pattern.  
  UI generator should be a dependency for this step.

### Adding Qt Designer in PyCharm

Settings => Tools => External Tools  
Program: `$ProjectFileDir$\venv\Lib\site-packages\PySide6\designer.exe`  
Arguments: `$FilePath$`  
Directory: `$ProjectFileDir$`

### Suggested Workflows for PyCharm
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
