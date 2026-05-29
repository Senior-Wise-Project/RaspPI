#!/bin/bash

#for now until camera.py is fixed
rpicam-still -o test.jpg

echo "$(pwd)"

scp ~/test.jpg robertzamora@Roberts-MacBook-Pro.local:~/Desktop/