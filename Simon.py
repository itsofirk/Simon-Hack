import keyboard
from utils.mouse import record_buttons, click_pixel, get_mouse_position, set_mouse_position
from utils.screen import get_pixel_color
from win32api import Sleep

SLEEP_BETWEEN_COMPUTER = 600
SLEEP_BETWEEN_CLICKS = 1000


class Simon:
    def __init__(self):
        self.buttons = record_buttons()
        self.base_colors = self.__get_base_colors(self.buttons)
        self.moves = []
        self.recording = True
        keyboard.add_hotkey('p', callback=self.__switch__, args=(False,), suppress=True)

    def __get_base_colors(self, buttons):
        set_mouse_position((0, 0))
        return [get_pixel_color(*pt) for pt in buttons]

    def record_simon(self):
        for i, pos in enumerate(self.buttons):
            curr_color = get_pixel_color(*pos)
            if self.base_colors[i] != curr_color:
                self.moves.append(pos)
                print(f"Recorded {i + 1} button")
                Sleep(SLEEP_BETWEEN_COMPUTER)

    def play_record(self):
        start_position = get_mouse_position()
        print(f"Executing moves: {self.moves}")
        while self.moves:
            mv = self.moves.pop(0)
            Sleep(SLEEP_BETWEEN_CLICKS)
            click_pixel(*mv)
        set_mouse_position(start_position)
        Sleep(SLEEP_BETWEEN_COMPUTER)
        self.__switch__(True)

    def __switch__(self, flag):
        self.recording = flag

    def play(self):
        print("Press P to play recording")
        print("Recording...")
        loops = 0
        while True:
            if self.recording:
                self.record_simon()
            else:
                self.play_record()


if __name__ == '__main__':
    s = Simon()
    s.play()
