#!/bin/bash
cd "$(dirname "$0")"
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""
echo "Done! You can now run the mouse jiggler with: python mouse_jiggler.py"
