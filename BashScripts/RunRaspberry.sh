#!/bin/bash
scp "$(pwd)/LocalRaspberryExecutor.sh" wiseproject@WiseProject.local:
echo "-------------------GOING INTO RASPBERRY---------------------"
echo "-----------------------------------------------------------"
ssh -t wiseproject@WiseProject.local "bash ~/LocalRaspberryExecutor.sh"
