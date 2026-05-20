#!/bin/bash
scp "$(pwd)/LocalRaspberryExecutor.sh" wiseproject@192.168.1.151:
echo "-------------------GOING INTO RASPBERRY---------------------"
echo "-----------------------------------------------------------"
ssh -t wiseproject@192.168.1.151 "bash ~/LocalRaspberryExecutor.sh"
