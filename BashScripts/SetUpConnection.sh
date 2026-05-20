#!/bin/bash
#only run once

set -e
KEY="$HOME/.ssh/id_ed25519"

if [ ! -f "$KEY" ]; then
  echo "No SSH key found. Generating one..."
  ssh-keygen -t ed25519 -N "" -f "$KEY"
else
  echo "SSH key already exists: $KEY"
fi

echo "Copying key to $HOST ..."
sudo ssh-copy-id -i "${KEY}.pub" wiseproject@192.168.1.151