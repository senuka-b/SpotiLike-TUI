from dotenv import load_dotenv
from spotipy import Spotify, SpotifyOAuth
from pynput import keyboard

from loguru import logger
from .database import Database

import sys, traceback


class SpotifyAPI:
    def __init__(self):
        load_dotenv()
        self.db = Database()

        self.sp = Spotify(auth_manager=SpotifyOAuth())

        try:
            self.username = self.sp.me()["display_name"]
        except Exception as e:
            raise e

        logger.info(f"Client authorised with username {self.username}")

    def run(self):
        playlists: dict = self.get_user_playlists()
        self.db._update_playlists(data=playlists)

    def _get_all_playlists(self):
        results = self.sp.current_user_playlists()

        tracks = results["items"]
        while results["next"]:
            results = self.sp.next(results)
            tracks.extend(results["items"])

        return tracks

    def get_user_playlists(self):
        """
        {
            "id": "playlist_name"
        }
        """
        data = self._get_all_playlists()
        _id = self.sp.me()["id"]

        return {item["id"]: item["name"] for item in data if item["owner"]["id"] == _id}

    def notify(self, message: str, log: bool = True, critical: bool = False):
        # TODO: IMPLEMENT NOTFICATIONS
        if log:
            logger.log("CRITICAL" if critical else "INFO", message)

        ...

    def _like(self, current):

        if not current or current["item"] is None:
            self.notify("Spotify is not playing anything", critical=True)
            return

        if self.sp.current_user_saved_tracks_contains(tracks=[current["item"]["id"]])[
            0
        ]:

            self.sp.current_user_saved_tracks_delete(tracks=[current["item"]["id"]])
            return self.notify(
                f"💔 Unliked [{current['item']['name']}] by {current['item']['album']['artists'][0]['name']}"
            )

        self.sp.current_user_saved_tracks_add(tracks=[current["item"]["id"]])

        self.notify(
            f"❤️ Liked [{current['item']['name']}] by {current['item']['album']['artists'][0]['name']}"
        )

    def save(self, value: str):
        # value = playlist id

        current = self.sp.current_playback()

        if value == "liked_songs":
            self._like(current)

        else:
            self.sp.playlist_add_items(value, items=[current["item"]["id"]])

            self.notify(
                f"❤ Saved [{current['item']['name']}] by {current['item']['album']['artists'][0]['name']} to [{self.db.get_playlist_by_id(id=value)[1]}] playlist."
            )


class SpotiLikeWorker:
    def __init__(self):
        self.db = Database()
        self.api = SpotifyAPI()

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            logger.critical("Exiting SpotiLike (cancelled by user)")
            sys.exit()

        else:
            traceback.print_exception(exc_type, exc_value, exc_traceback)

    def run(self):
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


if __name__ == "__main__":
    SpotifyAPI().run()
