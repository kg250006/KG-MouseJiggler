"""
macOS CoreGraphics mouse input wrapper.

This module provides mouse movement using the Quartz CoreGraphics API,
mirroring the interface of win32_input.py for cross-platform compatibility.
"""

import Quartz


def _get_mouse_position():
    """Get the current mouse cursor position."""
    event = Quartz.CGEventCreate(None)
    point = Quartz.CGEventGetLocation(event)
    return point.x, point.y


def send_mouse_input(delta: int) -> bool:
    """
    Send a relative mouse movement event using macOS CoreGraphics.

    Args:
        delta: The number of pixels to move the mouse along both X and Y axes.
               Positive values move right/down, negative values move left/up.

    Returns:
        True if the event was posted successfully, False otherwise.
    """
    try:
        x, y = _get_mouse_position()
        event = Quartz.CGEventCreateMouseEvent(
            None,
            Quartz.kCGEventMouseMoved,
            (x + delta, y + delta),
            0,
        )
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        return True
    except Exception:
        return False


def jiggle(delta: int = 1) -> None:
    """
    Jiggle the mouse by sending a small movement event.

    Args:
        delta: The movement amount in pixels (default: 1).
    """
    send_mouse_input(delta)
