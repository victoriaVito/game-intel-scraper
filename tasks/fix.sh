#!/bin/bash
# fix.sh - check for syntax errors in the project and report them.
# This script compiles all Python files to detect syntax errors.
# If syntax errors are found, it will print a message.

echo "Running syntax check on project..."
# Find all Python files in parent directory and attempt to compile them
PY_ERR=0
while IFS= read -r file; do
    python3 -m py_compile "$file" 2>/dev/null || PY_ERR=1
done < <(find .. -name "*.py" -not -path "*/venv/*")

if [ $PY_ERR -ne 0 ]; then
    echo "Syntax errors detected in the codebase. Please fix them before proceeding."
else
    echo "No syntax errors detected. Codebase looks good!"
fi
