# Git pre-commit hook for python code quality

This project sets up a **git pre-commit hook** that automatically checks python code quality using **pylint** and formats the code using **Black** before committing changes.

---

## Features

-> Runs `pylint` on all staged python files before commit.
-> Automatically formats code with `black` before committing.
-> Prevents committing code with linting errors.
-> Ignores minor warnings (Refactore `R`, Convention `C`).
-> Ensures code quality in every commit.

---

## Setup Instructions

### Install required tools

Ensure both `pylint` and `black` are installed:
'''pip install pylint black'''

### create the pre-commit hook

Navigate to the .git/hooks/ folder and create a pre-commit file:
'''touch pre-commit'''

In this file, write the bash script for running pylint and black:
'''
#!/bin/bash

echo "Running pylint on staged python files"

files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ -z "$files" ]; then
echo "No python files staged. skipping check."
exit 0
fi

python -m black $files
git add $files

for file in $files; do
python -m pylint --disable=R,C $file
if [ $? -ne 0 ]; then
echo "pylint found issues in $file. Fix them before committing."
exit 1
fi
done

echo "Code quality check passed. Proceeding with commit."
exit 0
'''

### Make the hook executable

'''chamod +x .git/hooks/pre-commit'''

### Test the hook

Try committing the python file(main.py)
'''git add main.py
git commit -m "Initial commit"
'''

If black finds formatting issues, it auto-formats the code and stages it.
If pylint finds issues, the commit will be blocked until fixed.
If everything passes, the commit will proceed as normal.
