import win32con
import win32gui
import keyboard


def focus_on_return(func, *args):
    hwnd = win32gui.GetForegroundWindow()
    func(*args)
    keyboard.press_and_release('alt')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWDEFAULT)


def check_function(key):
    print(f"Press {key}")
    keyboard.wait(key)
    print("Hit!")


if __name__ == '__main__':
    focus_on_return(check_function, 'ctrl+k')
