import win32con
import win32gui
import keyboard
import re


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        # keyboard.send()

        win32gui.SetForegroundWindow(self._handle)


if __name__ == '__main__':
    # w = WindowMgr()
    # w.find_window_wildcard(".*Python.*")
    hwnd = win32gui.GetForegroundWindow()

    keyboard.press_and_release('alt')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWDEFAULT)
