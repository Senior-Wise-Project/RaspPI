#!/bin/bash
scp "$(pwd)/CameraExecutor.sh" wiseproject@WiseProject.local:
echo "-------------------GOING INTO RASPBERRY---------------------"
echo "-----------------------------------------------------------"

#this is kind of cool in this line its saying go into the raspberry and run code to take picture and send back to laptop
ssh wiseproject@WiseProject.local "bash ~/CameraExecutor.sh"

#then on this line its saying go back into laptop and open the picture
ssh -i ~/.ssh/id_ed25519 robertzamora@Roberts-MacBook-Pro.local "open ~/Desktop/test.jpg"