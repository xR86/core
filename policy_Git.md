# core

## Git requirements

### .gitignore:
+ use `.gitignore` for the languages found in that repo, ignoring:
  + compiled files (eg: `.bin`, `.pyc`, `.class` etc.);
  + data files (with the exception of small `sqlite` files);
  + big binaries (eg: `.exe`);
  + libraries (eg: `node_modules`, `bower_components` etc.).
+ use a common `.gitignore` like the one found in **this repo** (language and project-agnostic):
+ if there are important root folders, use one level of nesting for `.gitignore` (a main `.gitignore` for the main problems, and shallow nested `.gitignores` for specific files or folders) - this allows for cleaner root gitignore, and easier tracking of files that should be removed from `.gitignore`
+ `TODO`: some Git workflow described here ?


### Commits:
+ commit wording (reflect this in `.gitignore`):
  + fix - something is broken
  + patch - something is added
  + ...


### Code quality:
+ `Proposal`: refactor passes:
  + open issue with targeted feature - eg: javadoc
  + mark with emoji in commit and add reference to issue (without closing)
    + no emoji == no refactor passes
    + evaluating quality of code by the number of emojis (eg: 2 emojis - slightly better than 1 ...)

