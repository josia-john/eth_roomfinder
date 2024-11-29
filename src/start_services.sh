#!/bin/bash

# Start cron in the background
cron &

# Fetch the files in the background
python fetchFiles.py &

# Start the Python server
gunicorn --bind 0.0.0.0:8000 app:app