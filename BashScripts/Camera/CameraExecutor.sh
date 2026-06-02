#!/bin/bash

#for now until camera.py is fixed
rpicam-still -o test.jpg

echo "$(pwd)"

scp ~/test.jpg ibrokhim@Ibrokhims-MacBook-Pro.local:~/Desktop/

#scp wiseproject@WiseProject.local:/path/to/image.jpg /path/to/destination/
#sftp://WiseProject.local

#REMEMBER CALL THIS IN A NEW TERMINAL WITHOUT USING CONNECT.SH OK!!
#scp wiseproject@WiseProject.local:/home/wiseproject/Images/processedImage.jpg /Users/ibrokhim/Desktop/