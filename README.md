# Mouse Jiggler

A simple Python utility that prevents your screen from locking by subtly moving the mouse every 60 seconds. Works on both **Windows** and **macOS**.

## Installation

1. Ensure Python 3.8+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   On Windows, you can also run `install.bat` which will install all dependencies automatically.

> **macOS note:** On first run, macOS will prompt you to grant **Accessibility** permissions to your terminal or Python. The jiggler needs this to move the mouse. Go to System Settings > Privacy & Security > Accessibility and enable your terminal app.

## Usage

### Standard Launch
Run the script:
```bash
python mouse_jiggler.py
```

A green circle icon will appear in your system tray (Windows) or menu bar (macOS) indicating the jiggler is active. Right-click the icon to access the menu:

- **Pause**: Temporarily stop mouse movement (icon turns gray)
- **Resume**: Resume mouse movement when paused (icon turns green)
- **Exit**: Close the application

### Windows: Hidden Launch (No Console Window)
For a cleaner experience without a console window, use the VBScript launcher:
```bash
wscript run-MouseJiggler.vbs
```
Or double-click `run-MouseJiggler.vbs` directly in Windows Explorer.

This method uses `pythonw.exe` (the windowless Python interpreter) to run the jiggler completely in the background with no visible command prompt window. The system tray icon remains visible for control.

**Tip:** Add `run-MouseJiggler.vbs` to your Windows Startup folder to automatically start the jiggler when you log in.

### macOS: Background Launch
Run the jiggler in the background using `nohup`:
```bash
nohup python mouse_jiggler.py &
```

**Tip:** Add the command to your Login Items (System Settings > General > Login Items) to start it automatically.

## How It Works

The application runs in the background and moves the mouse 4 pixels diagonally and then back every 60 seconds. The movement alternates direction each cycle, making it imperceptible during normal use while being sufficient to prevent screen lock and sleep timers from activating.

### Platform-Specific Mouse Input

The jiggler uses low-level OS APIs for mouse movement rather than higher-level automation libraries like pyautogui. A cross-platform abstraction (`mouse_input.py`) selects the correct backend at runtime:

**Windows — SendInput API** (`win32_input.py`)

Uses ctypes to call the Windows `SendInput` API via `user32.dll`, injecting relative mouse movement events (`MOUSEEVENTF_MOVE`) directly into the input stream. The events are indistinguishable from actual hardware input.

**macOS — CoreGraphics** (`macos_input.py`)

Uses the Quartz CoreGraphics framework (`CGEventCreateMouseEvent` / `CGEventPost`) to post mouse-moved events at the HID event tap level. Gets the current cursor position and applies a relative delta, matching the Windows behavior.

Both approaches offer:
1. **Low-level access** — Events are injected at the OS input layer
2. **Relative movement** — Cursor moves from its current position, no teleportation
3. **Lightweight** — Direct API calls with minimal overhead

### Features

- Cross-platform: Windows and macOS
- System tray / menu bar icon with visual status (green = active, gray = paused)
- Pause/Resume functionality without closing the application
- Hidden launch mode for background operation without console window (Windows)
- Minimal resource usage with background threading
- Clean shutdown handling

## Requirements

- Python 3.8+
- Windows or macOS
- Dependencies:
  - pystray >= 0.19.0
  - Pillow >= 10.0.0
  - pyobjc-framework-Quartz >= 10.0 (macOS only, installed automatically)

## Files

| File | Description |
|------|-------------|
| `mouse_jiggler.py` | Main application with system tray interface |
| `mouse_input.py` | Cross-platform mouse input abstraction |
| `win32_input.py` | Windows SendInput API wrapper using ctypes |
| `macos_input.py` | macOS CoreGraphics mouse input wrapper |
| `run-debug.bat` | Windows launcher (shows console window) |
| `run-MouseJiggler.vbs` | Windows hidden launcher (no console window) |
| `install.bat` | Windows dependency installer script |
| `requirements.txt` | Python package dependencies |

## License

MIT
