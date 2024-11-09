# Features tracker

Back to [README](README.md)

### Dev-critical

### Alpha-critical

### Beta-critical

### Critical

### Priority

### Nice to have

### Backlog

## Versions and release process

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
   Version numbers: `0.0.?x`
2. Alpha: Project is unstable and may have critical bugs.  
   Version numbers: `0.?.?a`
3. Beta: Project is unstable, but generally usable.  
   Version numbers: `1.?.?b`
4. Stable "Nightly" builds: Builds from `master` with the newest features.  
   Version numbers: `?.?.?d`
5. Stable release: Builds from `release`, best quality-wise.  
   Version numbers: `?.?.?r`

### Branches

* `release`: Stable branch from which releases are generated. Should be updated only from `master`.
* `master`: General development branch. Single-commit features or fixes can be submitted directly.
* `dev-...`: Branches for changes that should be split into multiple commits. 
