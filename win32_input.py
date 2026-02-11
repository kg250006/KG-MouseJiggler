"""
Windows API structures and SendInput wrapper for mouse input.

This module provides ctypes-based access to the Windows SendInput API,
mirroring the functionality of the C# Helpers.Jiggle() method.
"""

import ctypes
from ctypes import wintypes

# Windows API constants
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001


class MOUSEINPUT(ctypes.Structure):
    """
    Windows MOUSEINPUT structure for SendInput.

    See: https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
    """
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]


class INPUT(ctypes.Structure):
    """
    Windows INPUT structure for SendInput.

    See: https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
    """
    class _INPUT_UNION(ctypes.Union):
        _fields_ = [
            ("mi", MOUSEINPUT),
            # ki (KEYBDINPUT) and hi (HARDWAREINPUT) omitted - not needed for mouse jiggle
        ]

    _anonymous_ = ("_input",)
    _fields_ = [
        ("type", wintypes.DWORD),
        ("_input", _INPUT_UNION),
    ]


# Load user32.dll
_user32 = ctypes.WinDLL("user32", use_last_error=True)

# Configure SendInput function
_SendInput = _user32.SendInput
_SendInput.argtypes = [wintypes.UINT, ctypes.POINTER(INPUT), ctypes.c_int]
_SendInput.restype = wintypes.UINT


def send_mouse_input(delta: int) -> bool:
    """
    Send a relative mouse movement event using Windows SendInput API.

    This mirrors the C# Helpers.Jiggle() method, sending a single mouse
    movement event with the specified delta applied to both X and Y axes.

    Args:
        delta: The number of pixels to move the mouse along both X and Y axes.
               Positive values move right/down, negative values move left/up.

    Returns:
        True if the input was successfully inserted into the input stream,
        False otherwise.

    Example:
        # Move mouse 1 pixel diagonally
        send_mouse_input(1)

        # Move mouse back
        send_mouse_input(-1)
    """
    mouse_input = MOUSEINPUT(
        dx=delta,
        dy=delta,
        mouseData=0,
        dwFlags=MOUSEEVENTF_MOVE,
        time=0,
        dwExtraInfo=None,
    )

    inp = INPUT(
        type=INPUT_MOUSE,
        mi=mouse_input,
    )

    result = _SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    if result != 1:
        error_code = ctypes.get_last_error()
        # Log error for debugging but don't raise - matches C# behavior
        import logging
        logging.debug(
            f"SendInput failed: result={result}, error_code=0x{error_code:08x}"
        )
        return False

    return True


def jiggle(delta: int = 1) -> None:
    """
    Jiggle the mouse by sending a small movement event.

    This is a convenience wrapper around send_mouse_input that provides
    a simple interface for the common use case of jiggling the mouse
    to prevent screen lock or keep-alive.

    Args:
        delta: The movement amount in pixels (default: 1).
               The mouse moves diagonally by this amount.
    """
    send_mouse_input(delta)
