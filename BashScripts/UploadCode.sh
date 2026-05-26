#!/bin/bash
set -e
HOST="wiseproject@WiseProject.local"
cd "$(pwd)"
cd ..
KEY=$(pwd)
KEY="${KEY}/PythonScripts"

echo "Copying Python files to ${HOST}:/home/wiseproject"

scp -r "${KEY}" "${HOST}:/home/wiseproject"

echo "Done"








