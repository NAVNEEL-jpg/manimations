#!/usr/bin/env bash
set -e

echo "========================================================"
echo "   Welcome to Manim AI Studio Setup (macOS / Linux)"
echo "========================================================"

# 1. Check or install uv
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo " uv is installed."
fi

# 2. Check ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "[WARNING] ffmpeg is not installed. Please install it (e.g. brew install ffmpeg or sudo apt install ffmpeg)."
else
    echo " ffmpeg is installed."
fi

# 3. Install dependencies
echo "Setting up Python & Manim dependencies..."
uv sync --python 3.11

echo "Setup Complete!"
