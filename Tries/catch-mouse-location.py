import threading
import keyboard

import win32gui


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


query_mouse_position = win32gui.GetCursorPos


def record_colors(hotkey='k'):
    if not hotkey:
        raise KeyError('The hotkey must be in the format `ctrl+shift+a, s`.')
    positions = []
    print("In order to track color changes, please place the cursor over each button")
    for i in range(4):
        print(f"Capturing Point {i + 1}/4")
        print(f"Press {hotkey} when mouse is placed")
        keyboard.wait(hotkey)
        positions.append(
            query_mouse_position()
        )
    return positions


if __name__ == '__main__':
    pos_list = record_colors()
    print(pos_list)
    print("Exiting...")
