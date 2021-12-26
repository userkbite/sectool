#!/usr/bin/bash

apt-get update
apt-get upgrade
apt-get install -y  python3
pip install requests

echo "[i] all dependencies have already been installed, run the command \"python3 secdet.py\" to run the script"
