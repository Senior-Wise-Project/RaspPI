#!/bin/bash
set -e
HOST="wiseproject@192.168.1.151"
cd "$(pwd)"
cd ..
KEY=$(pwd)
KEY="${KEY}/PythonScripts"

echo "Copying Python files to ${HOST}:/home/wiseproject"

scp -r "${KEY}" "${HOST}:/home/wiseproject"

echo "Done"








