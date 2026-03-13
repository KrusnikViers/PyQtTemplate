# PyQtTemplate

[![codecov](https://codecov.io/gh/KrusnikViers/PyQtTemplate/graph/badge.svg)](https://codecov.io/gh/KrusnikViers/PyQtTemplate)
[![Maintainability](https://qlty.sh/gh/KrusnikViers/projects/PyQtTemplate/maintainability.svg)](https://qlty.sh/gh/KrusnikViers/projects/PyQtTemplate)

Template for Python projects using Qt as GUI.  
Other files: [License file (MIT)](LICENSE), [Features tracker](FEATURES.md)

## Setting up the project

1. Update `base/info.py` with your project data.
2. Update badge links in README
3. Add `CODECOV_TOKEN` from [codecov.io](https://codecov.io) to Repository Action secrets.
4. Update `.github/workflows/build.yml` if necessary

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

### Versions and release process

Project has three separate hardcoded version numbers. Updating version resets following ones to zero.

1. `PROJECT_COMPATIBILITY_VERSION`  
   Increased when changes make new version incompatible with the previous one in any way.
2. `PROJECT_FEATURE_PACK_VERSION`  
   Increased with significant changes from the user point of view.
3. `PROJECT_RELEASE_VERSION`  
   Increased for every new release as an indicator that any changes were made, to pinpoint exact version of the code.
4. `BUILD_TYPE_INDICATOR`  
   Letter based on type of build and development stage. Defined by the build type rather than in code.

### Development flow versions

1. Dev-only: Repository, code or product should be available only for Developers.  
   Version numbers: `?.?.?d`
2. Stable "Nightly" builds: Builds from `master` with the newest features.  
   Version numbers: `?.?.?n`
3. Stable release: Builds from `release`, best quality-wise.  
   Version numbers: `?.?.?r`

### Branches

* `release`: Stable branch from which releases are generated. Should be updated only from `master`.
* `master`: General development branch. Single-commit features or fixes can be submitted directly.

