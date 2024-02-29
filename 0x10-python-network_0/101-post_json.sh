#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -s -X POST "$1" -d "$2"
