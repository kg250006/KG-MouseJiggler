"""
Cross-platform mouse input abstraction.

Imports the correct platform-specific module based on the current OS.
"""

import sys

if sys.platform == "win32":
    from win32_input import send_mouse_input, jiggle
elif sys.platform == "darwin":
    from macos_input import send_mouse_input, jiggle
else:
    raise RuntimeError(f"Unsupported platform: {sys.platform}. Only Windows and macOS are supported.")

__all__ = ["send_mouse_input", "jiggle"]
