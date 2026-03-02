#!/usr/bin/env sh

set -e

# Detect latest available Python
if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN=$(command -v python3)
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN=$(command -v python)
else
    echo "Error: Python is not installed."
    exit 1
fi

echo "Using Python: $PYTHON_BIN"
$PYTHON_BIN --version

# Create virtual environment
echo "Creating virtual environment 'venv'..."
$PYTHON_BIN -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
# shellcheck disable=SC1091
. venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements if file exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping dependency installation."
fi

echo "Virtual environment setup complete!"
echo "Activate later using: source venv/bin/activate"