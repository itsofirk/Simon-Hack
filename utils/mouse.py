import keyboard
import win32gui
import win32api
import win32con


def click_pixel(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


get_mouse_position = win32gui.GetCursorPos
set_mouse_position = win32api.SetCursorPos


def record_buttons(hotkey='k'):
    positions = []
    print("Please place the cursor over each button")
    for i in range(4):
        print(f"Capturing Point {i + 1}/4 ...")
        print(f"Press {hotkey} when mouse is placed")
        keyboard.wait(hotkey, suppress=True)
        positions.append(
            win32gui.GetCursorPos()
        )
    return positions
