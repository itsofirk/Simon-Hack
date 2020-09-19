import win32gui


def get_pixel_color(x, y):
    desktop_window_id = win32gui.GetDesktopWindow()
    desktop_window_dc = win32gui.GetWindowDC(desktop_window_id)
    long_colour = win32gui.GetPixel(desktop_window_dc, x, y)
    color = int(long_colour)
    win32gui.ReleaseDC(desktop_window_id, desktop_window_dc)
    return (color & 0xff), ((color >> 8) & 0xff), ((color >> 16) & 0xff)
