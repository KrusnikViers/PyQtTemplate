# PyQtTemplate

Template for Python projects using Qt as GUI. Python compatibility version: 3.11+

Other files: [license file (MIT)](LICENSE), [features tracker](FEATURES.md)

## Setting up the project

* If you are using Qt Designer: add a build step with `build_tools/qt_gen_ui_files.py` script.  
  Make sure it executes during builds as well, to have the latest version of generated files.
* Add test build target for all scripts in the directory, using `*_test.py` target pattern.  
  UI generator should be "Before launch" step for this command.

### Adding Qt Designer in PyCharm

Settings => Tools => External Tools  
Program: `$ProjectFileDir$\venv\Lib\site-packages\PySide6\designer.exe`  
Arguments: `$FilePath$`  
Directory: `$ProjectFileDir$`