#!/bin/bash

# Change directory to the script's location
cd "$(dirname "$0")"
echo "Starting up..."
# Check if linsysmon_venv exists, if not create it
if [ ! -f "linsysmon_venv/bin/activate" ]; then
    rm -rf linsysmon_venv
    python3 -m venv linsysmon_venv
fi
# Activate the environment
source linsysmon_venv/bin/activate
# Upgrade pip
pip install --upgrade pip --quiet
# Install/Update dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
fi
# Check for OpenAI Key
if [ -z "$OPENAI_API_KEY" ]; then
    read -p "Please enter your OpenAI API Key: " OPENAI_API_KEY
    export OPENAI_API_KEY
fi
python agent.py