#!/bin/bash

PY_DIR="$(pwd)/PythonScripts"

while true; do
  ls "$PY_DIR"

  read -p "Enter file name: " INPUT

  FILE_PATH="${PY_DIR}/${INPUT}.py"

  if [[ -f "$FILE_PATH" ]]; then
    echo "File found: $INPUT"
    echo "Running script..."
    cd "$PY_DIR"
    python $FILE_PATH
    break
  else
    echo "File not found. Try again."
  fi
done