# General project name and version constants. Refer to these constants whenever possible.
# These values can be used for defining compatibility or storing project-related data, and should not be changed
# without a good reason.
PUBLISHER_NAME = "KrusnikViers"
PROJECT_NAME = "PyQtTemplate"
PROJECT_URL = "https://github.com/KrusnikViers/PyQtTemplate"

PROJECT_COMPATIBILITY_VERSION = 0
PROJECT_FEATURE_PACK_VERSION = 0
PROJECT_RELEASE_VERSION = 0
BUILD_TYPE_INDICATOR = 'd'

PROJECT_FULL_VERSION = 'v{}.{}.{}{}'.format(
    PROJECT_COMPATIBILITY_VERSION, PROJECT_FEATURE_PACK_VERSION, PROJECT_RELEASE_VERSION, BUILD_TYPE_INDICATOR)
PROJECT_FULL_NAME = '{} {}'.format(PROJECT_NAME, PROJECT_FULL_VERSION)
