#!/bin/bash

# This script is used to build and prepare the Flask application for deployment.

# Exit immediately if a command exits with a non-zero status
set -e

# Install required packages from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# (Optional) Any other build steps can be added here
# For example, you might want to collect static files, etc.

echo "Build complete."
