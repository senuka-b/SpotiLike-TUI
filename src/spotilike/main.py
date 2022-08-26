import sys, os

sys.path.append(os.path.realpath(__file__) + "/../")

from pynput import keyboard

from api.main import SpotifyAPI
from api.database import Database


class SpotiLikeWorker:
    def __init__(self):
        self.db = Database()
        self.api = SpotifyAPI()

    def start_thread(self):
        self.thread = keyboard.GlobalHotKeys(self.create_hotkeys())
        self.thread.start()
        self.thread.join()

    def create_hotkeys(self):
        data = self.db.get_all_hotkeys()

        keys = {}

        for item in data:
            for id, hotkey in (item,):
                if hotkey:
                    keys[hotkey] = lambda value=id: self.api.save(value)

        return keys

    def restart_thread(self):
        self.thread.stop()
        self.thread.start()


if __name__ == "__main__":
    SpotiLikeWorker().start_thread()
