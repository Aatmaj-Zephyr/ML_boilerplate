#!/bin/bash

set -e

echo "Activating virtual environment..."
source venv/bin/activate

echo "Moving files..."
mv outputs/* old_outputs/ 2>/dev/null || true

echo "Running main.py in production mode"
python -o main.py --mode prod