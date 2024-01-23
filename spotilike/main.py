from .api.main import SpotiLikeWorker
from .interface.SpotiLike import SpotiLike

import os
import argparse, sys, pynput, atexit


def main():

    parser = argparse.ArgumentParser(
        description=f"Save Spotify songs on-the-go while you're listening, to your Liked Songs library or your favourite playlists with custom hotkeys all through your keyboard! {os.getcwd()}",
    )

    parser.add_argument(
        "config", nargs="?", default="run", help="Run the configuration TUI"
    )

    args = parser.parse_args()


    if args.config == "config":
        atexit.register(lambda: pynput.keyboard.Controller().press(pynput.keyboard.Key.f11))

        pynput.keyboard.Controller().press(pynput.keyboard.Key.f11)

        SpotiLike.run(log="spotilike.log", title="SpotiLike <3")
    else:
        worker = SpotiLikeWorker()
        sys.excepthook = worker.handle_exception

        worker.run()


if __name__ == "__main__":
    main()
