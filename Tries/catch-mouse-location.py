import threading

import win32gui


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


query_mouse_position = win32gui.GetCursorPos

if __name__ == '__main__':
    print("Press Ctrl-K when mouse is placed")
    print("Capturing now...")

    set_interval(query_mouse_position, 0.1)

    print("Exiting...")
