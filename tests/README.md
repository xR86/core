# core

## tests

### `test_git*`

#### `test_git.py` - Git Guidelines tests

Checks mainly for `.gitignore`.  

Should also check for git guidelines set-up by the individual / org (in flags in this test or in some yaml file), such as commit conventions (eg: starts with caps or not, has a comment ...).

#### `test_github.community.py` - Github Community Guidelines tests

Checks for these files (with or without the markdown extension):
+ `README.md`
+ `LICENSE.md`
+ `CODE_OF_CONDUCT.md`
+ `CONTRIBUTING.md`
+ `ISSUE_TEMPLATE.md`
+ `PULL_REQUEST_TEMPLATE.md`

While `README` and `LICENSE` are mandatory, the other doc files are not. As such, you can optionally reinforce these docs by:
+ setting `flag_community = True` in `test_github_community.py`
+ or `flag_community: False` in `project_config.yaml` (as defined in `spec_project_config.md`)


---
