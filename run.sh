#!/bin/bash

# Call fastAPI
!/bin/bash

# Start the Python file (replace 'your_script.py' with your Python file)
python main.py &

# Get the process ID (PID) of the last background process (Uvicorn)
uvicorn_pid=$!

# Sleep for a few seconds to allow Uvicorn to start (adjust as needed)
sleep 5

# Check if Uvicorn is running
if ps -p $uvicorn_pid > /dev/null; then
    echo "Uvicorn is running with PID $uvicorn_pid."
else
    echo "Uvicorn is not running."
    exit 1
fi