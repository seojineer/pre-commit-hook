# Pre Commit Hooks

## 1. Apply pre-commit hook configuration
Create pre-commit-config.yaml in Git repository
-----------------------------------------------
```
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: http://soc-vnv.gitlab.o/ci/pre-commit-hooks.git
    rev: "537b08927c0abd4be1dffc5bbd0cdce1f3198121"
    hooks:
      - id: checkpatch.pl
        name: run checkpatch.pl
        verbose: true
        stages: [commit]

-   repo: https://github.com/jlebar/pre-commit-hooks.git
    rev: "62ca83ba4958da48ea44d9f24cd0aa58633376c7"
    hooks:
      - id: clang-format-diff-15.0.0
        stages: [commit]

-   repo: https://github.com/commitizen-tools/commitizen
    rev: v2.37.0
    hooks:
    -   id: commitizen
        stages: [commit-msg]
    -   id: commitizen-branch
        args: [--rev-range, origin/master..HEAD]
        stages: [manual]
```
Install pre-commit
------------------
```
$ pre-commit install -t pre-commit -t commit-msg --install-hooks
```

## 2. Adding a new hook
Add a new hook script
---------------------
```
$ git clone http://soc-vnv.gitlab.o/ci/pre-commit-hooks
$ cd pre-commit-hooks/pre_commit_hooks
$ vim do-echo
#!/bin/bash
echo "test script"
$ chmod +x do-echo
```
Add hook information in pre-commit-hooks.yaml
---------------------------------------------
```
- id: echo
  name: run echo script
  description: >
    Sample hook
  entry: pre_commit_hooks/do-echo
  args: [-v]
  language: script
```
Update new hook
-----------------------------------
```
$ git add -u
$ git commit -m 'test: add a sample hook'
$ git push
```
Apply new hook to Git repository
--------------------------------
This is example that add a new hook in ketu-firmware repository.
```
$ git clone http://soc-vnv.gitlab.o/ketu/ketu-firmware
$ vim .pre-commit-config.yaml
repos:
-   repo: http://soc-vnv.gitlab.o/ci/pre-commit-hooks.git
    rev: ""
    hooks:
      - id: echo
        stages: [commit]
```
If you want to share pre-commit configuration with others, generate it to remote repository.
```
$ git add .pre-commit-config.yaml
$ git commit -m 'test: apply echo hook'
$ git push
```
