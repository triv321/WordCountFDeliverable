#!/bin/bash
# Start the PCB Pro API server

echo "Starting PCB Pro API Server..."
cd "$(dirname "$0")"
/usr/bin/python3 api.py
