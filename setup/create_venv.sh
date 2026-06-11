#!/usr/bin/env sh

set -e

ENV_NAME="./venv"

# Check if conda is installed

if ! command -v conda >/dev/null 2>&1; then
echo "Error: Conda is not installed."
exit 1
fi

echo "Conda version:"
conda --version

# Initialize conda for non-interactive shells

CONDA_BASE="$(conda info --base)"

# shellcheck disable=SC1091

. "$CONDA_BASE/etc/profile.d/conda.sh"

# Create environment if it doesn't exist

if [ -d "$ENV_NAME" ]; then
echo "It is detected that an existing Conda environment '$ENV_NAME' exists. Do you want to restart the setup process (The environment will be removed and recreated)? (y/N)"
read -r response
if [ "$response" = "y" ]; then
conda env remove -p "$ENV_NAME"
echo "Creating Conda environment '$ENV_NAME' with latest supported Python..."
conda  create -p "$ENV_NAME"
else
echo "Exiting without changes."
exit 0
fi
else
echo "Creating Conda environment '$ENV_NAME' with latest supported Python..."
conda  create -p "$ENV_NAME"
fi

echo "Installing dependencies from environment.yml..."
conda env update -p "$ENV_NAME" -f setup/environment.yml

# Activate environment

echo "Activating Conda environment..."

echo "Python version:"
python --version

echo "Running on architecture: $(uname -m)"

# Upgrade pip

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Conda environment setup complete!"
echo "Activate later with:"
echo "  conda activate $ENV_NAME"
